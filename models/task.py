from sqlalchemy import *

metadata = MetaData()

tasks = Table(
    "tasks",
    metadata,

    Column(
        "id",
        Integer,
        primary_key=True
    ),

    Column(
        "nama_tugas",
        String
    ),

    Column(
        "durasi",
        Integer
    ),

    Column(
        "deadline_hari",
        Integer
    ),

    Column(
        "deadline_efektif",
        Integer
    ),

    Column(
        "bobot",
        Integer
    ),

    Column(
        "density",
        Float
    ),

    Column(
        "status",
        String,
        default="pending"
    )
)