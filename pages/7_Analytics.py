import streamlit as st
import plotly.express as px
import pandas as pd

st.title(
    "Analytics"
)

completed = st.session_state.get(
    "completed",
    []
)

score = st.session_state.get(
    "earned_score",
    0
)

st.metric(
    "Total Score",
    score
)

df = pd.DataFrame({

    "Kategori":[

        "Selesai"

    ],

    "Jumlah":[

        len(completed)

    ]

})

fig = px.pie(

    df,

    names="Kategori",

    values="Jumlah"

)

st.plotly_chart(
    fig,
    use_container_width=True
)