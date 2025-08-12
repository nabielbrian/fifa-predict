import streamlit as st
from PIL import Image
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def run():
    st.write("# FIFA Player Data Analysis")
    gambar = Image.open('mbappe.jpg')
    st.image(gambar)

    #Latar Belakang
    st.write("# Latar Belakang")
    st.write('''Menurut laporan [FIFA 2022](https://publications.fifa.com/en/annual-report-2021/around-fifa/professional-football-2021/), jumlah pemain sepakbola pada tahun 2021 kurang lebih sebanyak 130.000 pemain. 
                Namun, dalam dataset yang digunakan pada kali ini, hanya mencakup 20.000 pemain saja. 
                \n Project kali ini bertujuan untuk memprediksi rating pemain FIFA 2022 sehingga semua pemain sepak bola profesional dapat diketahui ratingnya dan tidak menutup kemungkinan untuk lahirnya talenta/wonderkid baru.
                Project ini akan dibuat menggunakan algoritma Linear Regresison dan akan dievaluasi dengan menggunakan metrics MAE (Mean Absolute Error) dengan target error +- 1.''')
    
    #dataset
    st.write("# Dataset")
    data = pd.read_csv('https://raw.githubusercontent.com/FTDS-learning-materials/phase-1/refs/heads/v2.3/w1/P1W1D1PM%20-%20Machine%20Learning%20Problem%20Framing.csv')
    data.rename(columns={'ValueEUR': 'Price', 'Overall': 'Rating'}, inplace=True)
    #tampilakn dataframe
    st.dataframe(data)

    #Visualisasi
    st.write("# Exploratory Data Analysis")

    st.write('## Player Rating Distribution')
    
    #Visualisasi matplotlib
    fig = plt.figure()
    sns.histplot(data['Rating'], kde=True, bins=30)
    plt.title('Histogram of Rating')
    st.pyplot(fig)

    # visualisasi berdasarkan input
    pilihan = ['PaceTotal', 'ShootingTotal', 'PassingTotal',
                'DribblingTotal', 'DefendingTotal', 'PhysicalityTotal']
    select = st.selectbox('input field untuk visualisasi', pilihan)
    fig = plt.figure(figsize=(10,4))
    sns.histplot(data[select], kde=True, bins=30)
    plt.title('Histogram of {select}')
    st.pyplot(fig)

    #plotly express
    st.write('## Tinggi vs Berat Pemain')
    chart = px.scatter(data, x='Weight', y='Height')
    st.plotly_chart(chart)
    
