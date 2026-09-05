## MT Lenguaje Regular

### Definición del Lenguaje ($L_1$)

**Alfabeto:**
$$\Sigma = \{a, b\}$$

**Expresión Formal:**
$$L_1 = \{ w \in \{a,b\}^* \mid |w|_a \text{ es par} \}$$

**Descripción Coloquial:**
Lenguaje formado por todas las cadenas de $a$'s y $b$'s que poseen un número par de apariciones de la letra $a$.

La Máquina de Turing que reconoce este lenguaje se encuentra en `MT-cantidad-a-pares.jff`.

---

## MT Lenguaje Libre de Contexto

### Definición del Lenguaje ($L_2$)

**Propuesta:**
$$L_{cfl} = \{ a^n b^{2n} \mid n \ge 1 \}$$
(Por cada letra $a$, debe haber exactamente el doble de letras $b$ a su derecha).

**Expresión Formal:**
$$L_2 = \{ a^n b^{2n} \mid n \ge 1 \}$$

**Alfabeto de Entrada:**
$$\Sigma = \{a, b\}$$

**Condición Coloquial:**
Cadenas formadas por una secuencia de $n$ letras $a$ seguidas por el doble ($2n$) de letras $b$.

---

## Tabla Comparativa: MT Aceptadora vs. MT Calculadora

| Criterio | MT accept (Aceptadora / Decididora) | MT calc (Calculadora / Computadora) |
|---|---|---|
| **Propósito** | Decidir si una cadena $w$ pertenece al lenguaje $L$ ($w \in L$). | Calcular el valor de una función $f(x) = y$. |
| **Resultado final** | Un estado de Aceptación ($q_{acc}$) o Rechazo ($q_{rej}$). | La cadena respuesta escrita sobre la cinta en el estado de Parada ($q_{halt}$). |
| **Entrada** | Una cadena de entrada (ej: $aabbbb$). | Un argumento de entrada (ej: el número $3$ en unario $111$). |
| **Salida típica** | Un valor booleano: Sí / No. | El resultado computado (ej: $11111$ para una suma). |
| **Ejemplo de aplicación** | Comprobar si $w \in \{a^n b^{2n}\}$. | Duplicar la cantidad de unos en la cinta: $f(1^n) = 1^{2n}$. |
