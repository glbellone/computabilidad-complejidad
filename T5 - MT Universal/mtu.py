import sys

BITS = 2
BLANCO = "10"
LARGO_REGISTRO = 5 * BITS
MOVIMIENTOS = {"00": "R", "01": "L", "10": "S"}


class MTU:
    def __init__(self, cinta_mtu):
        self.pasos = 0
        self.detenida = False

        if cinta_mtu.count("$") != 1:
            raise ValueError("la cinta tiene que tener exactamente un $")

        izquierda, derecha = cinta_mtu.split("$")
        reg0, *self.registros = derecha.split("#")

        if len(reg0) != 2 * BITS:
            raise ValueError(f"el registro 0 ({reg0}) tiene que tener {2 * BITS} bits: "
                             "estado + simbolo leido")

        if not self.registros or self.registros == [""]:
            raise ValueError("no hay tabla de transiciones despues del registro 0")

        for r in self.registros:
            if len(r) != LARGO_REGISTRO:
                raise ValueError(f"el registro {r} tiene {len(r)} bits y tiene que tener {LARGO_REGISTRO}")
            if r[-BITS:] not in MOVIMIENTOS:
                raise ValueError(f"el registro {r} termina en {r[-BITS:]}, que no es un movimiento "
                                 "(R = 00, L = 01, S = 10)")

        for r in [reg0, *self.registros]:
            if set(r) - {"0", "1"}:
                raise ValueError(f"'{r}' tiene simbolos que no son 0 ni 1")

        self.estado = reg0[:BITS]
        self.leido = reg0[BITS:]
        self.cinta = self._partir(izquierda)
        self.pos = self.cinta.index("*")

    def _partir(self, izquierda):
        if izquierda.count("*") != 1:
            raise ValueError("la cinta de M tiene que tener exactamente un * (el cabezal)")

        casilleros, i = [], 0

        while i < len(izquierda):
            if izquierda[i] == "*":
                casilleros.append("*")
                i += 1
            else:
                casillero = izquierda[i:i + BITS]
                if len(casillero) != BITS or set(casillero) - {"0", "1"}:
                    raise ValueError(f"la cinta de M no se puede partir en simbolos de {BITS} bits")
                casilleros.append(casillero)
                i += BITS

        return casilleros

    def paso(self):
        reg0 = self.estado + self.leido

        registro = next((r for r in self.registros if r.startswith(reg0)), None)
        if registro is None:
            self.detenida = True
            return False

        estado_sig = registro[4:6]
        escribe = registro[6:8]
        mov = MOVIMIENTOS[registro[8:10]]

        self.estado = estado_sig

        self.cinta[self.pos] = escribe

        if mov == "R":
            self.pos += 1
            if self.pos == len(self.cinta):
                self.cinta.append(BLANCO)
        elif mov == "L":
            if self.pos == 0:
                self.cinta.insert(0, BLANCO)
            else:
                self.pos -= 1

        self.leido = self.cinta[self.pos]
        self.cinta[self.pos] = "*"

        self.pasos += 1
        return True

    def ejecutar(self, max_pasos=1000, mostrar=True, pausa=False):
        if mostrar:
            self.mostrar()

        while self.pasos < max_pasos:
            if pausa:
                input("          [Enter] siguiente paso ")
            if not self.paso():
                break
            if mostrar:
                self.mostrar()

    def __str__(self):
        return "".join(self.cinta) + "$" + self.estado + self.leido + "#" + "#".join(self.registros)

    def cinta_de_m(self):
        return " ".join(f"[{self.leido}]" if c == "*" else c for c in self.cinta)

    def salida(self):
        casilleros = [self.leido if c == "*" else c for c in self.cinta]

        while casilleros and casilleros[0] == BLANCO:
            casilleros.pop(0)
        while casilleros and casilleros[-1] == BLANCO:
            casilleros.pop()

        return " ".join(casilleros)

    def mostrar(self):
        print(f"paso {self.pasos:>2}:  {self}")
        print(f"          estado {self.estado}   cinta de M:  {self.cinta_de_m()}")


def main():
    print("MTU - Maquina de Turing Universal")
    print("Formato: cinta de M $ registro 0 # registro # registro ...  (2 bits por campo)\n")

    while True:
        cinta = input("Cinta de la MTU: ").strip()
        try:
            u = MTU(cinta)
            break
        except ValueError as error:
            print(f"Error: {error}. Proba de nuevo.\n")

    modo = ""
    while modo not in ("c", "p"):
        modo = input("Ejecutar completo (c) o por pasos (p)? ").strip().lower()
    print()

    u.ejecutar(pausa=(modo == "p"))

    print()
    if u.detenida:
        print(f"M se detuvo en el estado {u.estado} despues de {u.pasos} pasos.")
    else:
        print("M no se detuvo en 1000 pasos (capaz no para nunca).")
    print("Cinta final de M:", u.salida() or "(vacia)")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nCortado.")
