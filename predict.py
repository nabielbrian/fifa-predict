import streamlit as st
import pandas as pd
import pickle

with open('model_best.pkl', 'rb') as file_5:
  model = pickle.load(file_5)

def run():
    st.write('# Predict Player Rating')


    # form inference
    with st.form("my_form"):
       st.write("### isi dengan data pemain")
       name = st.text_input("Masukkan nama pemain", placeholder='John Doe')
       age = st.number_input("Masukkan Usia Pemain", min_value = 0, max_value=100, value= 25)
       height = st.number_input("Masukkan Tinggi Pemain", min_value = 0, max_value=300, value= 100)
       weight = st.number_input("Masukkan Berat badan Pemain", min_value = 0, max_value=200, value= 55)
       price = st.number_input("Masukkan Harga Pemain dalam euro", min_value = 0)

       pilihan = ['Low', 'Medium', 'High']
       attackingworkrate = st.selectbox('Attacking Work Rate', pilihan)
       deffensifingworkrate = st.selectbox('Defensive Work Rate', pilihan)

       pace = st.slider('Pace Total', min_value=0, max_value=100)
       shooting = st.slider('Shooting Total', min_value=0, max_value=100)
       passing = st.slider('Passing Total', min_value=0, max_value=100)
       dribilling = st.slider('Dribbiling Total', min_value=0, max_value=100)
       defending = st.slider('Defending Total', min_value=0, max_value=100)
       physical = st.slider('Physical Total', min_value=0, max_value=100)

       submit = st.form_submit_button("Predict")


    #inference dataset
    data_inf = {
                'Name': name,
                'Age': age,
                'Height': height,
                'Weight': weight,
                'Price': price,
                'AttackingWorkRate': attackingworkrate,
                'DefensiveWorkRate': deffensifingworkrate,
                'PaceTotal': pace,
                'ShootingTotal': shooting,
                'PassingTotal': passing,
                'DribblingTotal': dribilling,
                'DefendingTotal': defending,
                'PhysicalityTotal':physical
                }

    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    # predict
    if submit:
        result = model.predict(data_inf)
        st.write(f'# Prediksi Rating {result[0]}')
