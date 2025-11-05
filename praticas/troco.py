import streamlit as st
TITULO = "Calculadora de troco"
st.title(TITULO)
st.set_page_config(page_title= TITULO)
# entrada de dados
produto = st.number_input("Digie o valor do produto:", min_value = 0.0, step = 0.01)
quantidade = st.number_input("Digite o a quantidade do produto:", min_value = 1, step=1)
DinheiroRecebido = st.number_input("Digite o a quantidade de dinheiro recebido:", min_value = 0.0, step=0.1)
# processamento
valorTotal = produto * quantidade
troco = DinheiroRecebido - valorTotal
# saida de dados
st.markdown("<strong><h2 style = 'text-align: center'> Resultado </h2></strong>",unsafe_allow_html= True)
st.write(f"Prço unitario do produto: {produto:.2f}")
st.write(f"Quantidade do produto: {quantidade}")
st.write(f"Dinheiro recebido: {DinheiroRecebido:.2f}")
st.write(f"TROCO: {troco:.2f}")