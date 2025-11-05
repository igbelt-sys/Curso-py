import streamlit as st
st.title("problema retangulo")
base = st.number_input("Digite a base do triangulo:")
altura = st.number_input("Digite a altura do triangulo:")

area = base * altura
perimetro  = 2 *(base + altura)
diagonal = (base**2 + altura**2)**0.5
st.write(f"A área do retângulo é: {area:.2f}")
st.write(f"O perímetro do retângulo é: {perimetro:.2f}")
st.write(f"A diagonal do retângulo é: {diagonal:.2f}")