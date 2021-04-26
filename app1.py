import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import joblib
import plotly.graph_objects as go
import plotly.express as px
from math import pi

def app():
    ############
    # CSS CODE #
    ############
    
    st.markdown(
        '<style>.css-2y0inq{top: -30px;}</style>', unsafe_allow_html=True)
    st.markdown(
        '<style>.css-1aumxhk{width: 30rem; background-image: linear-gradient(rgb(240, 240, 240), rgb(240, 240, 240));}</style>', unsafe_allow_html=True)
    st.markdown(
        '<style>.css-hi6a2p {padding: 1rem;}</style>', unsafe_allow_html=True)
    # st.markdown('<style>.st-bf{padding:60px}</style>', unsafe_allow_html=True)
    # st.markdown('<style>.css-145kmo2 {font:20px;}</style>', unsafe_allow_html=True)
    # st.markdown('<style>.css-1aumxhk{font: 4.25rem;font-weight: 600;}</style>', unsafe_allow_html=True)
    # st.markdown('<style>.css-hi6a2p{width: 838px}</style>', unsafe_allow_html=True)
    
    ##################
    # HEADER COLUMNS #
    ##################
    
    col1, col2 = st.beta_columns(2)
    
    col1.header('YOUR BIG 5 PERSONALITY SCORES')
    # st.markdown('''
    #             # YOUR BIG 5 PERSONALITY SCORES
    #             ''')
    col2.header('IN A PANDEMIC OUTBREAK...')
    col2.markdown('''
                  ### the prediction about your Stress and Loneliness levels is:
                  ###
                  ''')
    ###########
    # SIDEBAR #
    ###########
    st.sidebar.title('I see myself as a person who...')

    
    kwargs = {}

    bff15_options = ['Strongly disagree', 'Disagree',
                     'Slightly disagree', 'Slightly agree', 'Agree', 'Strongly agree']

    bff15_labels = ['... is often concerned',
                    '... easily gets nervous',
                    '... is good at staying cool in stressful situations',
                    '... likes to chat',
                    '... is extrovert and sociable',
                    '... is socially reserved',
                    '... gets a lot of new ideas',
                    '... appreciates arts and aesthetics',
                    '... has a vivid imagination and can think of things that do not yet exist',
                    '... is sometimes impolite to others',
                    '... is forgiving towards others',
                    '... is kind and considerate towards almost everyone',
                    '... is thorough and meticulous',
                    '... is lazy',
                    '... is effective when I do something']

    for x in range(1, 16):
        st.sidebar.subheader(bff15_labels[x-1])
        kwargs['BFF_15_'+str(x)] = st.sidebar.select_slider('', [1, 2, 3, 4, 5, 6],
                                                            value=4,
                                                            format_func=lambda o: bff15_options[o-1],
                                                            key='BFF_15_'+str(x))

    st.sidebar.subheader("Choose age:")
    kwargs['Dem_age'] = st.sidebar.slider("", 18, 70, value=42)
    st.sidebar.subheader("Pick a gender")
    kwargs['Dem_gender'] = st.sidebar.selectbox(
        '',  options=['Male', 'Other/would rather not say', 'Female'])
    st.sidebar.subheader("Pick your education")
    kwargs['Dem_edu'] = st.sidebar.selectbox("", options=['Uninformative response', 'None', 'Up to 6 years of school',
                                                          'Up to 9 years of school', 'Up to 12 years of school', 'Some College, short continuing education or equivalent',
                                                          'College degree, bachelor, master', 'PhD/Doctorate'], index=6)
    st.sidebar.subheader("Pick your mother's education")
    kwargs['Dem_edu_mom'] = st.sidebar.selectbox("", options=['Uninformative response', 'None', 'Up to 6 years of school',
                                                              'Up to 9 years of school', 'Up to 12 years of school', 'Some College or equivalent', 'College degree', 'PhD/Doctorate'], index=5)
    st.sidebar.subheader("Pick your employment status")
    kwargs['Dem_employment'] = st.sidebar.selectbox("", options=[
                                                    'Full time employed', 'Not employed', 'Part time employed', 'Retired', 'Self-employed'])
    st.sidebar.subheader("Are you living abroad?")
    kwargs['Dem_Expat'] = st.sidebar.selectbox(
        "", options=['yes', 'no'], index=1)
    st.sidebar.subheader("Choose your marital status")
    kwargs['Dem_maritalstatus'] = st.sidebar.selectbox("", options=[
                                                       'Single', 'Married/cohabiting', 'Other or would rather not say', 'Divorced/widowed', 'Uninformative response'])
    st.sidebar.subheader("Are you in a risk group?")
    kwargs['Dem_riskgroup'] = st.sidebar.selectbox(
        "", options=['Yes', 'No', 'Not sure'], index=1)
    st.sidebar.subheader("Are you currently isolated?")
    kwargs['Dem_isolation'] = st.sidebar.selectbox("", options=['Life carries on with minor changes',
                                                                'Isolated', 'Life carries on as usual',
                                                                'Isolated in medical facility of similar location', '1'])

    # FUNTION FOR RADAR CHART BIG 5

    def make_radar_chart():

        # markers = prediction.values.tolist()[0]
        categories = ['neu', 'ext', 'ope', 'agr', 'con']
        N = len(categories)

        # We are going to plot the first line of the data frame.
        # But we need to repeat the first value to close the circular graph:
        values = prediction.values.tolist()[0]
        values += values[:1]
        # values

        # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
        angles = [n / float(N) * 2 * pi for n in range(N)]
        angles += angles[:1]

        # Initialise the spider plot
        fig = plt.figure(figsize=(3, 3), dpi=100)
        
        ax = plt.subplot(111, polar=True)

        # Draw one axe per variable + add labels
        plt.xticks(angles[:-1], categories, color='grey', size=10)

        # Draw ylabels
        ax.set_rlabel_position(0)
        plt.yticks([2, 3, 4, 5], ["2", "3", "4", "5"], color="grey", size=7)
        plt.ylim(0, 6)

        # Plot data
        ax.plot(angles, values, linewidth=1, linestyle='solid')

        # Fill area
        ax.fill(angles, values, 'b', alpha=0.1)

        return fig

    # GENERATE THE VALUES FOR PREDICTIONS

    values = pd.DataFrame([kwargs.values()])

    # KNN Model

    knn = joblib.load('models/knn.joblib')
    pred = knn.predict(
        values.iloc[:, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]])
    prediction = pd.DataFrame(pred)
    prediction.columns = ['neu', 'ext', 'ope', 'agr', 'con']

    # Create Columns
    col1, col2, col3, col4 = st.beta_columns(4)

    # col1.header('Left')
    radar = make_radar_chart()
    col1.write(radar, use_column_width=True)
    # col1.write(prediction, use_column_width=True)

    # col2.write(str(prediction['ext'][0].round(2)))
    legend = f"""
                Extraversion {str(prediction['ext'][0].round(2))}

                Neuroticism {str(prediction['neu'][0].round(2))}

                Openness to experience {str(prediction['ope'][0].round(2))}

                Agreeableness {str(prediction['agr'][0].round(2))}

                Conscientiousness {str(prediction['con'][0].round(2))}
                """
    col2.write("""
            
            """)
    col2.write(legend)

    # STRESS LEVEL
    # Here I add the functions for predicting stress

    def edu_func(X):
        X['Dem_edu'] = X['Dem_edu'].replace({'Uninformative response': 0, 'None': 1, 'Up to 6 years of school': 2, 'Up to 9 years of school': 3,
                                             'Up to 12 years of school': 4, 'Some College, short continuing education or equivalent': 5, 'College degree, bachelor, master': 6, 'PhD/Doctorate': 7})
        return X[['Dem_edu']]

    def edu_mom_func(X):
        X['Dem_edu_mom'] = X['Dem_edu_mom'].replace({'Uninformative response': 0, 'None': 1, 'Up to 6 years of school': 2, 'Up to 9 years of school': 3,
                                                     'Up to 12 years of school': 4, 'Some College or equivalent': 5, 'College degree': 6, 'PhD/Doctorate': 7})
        return X[['Dem_edu_mom']]

    def edu_risk_group(X):
        X['Dem_riskgroup'] = X['Dem_riskgroup'].replace(
            {'No': 1, 'Not sure': 2, 'Yes': 3})
        return X[['Dem_riskgroup']]

    def dem_expat_func(X):
        X['Dem_Expat'] = X['Dem_Expat'].replace({'no': 0, 'yes': 1})
        return X[['Dem_Expat']]

    model_stress = joblib.load('models/model_stress.joblib')
    values = pd.DataFrame([kwargs.values()], columns=['BFF_15_1', 'BFF_15_2', 'BFF_15_3', 'BFF_15_4', 'BFF_15_5', 'BFF_15_6', 'BFF_15_7', 'BFF_15_8', 'BFF_15_9', 'BFF_15_10', 'BFF_15_11',
                                                      'BFF_15_12', 'BFF_15_13', 'BFF_15_14', 'BFF_15_15', 'Dem_age', 'Dem_gender', 'Dem_edu', 'Dem_edu_mom', 'Dem_employment', 'Dem_Expat', 'Dem_maritalstatus', 'Dem_riskgroup', 'Dem_isolation'])
    pred_stress = model_stress.predict(values)

    # st.markdown("""
    #             ## IN A PANDEMIC OUTBREAK...

    #             ### The prediction about your Stress and Loneliness levels:
    #             """)


    # Bar for Stress

    def make_speed_stress():
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=pred_stress[0],
            title={'text': "Stress Level"},
            domain={'x': [0, 1], 'y': [0, 1]},
            gauge={'axis': {'range': [None, 5]},
                   'bar': {'color': "rgb(255, 56, 116)"}}
        ))
        fig.update_layout(
            autosize=True,
            width=200,
            height=200,
            margin=dict(
                l=0,
                r=0,
                b=50,
                t=50,
                pad=2
            ))
        # ax = fig.add_subplot(111, polar=True)

        return fig

    stress = make_speed_stress()

    # LONELINESS LEVEL

    model_loneliness = joblib.load('models/model_loneliness.joblib')
    values = pd.DataFrame([kwargs.values()], columns=['BFF_15_1', 'BFF_15_2', 'BFF_15_3', 'BFF_15_4', 'BFF_15_5', 'BFF_15_6', 'BFF_15_7', 'BFF_15_8', 'BFF_15_9', 'BFF_15_10', 'BFF_15_11',
                                                      'BFF_15_12', 'BFF_15_13', 'BFF_15_14', 'BFF_15_15', 'Dem_age', 'Dem_gender', 'Dem_edu', 'Dem_edu_mom', 'Dem_employment', 'Dem_Expat', 'Dem_maritalstatus', 'Dem_riskgroup', 'Dem_isolation'])
    pred_loneli = model_loneliness.predict(values)

    # st.write(f'YOUR LONELINESS LEVEL PREDICTION IS: {pred_loneli[0]}')

    def make_speed_loneliness():
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=pred_loneli[0],
            title={'text': "Loneliness Level"},
            domain={'x': [0, 1], 'y': [0, 1]},
            gauge={'axis': {'range': [None, 5]},
                   'bar': {'color': "rgb(190, 202, 237)"}}
        ))
        fig.update_layout(
            autosize=True,
            width=200,
            height=200,
            margin=dict(
                l=0,
                r=0,
                b=50,
                t=50,
                pad=2
            ))
        return fig

    loneliness = make_speed_loneliness()

    # col3, col4 = st.beta_columns(2)

    col3.write(stress, use_column_width=True)
    col4.write(loneliness, use_column_width=True)
