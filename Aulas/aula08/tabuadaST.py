import streamlit as st

# Configuração da página
st.set_page_config(page_title="Tabuada")

# Título
TITULO = "🧮 Tabuada"
st.title(TITULO)

# Entrada
numero = st.text_input("Deseja a tabuada de qual número:")

# Verificação e processamento
if numero == "":
    st.warning("Digite algum valor para gerar a tabuada.")
else:
    try:
        n = int(numero)
        st.success(f"Tabuada do {n}")

        # Exibir a tabuada
        for i in range(1, 11):
            st.write(f"{n} x {i} = {n * i}")

    except ValueError:
        st.error("Digite apenas números inteiros.")
