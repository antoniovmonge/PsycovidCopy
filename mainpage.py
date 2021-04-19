import app1
import app2
import intro
import archi
import streamlit as st
PAGES = {
    "Introduction": intro,
    "Predictions": app1,
    "Data Analysis": app2,
    " Project Architecture": archi

}


def edu_func(X):

    X['Dem_edu'] = X['Dem_edu'].replace({'Uninformative response': 0, 'None': 1, 'Up to 6 years of school': 2, 'Up to 9 years of school': 3, 'Up to 12 years of school': 4, 'Some College, short continuing education or equivalent': 5, 'College degree, bachelor, master': 6, 'PhD/Doctorate': 7})
    return X[['Dem_edu']]


def edu_mom_func(X):
    X['Dem_edu_mom'] = X['Dem_edu_mom'].replace({'Uninformative response': 0, 'None': 1, 'Up to 6 years of school': 2, 'Up to 9 years of school': 3, 'Up to 12 years of school': 4, 'Some College or equivalent': 5, 'College degree': 6, 'PhD/Doctorate': 7})
    return X[['Dem_edu_mom']]


def edu_risk_group(X):
    X['Dem_riskgroup'] = X['Dem_riskgroup'].replace({'No': 1, 'Not sure': 2, 'Yes': 3})
    return X[['Dem_riskgroup']]


def dem_expat_func(X):
    X['Dem_Expat'] = X['Dem_Expat'].replace({'no': 0, 'yes': 1})
    return X[['Dem_Expat']]


st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()



