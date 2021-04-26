import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px

# from google.cloud import storage
# from psycovid.params import *
# import os
# from google.oauth2 import service_account

# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/antoniovmonge/code/antoniovmonge/gcp_keys/psycovid-beta-6cfec8fe1775.json"
# credentials = service_account.Credentials.from_service_account_file(
#     "/home/antoniovmonge/code/antoniovmonge/gcp_keys/psycovid-beta-6cfec8fe1775.json")
def app():

    # st.title('Visualisation Selector')

    # Comment/UNCOMMENT THOSE LINES TO ACTIVTE GCP PATH
    # client = language.LanguageServiceClient(credentials=credentials)
    
    # path = f"gs://{BUCKET_NAME}/{BUCKET_TRAIN_DATA_PATH}"
    path = 'raw_data/cleaned_data_040321.csv'

    @st.cache
    def get_cached_data():
        return pd.read_csv(path).drop(columns='Unnamed: 0')
    
    df = get_cached_data()
    # df = pd.read_csv(
    #     'raw_data/cleaned_data_040321.csv').drop(columns='Unnamed: 0')


    # PLOTLY RADAR CHART
    def country_radar():
        categories = ['Neuroticism', 'Openness', 'Extraversion',
                      'Agreeableness', 'Conscientiousness', 'Neuroticism']


        fig = go.Figure()

        for i in user_select:
            fig.add_trace(go.Scatterpolar(
                r=[df[df.Country == i].groupby('Country')['neu'].mean().to_list()[0],
                   df[df.Country == i].groupby('Country')['ope'].mean().to_list()[0],
                   df[df.Country == i].groupby('Country')['ext'].mean().to_list()[0],
                   df[df.Country == i].groupby('Country')['agr'].mean().to_list()[0],
                   df[df.Country == i].groupby('Country')['con'].mean().to_list()[0],
                   df[df.Country == i].groupby('Country')['neu'].mean().to_list()[0]],
                theta=categories,
                fill='toself',
                name=i))

        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 5]
                )),
            showlegend=True
        )

        # fig.show()
        return fig
    
    def stress():

        fig = plt.figure()

        for i in items:
            sns.kdeplot(data=df[df['Country'] == i],
                        x="PSS10_avg", bw_adjust=1, common_norm=False, label=i)
        plt.title('STRESS')
        plt.xlabel('Perceived Stress')
        plt.ylabel('Distribution')
        plt.yticks([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9],
                   ['10 %', '20 %', '30 %', '40 %', '50 %', '60 %', '70 %', '80 %', '90 %'])
        plt.legend()

        return fig


    def loneliness():
        fig = plt.figure()

        
        for i in user_select:
            items.append(i)
            # sns.set_style("talk")
            sns.kdeplot(data=df[df['Country'] == i],
                        x="SLON3_avg", bw_adjust=1.5, common_norm=False, label=i)
            plt.title('LONLINESS')
            plt.xlabel('Percived Loneliness')
            plt.ylabel('Distribution')
            plt.yticks([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7],
                       ['10 %', '20 %', '30 %', '40 %', '50 %', '60 %', '70 %'])
            plt.legend()

        return fig

    # Create Columns
    # col1, col2 = st.beta_columns(2)

    st.markdown('## Personality traits accross countries')
    user_select = st.multiselect(
        'Select countries', df['Country'].unique())

    #get the country selected in the selectbox
    sns.set_style('white')
    # select_country = df.loc[df['Country'].isin(user_select)]
    items = []
    for i in user_select:
        items.append(i)
    if st.button('Apply'):
        # print is visible in server output, not in the page
        print('button clicked!')
        
        col1, col2, col3 = st.beta_columns((1.5,1,1))
        col1.plotly_chart(country_radar(), use_container_width=True)
        # col1.plotly_chart(country_stats(), use_container_width=True)
        
        col2.pyplot(stress())
        col2.pyplot(loneliness())
        items = []
    else:
        st.write('Press to apply')
