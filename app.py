import streamlit as st

st.set_page_config(
    page_title=
    "Smart Task Scheduler",
    layout="wide"
)

st.title(
    "Smart Task Scheduler Optimizer"
)

nama = st.text_input(
    "Nama"
)

jam_produktif = st.number_input(
    "Jam Produktif Harian",
    value=8
)

jam_mulai = st.time_input(
    "Jam Mulai Produktif"
)

if st.button(
    "Masuk Dashboard"
):

    st.session_state[
        "nama"
    ] = nama

    st.session_state[
        "jam_produktif"
    ] = jam_produktif

    st.session_state[
        "jam_mulai"
    ] = jam_mulai

    st.switch_page(
        "pages/1_Dashboard.py"
    )