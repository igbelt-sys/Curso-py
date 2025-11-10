import streamlit as st
# problema com experiencias com cobaias
st.title("Laboratorio de cobaias")
# entrada de dados
total_cobaias = 0 
total_ratos = 0
total_sapos = 0 
total_coelhos = 0 
# entrada de dados
n = st.number_input("Digite o numero de experimentos:",min_value= 0,step=1)

# controle
for i in range(n):
    quantidade = (f"Experimento {i+1} - quantidade de cobaias utilizadas")
    tipo = st.selectbox(f"Exeprimento {i+1} - tipo de cobaia C:Coelhp, R:Rato, S:Sapo", options=['C','R','S'])
    
if tipo == 'C':
    total_cobaias += quantidade
elif tipo == 'R':
    total_ratos += quantidade
elif tipo == 'S':
    total_sapos += quantidade
    
if total_cobaias > 0:
    percentual_coelhos = (total_coelhos / total_cobaias)*100
    percentual_ratos = (total_ratos / total_cobaias)*100
    percentual_sapo = (total_sapos / total_cobaias)*100
else:
    percentual_coelhos = percentual_ratos = percentual_sapo = 0
st.subheader("Resultados:")
st.write("Total de cobaias utilizadas: ", total_cobaias)    
st.write("Total de sapos utilizadas: ", total_sapos)   
st.write("Total de ratos utilizadas: ", total_ratos)  
st.write("Total de coelhos utilizadas: ", total_coelhos)   
st.write("Percentual de sapos", percentual_sapo)
st.write("Percentual de ratos", percentual_ratos)
st.write("Percentual de coelhos", percentual_coelhos)
