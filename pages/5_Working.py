import streamlit as st

from datetime import datetime
from datetime import timedelta

from database.task_repository import *

from algorithms.greedy import *
from algorithms.dynamic_programming import *
from algorithms.scheduler import *

from streamlit_autorefresh import st_autorefresh

import plotly.graph_objects as go


# ======================================
# AUTO REFRESH
# ======================================

st_autorefresh(
    interval=1000,
    key="timer_refresh"
)

st.title(
    "⏱ Smart Task Working Mode"
)

# ======================================
# LOAD DATA
# ======================================

tasks = get_tasks()

metode = st.session_state["metode"]

if metode == "Greedy":

    result = greedy(tasks)

else:

    result = dynamic_programming(tasks)

schedule = generate_schedule(

    result["tasks"],

    st.session_state["jam_mulai"],

    st.session_state["jam_produktif"]

)

# ======================================
# SESSION
# ======================================

st.session_state["schedule"] = schedule

if "current_task" not in st.session_state:
    st.session_state["current_task"] = 0

if "completed" not in st.session_state:
    st.session_state["completed"] = []

if "earned_score" not in st.session_state:
    st.session_state["earned_score"] = 0

if "running" not in st.session_state:
    st.session_state["running"] = False

# ======================================
# FINISH CHECK
# ======================================

if (
    st.session_state["current_task"]
    >=
    len(st.session_state["schedule"])
):

    st.session_state[
        "final_profit"
    ] = st.session_state[
        "earned_score"
    ]

    st.session_state[
        "selected_method"
    ] = metode

    st.success(
        "🎉 Semua tugas selesai"
    )

    st.switch_page(
        "pages/6_Finish.py"
    )

# ======================================
# HEADER
# ======================================

st.success(
    f"Metode Aktif : {metode}"
)

st.subheader(
    "Urutan Tugas"
)

for i,t in enumerate(
    result["tasks"],
    start=1
):

    st.write(
        f"{i}. {t['nama_tugas']}"
    )

# ======================================
# PROGRESS
# ======================================

total_task = len(
    st.session_state["schedule"]
)

selesai = len(
    st.session_state["completed"]
)

persen = int(
    selesai
    /
    total_task
    *
    100
)

st.progress(
    persen
)

st.write(
    f"Progress : {persen}%"
)

# ======================================
# PRODUCTIVITY SCORE
# ======================================

max_profit = result["profit"]

score = 0

if max_profit > 0:

    score = round(

        st.session_state[
            "earned_score"
        ]

        /

        max_profit

        *

        100,

        2

    )

st.metric(
    "🏆 Productivity Score",
    f"{score}%"
)

# ======================================
# TASK AKTIF
# ======================================

task = st.session_state[
    "schedule"
][
    st.session_state[
        "current_task"
    ]
]

st.subheader(
    task["Tugas"]
)

st.info(
f"""
Hari : {task['Hari']}

Mulai : {task['Mulai']}

Selesai : {task['Selesai']}
"""
)

# ======================================
# DEADLINE CHECK
# ======================================

awal_hari = datetime.combine(
    datetime.today(),
    st.session_state[
        "jam_mulai"
    ]
)

selesai_jam = (

    task["Selesai"]

    -

    awal_hari

).total_seconds() / 3600

deadline = task["Deadline"]

if selesai_jam > deadline:

    st.error(
        f"""
Deadline Terlewati

Deadline :
{deadline} jam

Selesai :
{round(selesai_jam,2)} jam
"""
    )

else:

    st.success(
        f"""
Deadline Aman

Deadline :
{deadline} jam

Selesai :
{round(selesai_jam,2)} jam
"""
    )

# ======================================
# REMINDER
# ======================================

now = datetime.now()

jadwal_mulai = task["Mulai"]

if not st.session_state["running"]:

    if now >= jadwal_mulai:

        st.warning(
            "⚠ Saatnya mulai tugas"
        )

    if now > jadwal_mulai + timedelta(minutes=15):

        st.error(
            "⚠ Terlambat memulai tugas"
        )

        delay = now - jadwal_mulai

        for t in st.session_state["schedule"]:

            t["Mulai"] += delay

            t["Selesai"] += delay

# ======================================
# MULAI TUGAS
# ======================================

if not st.session_state["running"]:

    if st.button(
        "▶ Mulai Tugas"
    ):

        st.session_state[
            "start_time"
        ] = datetime.now()

        st.session_state[
            "running"
        ] = True

        st.rerun()

# ======================================
# TIMER
# ======================================

if st.session_state["running"]:

    durasi = (
        task["Durasi"]
        *
        3600
    )

    elapsed = (

        datetime.now()

        -

        st.session_state[
            "start_time"
        ]

    ).seconds

    remaining = max(
        0,
        durasi - elapsed
    )

    jam = remaining // 3600

    menit = (
        remaining % 3600
    ) // 60

    detik = (
        remaining % 60
    )

    persen_waktu = (
        remaining
        /
        durasi
    ) * 100

    fig = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=persen_waktu,

            number={
                "suffix":"%"
            },

            title={
                "text":
                f"{jam:02}:{menit:02}:{detik:02}"
            },

            gauge={
                "axis":{
                    "range":[0,100]
                }
            }

        )

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ALERT

    if remaining <= 600:
        st.warning(
            "⚠ 10 menit lagi"
        )

    if remaining <= 300:
        st.warning(
            "⚠ 5 menit lagi"
        )

    if remaining <= 180:
        st.error(
            "⚠ 3 menit lagi"
        )

    # ==================================
    # SELESAI TUGAS
    # ==================================

    if st.button(
        "✅ Selesai Tugas"
    ):

        st.session_state[
            "completed"
        ].append(
            task["Tugas"]
        )

        st.session_state[
            "earned_score"
        ] += task["Bobot"]

        actual_finish = datetime.now()

        for i in range(

            st.session_state[
                "current_task"
            ] + 1,

            len(
                st.session_state[
                    "schedule"
                ]
            )

        ):

            next_task = st.session_state[
                "schedule"
            ][i]

            durasi_task = next_task[
                "Durasi"
            ]

            next_task[
                "Mulai"
            ] = actual_finish

            next_task[
                "Selesai"
            ] = (

                actual_finish

                +

                timedelta(
                    hours=
                    durasi_task
                )

            )

            actual_finish = next_task[
                "Selesai"
            ]

        st.session_state[
            "current_task"
        ] += 1

        st.session_state[
            "running"
        ] = False

        st.rerun()

    # ==================================
    # WAKTU HABIS
    # ==================================

    if remaining == 0:

        st.error(
            "⛔ Waktu Habis"
        )

        tambahan = st.number_input(
            "Tambah waktu (menit)",
            min_value=0,
            value=10
        )

        if st.button(
            "Tambah Waktu"
        ):

            st.session_state[
                "start_time"
            ] = datetime.now() - timedelta(

                seconds=
                durasi
                -
                (
                    tambahan
                    *
                    60
                )

            )

            st.rerun()

# ======================================
# NEXT TASK
# ======================================

if (

    st.session_state[
        "current_task"
    ]

    + 1

    <

    len(
        st.session_state[
            "schedule"
        ]
    )

):

    next_task = st.session_state[
        "schedule"
    ][

        st.session_state[
            "current_task"
        ]

        + 1

    ]

    st.info(
f"""
📌 Tugas Berikutnya

{next_task['Tugas']}

Mulai :
{next_task['Mulai']}
"""
    )