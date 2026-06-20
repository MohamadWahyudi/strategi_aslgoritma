import streamlit as st
import pandas as pd

from database.task_repository import *

from algorithms.greedy import *
from algorithms.dynamic_programming import *

from algorithms.scheduler import *

# =====================================
# LOAD DATA
# =====================================

tasks = get_tasks()

metode = st.session_state.get(
    "metode",
    "Greedy"
)

# =====================================
# PILIH ALGORITMA
# =====================================

if metode == "Greedy":

    result = greedy(tasks)

else:

    result = dynamic_programming(tasks)

# =====================================
# GENERATE SCHEDULE
# =====================================

schedule = generate_schedule(

    result["tasks"],

    st.session_state["jam_mulai"],

    st.session_state["jam_produktif"]

)

# =====================================
# TITLE
# =====================================

st.title(
    "Jadwal Pengerjaan"
)

st.success(

    f"""
Metode :

{metode}
"""
)

# =====================================
# TABEL JADWAL
# =====================================

df = pd.DataFrame(schedule)

st.dataframe(
    df,
    use_container_width=True
)

# =====================================
# CARD JADWAL
# =====================================

st.divider()

for item in schedule:

    st.info(

        f"""
Tugas :
{item['Tugas']}

Hari :
{item['Hari']}

Mulai :
{item['Mulai']}

Selesai :
{item['Selesai']}
"""
    )

# =====================================
# BUTTON
# =====================================

if st.button(
    "Mulai Working Mode"
):

    st.switch_page(
        "pages/5_Working.py"
    )