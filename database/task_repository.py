import sqlite3

DB = "smart_task.db"


def add_task(task):

    conn = sqlite3.connect(DB)

    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO tasks(

        nama_tugas,
        durasi,
        deadline_hari,
        deadline_efektif,
        bobot,
        density,
        status

    )

    VALUES(?,?,?,?,?,?,?)

    """,

    (

        task["nama_tugas"],
        task["durasi"],
        task["deadline_hari"],
        task["deadline_efektif"],
        task["bobot"],
        task["density"],
        "pending"

    ))

    conn.commit()

    conn.close()


def get_tasks():

    conn = sqlite3.connect(DB)

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM tasks"
    )

    data = cursor.fetchall()

    conn.close()

    return [
        dict(row)
        for row in data
    ]