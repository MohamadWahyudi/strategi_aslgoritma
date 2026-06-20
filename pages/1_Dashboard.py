import streamlit as st

from database.task_repository import *

st.title(

    f"Hi {st.session_state['nama']}"

)

st.write(
"""
Smart Task Scheduler Optimizer
menggunakan Greedy Algorithm
dan Dynamic Programming.
"""
)

nama = st.text_input(
    "Nama Tugas"
)

durasi = st.number_input(
    "Durasi (Jam)",
    min_value=1
)

deadline = st.number_input(
    "Deadline (Hari)",
    min_value=1
)

bobot = st.number_input(
    "Bobot",
    min_value=1
)

if st.button(
    "Tambah Tugas"
):

    deadline_efektif = (

        deadline *

        st.session_state[
            "jam_produktif"
        ]

    )

    density = (

        bobot /

        (

            durasi *

            deadline_efektif

        )

    )

    add_task({

        "nama_tugas":
        nama,

        "durasi":
        durasi,

        "deadline_hari":
        deadline,

        "deadline_efektif":
        deadline_efektif,

        "bobot":
        bobot,

        "density":
        density

    })

    st.success(
        "Tugas berhasil ditambahkan"
    )

tasks = get_tasks()

st.subheader(
    "Daftar Tugas"
)

st.dataframe(tasks)

if st.button(
    "Bandingkan Metode"
):
    st.switch_page(
        "pages/2_Comparison.py"
    )