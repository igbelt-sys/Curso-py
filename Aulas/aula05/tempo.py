import streamlit as st

TITULO = "Calculadora de duração de tempo"
st.set_page_config(page_title=TITULO)
st.title(TITULO)

# ENTRADA DE DADOS
tempo = st.number_input("Digite o tempo em segundos:", min_value = 0, step = 1,help = "insira o tempo total em segundos")

# processamento
tempo = int(tempo)  # garante que seja inteiro
horas = tempo // 3600
minutos = (tempo % 3600) // 60
segundos = tempo % 60  # simplificado

# saída de dados
st.write(f"O tempo de {tempo} segundos corresponde a: {horas} horas, {minutos} minutos e {segundos} segundos.")
