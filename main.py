
import streamlit as st
st.set_page_config(
    page_title="SC Sports Scores Weekly",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.header('SC Sports Scores Weekly')
st.divider()

st.subheader('SC Sports Scores Weekly is a public website database that provides statewide scores from all sports played in the state of South Carolina.')
st.subheader('This website is updated weekly.')
