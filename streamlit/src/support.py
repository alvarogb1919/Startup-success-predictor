import streamlit as st
import pandas as pd
import pickle
import math

# Dictionaries to convert countries and sector inserted by user to rank encoding

countries = {'USA': {'rank': 1},
 'GBR': {'rank': 2},
 'CAN': {'rank': 3},
 'FRA': {'rank': 4},
 'IND': {'rank': 5},
 'DEU': {'rank': 6},
 'ISR': {'rank': 7},
 'CHN': {'rank': 8},
 'ESP': {'rank': 9},
 'IRL': {'rank': 10},
 'SWE': {'rank': 11},
 'AUS': {'rank': 12},
 'SGP': {'rank': 13},
 'ITA': {'rank': 14},
 'NLD': {'rank': 15},
 'CHL': {'rank': 16},
 'BRA': {'rank': 17},
 'RUS': {'rank': 18},
 'JPN': {'rank': 19},
 'FIN': {'rank': 20},
 'Other': {'rank': 21}}

markets = {'Software': {'rank': 1},
 'Biotechnology': {'rank': 2},
 'Mobile': {'rank': 3},
 'Enterprise Software': {'rank': 4},
 'E-Commerce': {'rank': 5},
 'Curated Web': {'rank': 6},
 'Health Care': {'rank': 7},
 'Hardware + Software': {'rank': 8},
 'Advertising': {'rank': 9},
 'Games': {'rank': 10},
 'Clean Technology': {'rank': 11},
 'Health and Wellness': {'rank': 12},
 'Social Media': {'rank': 13},
 'Education': {'rank': 14},
 'Analytics': {'rank': 15},
 'Finance': {'rank': 16},
 'Semiconductors': {'rank': 17},
 'Security': {'rank': 18},
 'Manufacturing': {'rank': 19},
 'Web Hosting': {'rank': 20},
 'Other': {'rank': 21}}



def user_input_features():
    """
    Function to save the info that the user give in the app
    Args: 
        non receive parameters
    Returns:
        A dataframe with the characteristcs given by the user
    """
    total_funding = st.sidebar.text_input('Total funding', 0) # the sidebar.slider magic function receive the max, min and default value in out sidebar
    funding_rounds = st.sidebar.slider('Funding rounds', 1, 20, 5)
    founded_year = st.sidebar.slider('Founding year', 1900, 2021, 2000)
    delta_founded_vs_firstfunding = st.sidebar.text_input('Days from founded date until first funding', 0)
    country = st.sidebar.selectbox('Country of origin', ('USA', 'GBR', 'CAN', 'FRA', 'IND', 'DEU', 'ISR', 'CHN', 'ESP', 'IRL', 'SWE', 'AUS', 'SGP', 'ITA', 'NLD', 'CHL', 'BRA', 'RUS', 'JPN', 'FIN','Other'))
    country_rank = countries[country]['rank']
    sector = st.sidebar.selectbox('Sector', ( 'Software', 'Biotechnology', 'Mobile', 'Enterprise Software', 'E-Commerce', 'Curated Web', 'Health Care', 'Hardware + Software', 'Advertising', 'Games', 'Clean Technology', 'Health and Wellness', 'Social Media', 'Education', 'Analytics', 'Finance', 'Semiconductors', 'Security', 'Manufacturing', 'Web Hosting','Other'))
    sector_rank = markets[sector]['rank']
    data = {'total_funding': int(total_funding),
            'funding_rounds': float(funding_rounds),
            'founded_year': float(founded_year),
            'delta_founded_vs_firstfunding': float(delta_founded_vs_firstfunding),
            'country_ranking': country_rank,
            'market_ranking': sector_rank}
    
    return pd.DataFrame(data, index=[0])

def model(df):
    """
    Function imports my already trained model and returns prediction based on user parameters
    Args: 
        df: dataframe with the users parameters
    Returns:
        pred_valuation: estimated valuation for startup
        pred_digit: estimated number of digits for valuation
    """
    model = pickle.load(open('Startup_model.pkl','rb'))
    
    prediction = model.predict(df)
    
    pred_digit = int(prediction)
    pred_valuation = 10**prediction
    clean_valuation = round(pred_valuation[0])
    cleaner_valuation = "{:0,}".format(clean_valuation)

    return f"Estimated valuation: € {cleaner_valuation}"