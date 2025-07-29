import streamlit as st
from data.emendas_loader import carregar_emendas
from components.kpis import mostrar_kpis
from components.charts import grafico_top_parlamentares
from utils.filtros import filtrar_emendas  # opcional

st.set_page_config(layout="centered")
st.title("📊 Dashboard de Emendas Parlamentares")

df = carregar_emendas()

ufs = ["Todos"] + sorted(df['uf'].dropna().unique())
tipos = ["Todos"] + sorted(df['tipo_de_emenda'].dropna().unique())

col1, col2 = st.columns(2)
with col1:
    uf = st.selectbox("UF", ufs)
with col2:
    tipo = st.selectbox("Tipo de Emenda", tipos)



nome_parlamentar = st.text_input("Nome do parlamentar (opcional)").strip().lower()

# Filtro (via função)
df_filtrado = filtrar_emendas(df, uf, tipo, nome_parlamentar)

# Exibir
mostrar_kpis(df_filtrado)
grafico_top_parlamentares(df_filtrado)

st.subheader("📄 Registros Detalhados")
st.dataframe(df_filtrado)
