import streamlit as st
import math as mt

TITULO = "Cálculo de área de um Quadrado, Triângulo e Trapézio"
st.markdown("<h1 style='text-align: center; color: red;'>{}</h1>".format(TITULO), unsafe_allow_html=True)

medidaA = st.number_input("Digite a medida A:")
medidaB = st.number_input("Digite a medida B:")
medidaC = st.number_input("Digite a medida C:")

area_quadrado = mt.pow(medidaA, 2)
area_triangulo = (medidaA * medidaB) / 2
area_trapezio  = ((medidaA + medidaB) * medidaC) / 2

st.write(f"A área do quadrado é: {area_quadrado:.4f}")
st.write(f"A área do triângulo é: {area_triangulo:.4f}")
st.write(f"A área do trapézio é: {area_trapezio:.4f}")