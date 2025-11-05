import streamlit as st

st.markdown("<h1 style = 'text-align: center;'>Calculo de trângulos</h1>",unsafe_allow_html = True)
st.write("Descubra o tipo do seu trângulo com base no comprimento dos seus lados.")
ladoA = st.number_input("insira o valor do lado A:", min_value= 0,step=1)
ladoB = st.number_input("insira o valor do lado B:", min_value= 0, step=1)
ladoC = st.number_input("insira o valor do lado C:", min_value=0,step=1)
 
if ladoA != ladoB and ladoB != ladoC and ladoA != ladoC:
    st.write("O seu triângulo é Escaleno!")
elif ladoA == ladoB and ladoB == ladoC:
    st.write("O seu triângulo é Equilátero!")
else:
    st.write("O seu triângulo é isóceles!")