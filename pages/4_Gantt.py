import streamlit as st

import pandas as pd

import plotly.express as px

from database.task_repository import *

from algorithms.greedy import *

from algorithms.scheduler import *

tasks = get_tasks()

result = greedy(tasks)

schedule = generate_schedule(

    result["tasks"],

    st.session_state[
        "jam_mulai"
    ],

    st.session_state[
        "jam_produktif"
    ]

)

df = pd.DataFrame(
    schedule
)

st.title(
    "Gantt Chart"
)

fig = px.timeline(

    df,

    x_start="Mulai",

    x_end="Selesai",

    y="Tugas",

    color="Hari"

)

fig.update_yaxes(
    autorange="reversed"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

if st.button(
    "Mulai Pengerjaan"
):
    st.switch_page(
        "pages/5_Working.py"
    )