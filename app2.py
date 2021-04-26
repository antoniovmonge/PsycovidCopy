import streamlit as st

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px
<<<<<<< HEAD
from google.cloud import storage
from psycovid.params import *
import os
from google.oauth2 import service_account
=======
# from google.cloud import storage
# from psycovid.params import *
>>>>>>> 4e1bcb8342d0e3d64ffa151fd478682c140dede8

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/antoniovmonge/code/antoniovmonge/gcp_keys/psycovid-beta-6cfec8fe1775.json"
credentials = service_account.Credentials.from_service_account_file(
    "/home/antoniovmonge/code/antoniovmonge/gcp_keys/psycovid-beta-6cfec8fe1775.json")
def app():

    st.sidebar.title('Visualisation Selector')

    # Comment/UNCOMMENT THOSE LINES TO ACTIVTE GCP PATH
<<<<<<< HEAD
    client = language.LanguageServiceClient(credentials=credentials)
    
    path = f"gs://{BUCKET_NAME}/{BUCKET_TRAIN_DATA_PATH}"

    @st.cache
    def get_cached_data():
=======
    # client = storage.Client()
    
    # CLOUD PATH
    # path = f"gs://{BUCKET_NAME}/{BUCKET_TRAIN_DATA_PATH}"
    
    # LOCLA PATH
    path = 'raw_data/cleaned_data_040321.csv'
    
    
    @st.cache
    def get_cached_data():
        
>>>>>>> 4e1bcb8342d0e3d64ffa151fd478682c140dede8
        return pd.read_csv(path).drop(columns='Unnamed: 0')
    
    df = get_cached_data()
    # df = pd.read_csv(
    #     'raw_data/cleaned_data_040321.csv').drop(columns='Unnamed: 0')


    #select = st.sidebar.selectbox('Select a State',df['state'])

    st.sidebar.markdown('Personality traits accross countries')
    user_select = st.sidebar.multiselect(
        'Select countries', df['Country'].unique())

    #get the country selected in the selectbox
    select_country = df.loc[df['Country'].isin(user_select)]


    def country_stats():

        # Define variables
        Country_neu = select_country.groupby('Country')['neu'].mean()
        Country_ext = select_country.groupby('Country')['ext'].mean()
        Country_ope = select_country.groupby('Country')['ope'].mean()
        Country_con = select_country.groupby('Country')['con'].mean()
        Country_agr = select_country.groupby('Country')['agr'].mean()

        fig = make_subplots(rows=5, cols=1, shared_xaxes=True)

        fig.append_trace(go.Bar(x=Country_neu.index,
                                y=Country_neu.values), row=1, col=1)
        fig.update_yaxes(range=(0, 5), title_text="Neuroticism", row=1, col=1)

        fig.append_trace(go.Bar(x=Country_ope.index,
                                y=Country_ope.values), row=2, col=1)
        fig.update_yaxes(range=(0, 5), title_text="Openness", row=2, col=1)

        fig.append_trace(go.Bar(x=Country_ext.index,
                                y=Country_ext.values), row=3, col=1)
        fig.update_yaxes(range=(0, 5), title_text="Extraversion", row=3, col=1)

        fig.append_trace(go.Bar(x=Country_agr.index,
                                y=Country_agr.values), row=4, col=1)
        fig.update_yaxes(range=(0, 5), title_text="Agreeableness", row=4, col=1)

        fig.append_trace(go.Bar(x=Country_con.index,
                                y=Country_con.values), row=5, col=1)
        fig.update_yaxes(
            range=(0, 5), title_text="Conscientiousness", row=5, col=1)

        fig.update_layout(height=800, width=600, title_text="Personality traits per country",
                        xaxis_tickangle=90, showlegend=False)

        return fig

    # PLOTLY RADAR CHART
    def country_radar():
        Country_neu = select_country.groupby('Country')['neu'].mean()
        Country_ext = select_country.groupby('Country')['ext'].mean()
        Country_ope = select_country.groupby('Country')['ope'].mean()
        Country_con = select_country.groupby('Country')['con'].mean()
        Country_agr = select_country.groupby('Country')['agr'].mean()
        
        categories = ['Neuroticism', 'Openness', 'Extraversion',
                      'Agreeableness', 'Conscientiousness']
        
        fig = go.Figure()

        fig.add_trace(go.Scatterpolar(
            r=[Country_neu, 5, 2, 2, 3],
            theta=categories,
            fill='toself',
            name='Product A'
        ))
        # fig.add_trace(go.Scatterpolar(
        #     r=[4, 3, 2.5, 1, 2],
        #     theta=categories,
        #     fill='toself',
        #     name='Product B'
        # ))

        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 5]
                )),
            showlegend=False
        )

        # fig.show()
        
        return fig
    
    def stress():

        fig = plt.figure()

        for i in items:
            sns.kdeplot(data=df[df['Country'] == i],
                        x="PSS10_avg", common_norm=False, label=i)
        plt.title('STRESS', fontsize=20)
        plt.xlabel('Perceived Stress', size=15)
        plt.ylabel('Number of people', size=15)
        plt.legend()

        return fig


    def loneliness():

        fig = plt.figure()

        
        for i in user_select:
            items.append(i)
        
            sns.kdeplot(data=df[df['Country'] == i],
                        x="SLON3_avg", common_norm=False, label=i)
            plt.title('LONLINESS', fontsize=20)
            plt.xlabel('Percived Loneliness', size=15)
            plt.ylabel('Percentage of people', size=15)
            plt.legend()

        return fig

    # Create Columns
    # col1, col2 = st.beta_columns(2)


    items = []
    for i in user_select:
        items.append(i)
    if st.sidebar.button('Apply'):
        # print is visible in server output, not in the page
        print('button clicked!')
        st.write(country_radar())
        st.plotly_chart(country_stats(), use_container_width=False)
        col1, col2 = st.beta_columns(2)
        col1.write(stress(), use_column_width=True)
        col2.write(loneliness(), use_column_width=True)
        items = []
    else:
        st.sidebar.write('Press to apply')
        st.title('Please, select countries to compare')
        st.header('...and press Apply')
    
    
