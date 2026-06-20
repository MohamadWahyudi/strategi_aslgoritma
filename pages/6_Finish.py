import streamlit as st

from fpdf import FPDF

st.title(
    "🎉 Hasil Pengerjaan"
)

metode = st.session_state.get(
    "selected_method",
    "-"
)

profit = st.session_state.get(
    "final_profit",
    0
)

completed = st.session_state.get(
    "completed",
    []
)

total_task = len(
    completed
)

st.success(
    "Seluruh tugas berhasil diselesaikan"
)

# ==================================
# RINGKASAN
# ==================================

st.subheader(
    "Ringkasan"
)

st.metric(
    "Metode",
    metode
)

st.metric(
    "Profit",
    profit
)

st.metric(
    "Jumlah Tugas",
    total_task
)

# ==================================
# PRODUCTIVITY SCORE
# ==================================

score = 100

st.metric(
    "Productivity Score",
    f"{score}%"
)

# ==================================
# LIST TUGAS
# ==================================

st.subheader(
    "Tugas Yang Diselesaikan"
)

for task in completed:

    st.success(
        task
    )

# ==================================
# PDF
# ==================================

if st.button(
    "Export PDF"
):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font(
        "Arial",
        size=12
    )

    pdf.cell(
        200,
        10,
        txt="SMART TASK SCHEDULER REPORT",
        ln=True
    )

    pdf.cell(
        200,
        10,
        txt=f"Metode : {metode}",
        ln=True
    )

    pdf.cell(
        200,
        10,
        txt=f"Profit : {profit}",
        ln=True
    )

    pdf.cell(
        200,
        10,
        txt=f"Jumlah Tugas : {total_task}",
        ln=True
    )

    pdf.cell(
        200,
        10,
        txt="",
        ln=True
    )

    pdf.cell(
        200,
        10,
        txt="Daftar Tugas",
        ln=True
    )

    for task in completed:

        pdf.cell(
            200,
            10,
            txt=f"- {task}",
            ln=True
        )

    pdf.output(
        "laporan_jadwal.pdf"
    )

    with open(
        "laporan_jadwal.pdf",
        "rb"
    ) as file:

        st.download_button(

            "Download PDF",

            file,

            file_name=
            "laporan_jadwal.pdf"

        )

# ==================================
# RESTART
# ==================================

if st.button(
    "Mulai Lagi"
):

    keys = [

        "schedule",

        "current_task",

        "completed",

        "earned_score",

        "running",

        "final_profit"

    ]

    for key in keys:

        if key in st.session_state:

            del st.session_state[key]

    st.switch_page(
        "Home.py"
    )