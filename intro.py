
def app():



    import streamlit as st

    import numpy as np
    import pandas as pd

    import matplotlib.pyplot as plt
    import numpy as np
    import seaborn as sns

    from plotly.subplots import make_subplots
    import plotly.graph_objects as go

    st.sidebar.title('Who are we?')

    st.sidebar.markdown(
        "[Shruthi Lakshmanan Parthasarathy](https://www.linkedin.com/in/shruthilp/)")
    st.sidebar.markdown(
        "[Antonio Vilchez Monge](https://www.linkedin.com/in/antonio-v-monge/)")
    st.sidebar.markdown(
        "[Wojciech Gutkiewicz](https://www.linkedin.com/in/gutkiewicz/)")
    st.sidebar.markdown(
        "[Veronica Delgado Benito](https://www.linkedin.com/in/veronica-delgadobenito/)")

    st.sidebar.text('Soon to be Data Scientists')
    st.sidebar.text("Le Wagon's Data Science Bootcamp")
    st.sidebar.text("Berlin Batch 532")

    st.markdown('''
                # PSYCOVID - Data Science Project
                ### Study based on on psychological impact and behavioural consequences of the COVID-19 outbreak
                #####
                ''')
    col1, col2, col3 = st.beta_columns(3)
    
    # LEFT COLUMN
    
    col1.markdown('''
                  ### Data Analysis
                  Interactive Data Analysis of Personality and emotional repercusion of COVID-19 by countries
                  ''')
    col1.image(['images/white-space-small.png','images/brain-beta-2.png', 'images/white-space-small.png',
                'images/virus-1.png'], use_column_width=False, width=75)
    # col1.image(['images/white-space-small.png','images/emotions-1.png'], width=75)
    col1.markdown('''
                  ####
                  Analisys of demographic background variables, 
                  perceived stress (PSS-10), availability of social provisions (SPS-10), trust in various authorities, 
                  trust in governmental measures to contain the virus (OECD trust), personality traits (BFF-15), information behaviours, 
                  agreement with the level of government intervention, and compliance with preventive measures, 
                  along with a rich pool of exploratory variables and written experiences.
                  ''')
    col1.image(['images/white-space-small.png', 'images/map-1.png'], width=150)
    
    # COLUMN 2
    col2.markdown('''
                  > ### Predictions
                  Interactive **Machine Learning** that quantifies you personality based on the big 5 personality traits using the bff_personality test
                  ''')
    col2.image(['images/white-space-small.png',
                'images/radar-chart.png'], use_column_width=False, width=140)
    col2.markdown(
        '> and predict stress and loneliness levels based on your personaliy and some demographical factors')
    col2.image('images/speedometers-good.png',
               use_column_width=True, width=400)
    

    # COLUMN 3 
    col3.markdown('''
                  > ### Data Source
                  Data Collection Technology: **Survey** [COVIDiSTRESS Global Survey](https://osf.io/z39us/)
                    
                  > Period of time Data Collection: between 30th March and 30th May 2020
                    
                  > N = 173,426
                    
                  > Factor Types: 
                  - geographic location language 
                  - age of participant
                  - gouvernamental responses to the Coronavirus pandemic
                  
                  > Measurements: psychological measurement
                  - anxiety-related behavior trait
                  - Stress
                  - response to Isolation
                  - loneliness measurement
                  - Emotional Distress
                  ''')
    
    
