import sqlite3

conn = sqlite3.connect("smart_task.db")

cursor = conn.cursor()

cursor.execute(
    "DELETE FROM tasks"
)

conn.commit()

conn.close()

print("Database berhasil dikosongkan")