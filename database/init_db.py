import sqlite3

conn = sqlite3.connect(
    "smart_task.db"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    nama_tugas TEXT,

    durasi INTEGER,

    deadline_hari INTEGER,

    deadline_efektif INTEGER,

    bobot INTEGER,

    density REAL,

    status TEXT

)
""")

conn.commit()

conn.close()

print("Database berhasil dibuat")