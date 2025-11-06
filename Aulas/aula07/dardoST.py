import streamlit as st
st.title("🎯Simulação de lançamento de dardos🎯")
"""Simulação de lançamentos de dardos. O objetivo do aplicativo é mostrar o dardo com a maior distância """
# entrada de dados
st.header("Inserir distâncias dos dardos lançados pelo jogador")

coluna1, coluna2, coluna3 = st.columns(3)
with coluna1:
    d1 = st.number_input ("Insira a distância do 1° dardo em metros",min_value=0)
with coluna2:
    d2 = st.number_input ("Insira a distância do 2° dardo em metros",min_value=0)
with coluna3:
    d3 = st.number_input ("Insira a distância do 3° dardo em metros",min_value=0)


# processamento de dados
st.button("Calcular")
if d2 < d1 > d3:
    st.success (f"A maior distancia foi do dardo 1° dardo com {d1} metros!")
elif d1 < d2 >d3:
    st.success (f"A maior distancia foi do dardo 2° dardo {d2} metros!")
elif d1<d3>d2:
    st.success(f"A maior distancia foi do dardo 3° dardo {d3} metros!")
else:
    st.warning(f"A um empate entre as distâncias dos dardos!")