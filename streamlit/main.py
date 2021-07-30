import streamlit as st
import pandas as pd
from PIL import Image
import pickle

from src.support import user_input_features, model

st.write ("""
# Startup valuation estimator - delivering value(ations) since 2021
""")

image_1 = Image.open("../images/cover.png")
st.image(image_1, use_column_width=True)

st.write ("""
### In this app you will find a tool that will allow you to obtain an estimated valuation for a specfic startup based on some key parameters that you will have to provide. In this case, the model parameters you will be required to input are:

- Total funding
- Number of funding rounds
- Founded year
- Days passed between founding date and first financing date
- Country
- Sector
""")

st.write ("""
## In order to begin, please input parameters indicated in the sidebar and then click the Predict button
""")

#we create a sidebar on the left of the page
st.sidebar.header('Startup Input Parameters')

df = user_input_features()

submit = st.button('Predict')

st.subheader('Prediction')

if submit:

    pred = model(df)
    st.write(f"""
    ## {pred}
    """)

    st.text('''''')
    st.text('''''')
    st.text('''''')

    st.text('''Disclaimer: Don't take this figure at face value, use it as a benchmark 
    alongside other valuation methods. Please visit the following link for guidance on 
    startup valuation: 
    https://corporatefinanceinstitute.com/resources/knowledge/valuation/startup-valuation-methods/''')

