import streamlit as st
import pandas as pd

st.title("📊 Encuesta 'Lenguaje de programación favorito'")

opciones = ["Python", "JavaScript", "Java", "C#", "C++"]

if "votos" not in st.session_state:
    st.session_state.votos = {op: 0 for op in opciones}

eleccion = st.radio("Elige un lenguaje: ", opciones)

if st.button("Votar"):
    st.session_state.votos[eleccion] += 1
    st.success(f"¡Votaste por {eleccion}!")

df = pd.DataFrame.from_dict(st.session_state.votos, orient="index", columns=["Votos"])

total = df["Votos"].sum()

if total > 0:
    df["%"] = (df["Votos"] / total * 100).round(1)
else:
    df["%"] = 0.0

st.dataframe(df)
st.bar_chart(df["Votos"])
