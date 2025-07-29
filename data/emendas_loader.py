import requests 
import zipfile
import io 
import pandas as pd
import streamlit as st
from unidecode import unidecode

URL = "https://dadosabertos-download.cgu.gov.br/PortalDaTransparencia/saida/emendas-parlamentares/EmendasParlamentares.zip"
ARQUIVO = "EmendasParlamentares.csv"

def normalizar_colunas(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = [unidecode(c)
                  .strip()
                  .lower()
                  .replace(" ", "_") 
                  for c in df.columns]
    return df

def limpar_texto(df: pd.DataFrame) -> pd.DataFrame:
    for col in df.select_dtypes(include="object"):
        df[col] = df[col].str.strip()
    return  df

def converter_valores_monetários(df: pd.DataFrame, colunas) -> pd.DataFrame:
    for col in colunas:
        if col in df.columns:
            df[col] = pd.to_numeric(
                df[col].str.replace(",", "."),
                errors="coerce"
            )
    return df

@st.cache_data(show_spinner="Baixando dados " \
"de emendas parlamentares...")
def baixar_arquivos_zip_bytes(url: str) -> bytes:
    return requests.get(url).content


def carregar_csv_emendas(zip_bytes: bytes,
                         nome_arquivo: str) -> pd.DataFrame:
    with zipfile.ZipFile(io.BytesIO(zip_bytes)) as z:
        with z.open(nome_arquivo) as f:
            df = pd.read_csv(f,
                             sep=";",
                             encoding="latin1",
                             dtype=str)
    df = normalizar_colunas(df)
    df = limpar_texto(df)
    df = converter_valores_monetários(
        df,
        ["valor_empenhado",
         "valor_liquidado",
         "valor_pago"]
    )
    return df 

@st.cache_data(show_spinner="Carregando " \
"e processando a base principal")
def carregar_emendas() -> pd.DataFrame:
    zip_bytes = baixar_arquivos_zip_bytes(URL)
    return carregar_csv_emendas(zip_bytes, ARQUIVO)