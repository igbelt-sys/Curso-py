
import math as mt
from streamlit import header, write, text_input, button, warning, success, error

# funcao python
def calculo(deltafunc):
     valor = mt.sqrt(delta) / (2*a)
     return valor

header('Fórmula de Bhaskara')
write("Calculadora de raízes de uma equação do segundo grau") 
write("ax² + bx + c = 0")

a = text_input("Digite o valor de A:")
b = text_input("Digite o valor de B:")
c = text_input("Digite o valor de C:")

if button("Calcular"):
    try:
        a = float(a)
        b = float(b)
        c = float(c)

        delta = mt.pow(b, 2) - 4*a*c

        if delta < 0:
            warning("A equação não possui raízes reais.")
        elif delta == 0:
            raiz3 = calculo(delta)
            success(f"A equação possui uma raiz real: x = {raiz3:.2f}")
        else:
            raiz1 = calculo (delta)
            raiz2 = calculo(delta)
            (f"A equação possui duas raízes reais:\nx₁ = {raiz1:.2f}\nx₂ = {raiz2:.2f}")

    except:
        error("Por favor, insira valores válidos.")
