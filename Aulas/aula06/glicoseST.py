import streamlit as st
st.title("Classificacao de nivel de glicose no sangue")
st.markdown("""
            <style>
                table{
                width: 600px;
 
                 }
            </style>
      <table>
    <tr>
    <th> Nivel de glicose </th>
    <th> Classificação </th>
    </tr>       
    <td> 0 - 70 </td>
    <td>Hipoglicemia</td>
    </tr> 
    </tr>       
    <td> 71 - 100 </td>
    <td>Normal</td>
    </tr>
    </tr>       
    <td> 101 - 140 </td>
    <td>Pré-diabetes</td>
    </tr>
    </tr>       
    <td> 141 - ou mais </td>
    <td>Hipoglicemia</td>
    </tr>                  
    </table>    
 """,unsafe_allow_html= True)


st.sidebar.title("Insira seu nível de glicose no sangue abaixo:")

nivelGlicose = st.sidebar.number_input("Nível de glicose (mg/dL):", min_value=0, step=1)
if st.button("Classificar"):
    if nivelGlicose <= 70:
        st.error("Hipoglicemia")
    elif nivelGlicose <= 100:
        st.success("Normal")
        st.balloons()
    elif nivelGlicose <= 140:
        st.warning("Pré-diabetes")
    else:
        st.error("Diabetes")