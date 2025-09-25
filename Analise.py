import pandas as pd
import streamlit as st

st.title("🎬 Análise de Filmes")


filmes = {
    "Títulos": ["Vingadores", "Toy Story", "Titanic", "Superbad"],
    "Gênero": ["Ação", "Animação", "Drama", "Comédia"],
    "Ano": [2012, 1995, 1997, 2007],
    "Avaliação": [9, 8, 9, 7]
}

uploaded_file = st.file_uploader("📂 Escolha um arquivo CSV", type="csv")


if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.DataFrame(filmes)

st.subheader("📊 Dados dos Filmes")
st.dataframe(df)

st.subheader("📋 Estatísticas")
st.write(df.describe(include="all"))

st.subheader("🎥 Lista de Filmes")
st.table(df[["Títulos", "Gênero", "Ano", "Avaliação"]])

st.subheader("📈 Avaliação dos Filmes")
st.bar_chart(df.set_index("Títulos")["Avaliação"])
