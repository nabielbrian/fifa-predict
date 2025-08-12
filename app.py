import streamlit as st
import eda,predict

with st.sidebar:
    st.write("# Page Navigation")

    ##toggle pilih halaman
    page = st.selectbox("Pilih Halaman", ("EDA", "Predict Rating"))

    #test
    st.write(f"Halaman yang dituju {page}")

    st.write("## About")
    st.write("Page ini berisikan hasil analisis data terhadap pemain di fifa 2024 dan juga prediksi rating pemain berdasarkan atribut yang dimiliki")


if page == "EDA":
    eda.run()

else:
    predict.run()