import streamlit as st

# Problema Lanchonete
st.title("🍔 Lanchonete do Guitomw")
st.header("Menu de opções do restaurante")
st.subheader("Opções de lanche")

# HTML da tabela
tabela_html = """
<style>
table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
    align-text:center;
}
th, td {
    border: 1px solid #ddd;
    padding: 10px;
    text-align: center;
}
th {
    background-color: #000000;
    color: white;
    align-text:center;
}
tr:nth-child(even) {
    background-color: #f9f9f9;
}

</style>

<table>
    <thead>
        <tr>
            <th>Código</th>
            <th>Descrição do Item</th>
            <th>Preço (R$)</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>1001</td><td>Frangolino</td><td>18,00</td></tr>
        <tr><td>1002</td><td>VaivcVaivc</td><td>22,00</td></tr>
        <tr><td>1003</td><td>Simplão</td><td>14,00</td></tr>
        <tr><td>1004</td><td>Da sucessagem</td><td>20,00</td></tr>
        <tr><td>1005</td><td>Sucesso</td><td>21,50</td></tr>
        <tr><td>1006</td><td>yoyoyo</td><td>25,00</td></tr>
        <tr><td>1007</td><td>Capcioso</td><td>17,50</td></tr>
        <tr><td>1008</td><td>X Desgraça</td><td>28,00</td></tr>
        <tr><td>1009</td><td>X Miséria</td><td>13,00</td></tr>
        <tr><td>1010</td><td>X Nenê</td><td>15,00</td></tr>
        <tr><td>1011</td><td>X Hashirama</td><td>26,00</td></tr>
    </tbody>
</table>
"""
st.markdown(tabela_html, unsafe_allow_html=True)

opcao = st.selectbox("Selecione o codigo do lanche desejado:", 
                     options = ["1001","1002","1003","1003","1004","1005","1006","1007", "1008","1009","1010"])
codigo  = int(opcao)
quantidade = st.number_input("Digite aquantidade desejada",min_value = 1, step = 1)
# estrutura de controle de seleção
# estrutura de controle de seleção
match codigo:
    case 1001:
        preco = 18.00
        lanche = "Frangolino"
    case 1002:
        preco = 22.00
        lanche = "Bauru de Contrafilé"
    case 1003:
        preco = 14.00
        lanche = "Simplão"
    case 1004:
        preco = 20.00
        lanche = "Da Casa"
    case 1005:
        preco = 21.50
        lanche = "À Moda"
    case 1006:
        preco = 25.00
        lanche = "X Mignon"
    case 1007:
        preco = 17.50
        lanche = "Salada Especial"
    case 1008:
        preco = 28.00
        lanche = "X Desgraça"
    case 1009:
        preco = 13.00
        lanche = "X Miséria"
    case 1010:
        preco = 15.00
        lanche = "X Nenê"
    case 1011:
        preco = 26.00
        lanche = "X Hashirama"
    case _:
        preco = 0.00
# processamento
total = preco*quantidade
st.subheader(f"Total a pagar R$ {total}")

