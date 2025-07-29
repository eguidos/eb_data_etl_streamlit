import streamlit as st
import pandas as pd 

def mostrar_kpis(df: pd.DataFrame):
    df["valor_empenhado"] = pd.to_numeric(
        df["valor_empenhado"], 
        errors="coerce"
    )
    df["valor_liquidado"] = pd.to_numeric(
        df["valor_liquidado"], 
        errors="coerce"
    )
    df["valor_pago"] = pd.to_numeric(
        df["valor_pago"], 
        errors="coerce"
    )

    col1, = st.columns(1)
    col1.metric("💰 Valor Empenhado", f"R$ {df['valor_empenhado'].sum():,.2f}")

    st.markdown("<br>", unsafe_allow_html=True)

    col2, = st.columns(1)
    col2.metric("💵 Valor Liquidado", f"R$ {df['valor_liquidado'].sum():,.2f}")

    st.markdown("<br>", unsafe_allow_html=True)

    col3, = st.columns(1)
    col3.metric("✅ Valor Pago", f"R$ {df['valor_pago'].sum():,.2f}")

