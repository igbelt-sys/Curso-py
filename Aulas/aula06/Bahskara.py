import streamlit as st
import math as mt

st.header('Fórmula de Bhaskara')
st.write("Calculadora de raízes de uma equação do segundo grau") 
st.write("ax² + bx + c = 0")

a = st.text_input("Digite o valor de A:")
b = st.text_input("Digite o valor de B:")
c = st.text_input("Digite o valor de C:")

if st.button("Calcular"):
    try:
        a = float(a)
        b = float(b)
        c = float(c)

        delta = mt.pow(b, 2) - 4*a*c

        if delta < 0:
            st.warning("A equação não possui raízes reais.")
        elif delta == 0:
            raiz3 = (-b) / (2*a)
            st.success(f"A equação possui uma raiz real: x = {raiz3:.2f}")
        else:
            raiz1 = (-b + mt.sqrt(delta)) / (2*a)
            raiz2 = (-b - mt.sqrt(delta)) / (2*a)
            st.success(f"A equação possui duas raízes reais:\nx₁ = {raiz1:.2f}\nx₂ = {raiz2:.2f}")

    except:
        st.error("Por favor, insira valores válidos.")
