import streamlit as st

def grafico(d1, d2, d3):
    # O gráfico precisa receber um dicionário no formato certo
    dados = {
        "1° Dardo": [d1],
        "2° Dardo": [d2],
        "3° Dardo": [d3]
    }

    st.subheader("📊 Gráfico das distâncias dos dardos")
    st.bar_chart(dados, use_container_width=True)  # Você pode trocar por st.area_chart(dados)

def app():
    st.header("Simulação de Lançamento de Dardos")

    col1, col2, col3 = st.columns(3)
    with col1:
        d1 = st.number_input("Distância do 1° dardo (m)", min_value=0.0)
    with col2:
        d2 = st.number_input("Distância do 2° dardo (m)", min_value=0.0)
    with col3:
        d3 = st.number_input("Distância do 3° dardo (m)", min_value=0.0)

    if st.button("Calcular"):
        if d1 == d2 == d3:
            st.info("⚠️ Houve empate entre os dardos!")
        else:
            if d1 > d2 and d1 > d3:
                st.success(f"🏆 1° lugar: 1° dardo — {d1} m")
                if d2 > d3:
                    st.warning(f"🥈 2° lugar: 2° dardo — {d2} m")
                    st.error(f"🥉 3° lugar: 3° dardo — {d3} m")
                else:
                    st.warning(f"🥈 2° lugar: 3° dardo — {d3} m")
                    st.error(f"🥉 3° lugar: 2° dardo — {d2} m")

            elif d2 > d1 and d2 > d3:
                st.success(f"🏆 1° lugar: 2° dardo — {d2} m")
                if d1 > d3:
                    st.warning(f"🥈 2° lugar: 1° dardo — {d1} m")
                    st.error(f"🥉 3° lugar: 3° dardo — {d3} m")
                else:
                    st.warning(f"🥈 2° lugar: 3° dardo — {d3} m")
                    st.error(f"🥉 3° lugar: 1° dardo — {d1} m")

            elif d3 > d1 and d3 > d2:
                st.success(f"🏆 1° lugar: 3° dardo — {d3} m")
                if d1 > d2:
                    st.warning(f"🥈 2° lugar: 1° dardo — {d1} m")
                    st.error(f"🥉 3° lugar: 2° dardo — {d2} m")
                else:
                    st.warning(f"🥈 2° lugar: 2° dardo — {d2} m")
                    st.error(f"🥉 3° lugar: 1° dardo — {d1} m")

        # Chama o gráfico (sempre aparece)
        grafico(d1, d2, d3)
 