import streamlit as st
import math
    # progrma pro cesar lindo careca fofo programador OO 🌟
st.header("Verificação de Triângulo e Cálculo de Perímetro ou Área")
# entrada de dados
a = st.number_input("Digite o valor de A", min_value=0.0)
b = st.number_input("Digite o valor de B", min_value=0.0)
c = st.number_input("Digite o valor de C", min_value=0.0)
st.button("Calcular")
# processamento 
if a > 0 and b > 0 and c > 0:
    if a + b > c and b + c > a and c + a > b:
        perimetro = a + b 
        s = perimetro / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c)) 
# saida
        st.success("Os valores formam um triângulo!")
        st.write(f"Perímetro = {perimetro}")
        st.write(f"Área = {area:.1f}")
    else:
        area_trapezio = ((a + b) * c) / 2
        st.error("Os valores não formam um triângulo.")
        st.write(f"Área = {area_trapezio:.1f}")
else:
    st.warning("Por favor, insira valores positivos para os lados.")