
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
    st.sidebar.text('Soon to be Data Scientists')
    st.sidebar.text("Le Wagon's Data Science Bootcamp")
    st.sidebar.text("Berlin Batch 532")
    st.sidebar.markdown("Shruthi Lakshmanan Parthasarathy")
    st.sidebar.markdown("Antonio Vilchez Monge")
    st.sidebar.markdown("Wojciech Gutkiewicz")
    st.sidebar.markdown("Veronica Delgado Benito")


    st.title("    PSYCOVID     ")
    st.header('Welcome to our Data Science Project! :notebook:')
    st.image('brain.jpg', width=500)
    st.markdown('                  ')
    st.markdown('                  ')

    st.header("It all started with a survey and a question...:thinking_face:")
    st.markdown("> Global survey to map how COVID19 affects humans across countries")
    st.markdown("> What is the impact of COVID19 on our psyche and behaviour?")
    st.markdown('                  ')
    st.markdown('                  ')

    st.header("We want to use ML to predict human behaviour :fire:")
    st.image('pexels.jpg', width=500)

