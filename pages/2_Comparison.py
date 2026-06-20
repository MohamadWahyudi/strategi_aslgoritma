import streamlit as st
import pandas as pd
import plotly.express as px

from database.task_repository import *

from algorithms.greedy import *
from algorithms.dynamic_programming import *

# =====================================
# LOAD DATA
# =====================================

tasks = get_tasks()

greedy_result = greedy(tasks)

dp_result = dynamic_programming(tasks)

# =====================================
# TITLE
# =====================================

st.title(
    "📊 Perbandingan Metode"
)

# =====================================
# PROFIT
# =====================================

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Profit Greedy",
        greedy_result["profit"]
    )

with col2:

    st.metric(
        "Profit Dynamic Programming",
        dp_result["profit"]
    )

# =====================================
# REKOMENDASI SISTEM
# =====================================

st.divider()

if dp_result["profit"] > greedy_result["profit"]:

    st.success(
        f"""
Rekomendasi Sistem :

Dynamic Programming

Profit :
{dp_result['profit']}
"""
    )

    rekomendasi = "Dynamic Programming"

else:

    st.success(
        f"""
Rekomendasi Sistem :

Greedy

Profit :
{greedy_result['profit']}
"""
    )

    rekomendasi = "Greedy"

# =====================================
# DAFTAR TUGAS GREEDY
# =====================================

st.divider()

st.subheader(
    "🟢 Urutan Tugas Greedy"
)

for i, task in enumerate(
    greedy_result["tasks"],
    start=1
):

    st.success(
        f"{i}. {task['nama_tugas']}"
    )

# =====================================
# DAFTAR TUGAS DP
# =====================================

st.subheader(
    "🔵 Urutan Tugas Dynamic Programming"
)

for i, task in enumerate(
    dp_result["tasks"],
    start=1
):

    st.info(
        f"{i}. {task['nama_tugas']}"
    )

# =====================================
# GRAFIK
# =====================================

df = pd.DataFrame({

    "Metode":[

        "Greedy",

        "Dynamic Programming"

    ],

    "Profit":[

        greedy_result["profit"],

        dp_result["profit"]

    ]

})

fig = px.bar(

    df,

    x="Metode",

    y="Profit",

    text="Profit"

)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================
# PILIH METODE
# =====================================

st.divider()

st.subheader(
    "Pilih Metode Pengerjaan"
)

metode = st.radio(

    "",

    [

        "Greedy",

        "Dynamic Programming"

    ],

    index=0
    if rekomendasi == "Greedy"
    else 1

)

# =====================================
# SIMPAN METODE
# =====================================

if st.button(
    "🚀 Mulai Pengerjaan"
):

    st.session_state[
        "metode"
    ] = metode

    st.switch_page(
        "pages/5_Working.py"
    )

# =====================================
# LIHAT JADWAL
# =====================================

if st.button(
    "📅 Lihat Jadwal"
):

    st.session_state[
        "metode"
    ] = metode

    st.switch_page(
        "pages/3_Schedule.py"
    )