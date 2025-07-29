import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

"""    if df.empty or "valor_pago" not in df.columns:
        return pd.Series(dtype=float)"""


def is_empty(df: pd.DataFrame, col: str) -> bool:
    return True if df.empty or col not in df.columns else False

def preparar_ranking(df: pd.DataFrame, n=100):
    if is_empty(df, "valor_pago"):
        return pd.Series(dtype=float)
    
    df["valor_pago"] = pd.to_numeric(
        df["valor_pago"], errors="coerce")
    ranking = (
        df.groupby("nome_do_autor_da_emenda")
            ["valor_pago"]
        .sum()
        .sort_values(ascending=False)
        .head(n)
    )

    return ranking

def desenhar_barra_horizontal(ranking: pd.Series,
                              altura_por_linha=0.3):
    if ranking.empty:
        st.info("Nenhum dado siponível " \
        "para o gráfico")
        return

    fig, ax = plt.subplots(
        figsize=(10, len(ranking) * 
                 altura_por_linha))
    ranking.plot(kind="barh", ax=ax)
    ax.set_title("🏛️Top parlamentares por valor pago")
    ax.set_xlabel("Valor Pago (R$)")
    ax.set_ylabel("")
    ax.invert_yaxis()   
    plt.tight_layout()

    st.markdown("<div style='max-height: 600px;" \
    " overflow-y: auto;'>", 
    unsafe_allow_html=True)
    st.pyplot(fig)

    st.markdown("</div>", 
                unsafe_allow_html=True)    

def grafico_top_parlamentares(df: pd.DataFrame,
                              n=100):
    ranking = preparar_ranking(df, n)
    desenhar_barra_horizontal(ranking)