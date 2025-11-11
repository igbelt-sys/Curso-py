import streamlit as st

# Função de porcentagem
def porcentagem(cobaia, total):
    if total > 0:
        return (cobaia / total) * 100
    else:
        return 0

# Título
st.title("🧪 Laboratório de Cobaias")

# Inicialização dos totais
total_cobaias = 0
total_ratos = 0
total_sapos = 0
total_coelhos = 0

# Entrada do número de experimentos
n = st.number_input("Digite o número de experimentos:", min_value=0, step=1)

st.header("🔬 Dados dos experimentos")

# Coleta dos dados
for i in range(int(n)):
    st.markdown(f"### Experimento {i+1}")
    quantidade = st.number_input(f"Quantidade de cobaias utilizadas:", min_value=0, step=1, key=f"qtd_{i}")
    tipo = st.selectbox(
        f"Tipo de cobaia:",
        options=["C - Coelho", "R - Rato", "S - Sapo"],
        key=f"tipo_{i}"
    )

    # Atualiza os totais
    if "C" in tipo:
        total_coelhos += quantidade
    elif "R" in tipo:
        total_ratos += quantidade
    elif "S" in tipo:
        total_sapos += quantidade

# Calcula o total geral
total_cobaias = total_coelhos + total_ratos + total_sapos

# Calcula os percentuais
percentual_coelhos = porcentagem(total_coelhos, total_cobaias)
percentual_ratos = porcentagem(total_ratos, total_cobaias)
percentual_sapos = porcentagem(total_sapos, total_cobaias)

# Exibe os resultados
st.header("📊 Resultados")
st.write(f"**Total de cobaias utilizadas:** {total_cobaias}")
st.write(f"🐇 Coelhos: {total_coelhos} ({percentual_coelhos:.2f}%)")
st.write(f"🐀 Ratos: {total_ratos} ({percentual_ratos:.2f}%)")
st.write(f"🐸 Sapos: {total_sapos} ({percentual_sapos:.2f}%)")
