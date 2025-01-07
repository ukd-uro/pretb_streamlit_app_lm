# Import libraries
import time
import requests
import streamlit as st

# Initialize variables
ip = '13.60.71.91'
url = 'http://' + ip + '/api/t5_small/v1/predict'
headers = {
    'Content-Type': 'application/json'
    }

# Load images
col1, col2 = st.columns(2, gap='large', vertical_alignment='center')

with col1:
    st.image('ukd_logo.jpg', width=250)

with col2:
    st.image('uoz_logo.png', width=150)

# The title
st.title('PreTb_T5')

# The header
st.header('LLM für das prätherapeutische Tumorboard')

text = st.text_area('Patientendaten eingeben', '', height=200)

data = {'text': [text]}

button_predict = st.button('Prädiktion')

if button_predict:
    with st.spinner('Berechnung läuft...'):
        start = time.time()
        response = requests.post(url, headers=headers, json=data)
        end = time.time()
        prediction_time = end - start
        output = response.json()
        st.text('PreTb_T5 empfiehlt folgendes Procedere:')
        st.markdown(output['prediction'])
        st.text('Berechnungszeit: ' + str(prediction_time) + ' s')
