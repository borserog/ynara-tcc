import streamlit as st
import pandas as pd
import plotly.express as px


def get_pet_ownership_result(df):
    cat_and_dog = ((df["1"] == True) & (df["2"] == True)).sum()
    dog_only = ((df["1"] == True) & (df["2"] == False)).sum()
    cat_only = ((df["1"] == False) & (df["2"] == True)).sum()
    none = ((df["1"] == False) & (df["2"] == False)).sum()

    return pd.DataFrame(
        {
            "Category": ["Cão & Gato", "Apenas Cão", "Apenas Gato", "Nenhum"],
            "Count": [cat_and_dog, dog_only, cat_only, none],
        }
    )


df = pd.read_csv("data/questionario.csv")


st.header("Tópico 1: Distribuição da Posse de Animais de Estimação")
explicacao = """
A visualização da posse de animais de estimação (cães e gatos) por parte dos alunos é fundamental para o tema do conhecimento sobre intoxicação por plantas em pequenos animais.  Essa informação desempenha um papel crítico na compreensão da dinâmica da exposição de animais de estimação a plantas potencialmente tóxicas e na criação de estratégias eficazes de prevenção e conscientização.
"""

st.write(explicacao)
st.write(
    px.pie(
        get_pet_ownership_result(df),
        values="Count",
        names="Category",
    ).update_traces(textinfo="value")
)
