from datetime import datetime
from datetime import timedelta


def generate_schedule(
        tasks,
        jam_mulai,
        jam_produktif
):

    result = []

    hari = 1

    current = datetime.combine(
        datetime.today(),
        jam_mulai
    )

    batas_harian = jam_produktif

    jam_terpakai = 0

    for task in tasks:

        durasi = task["durasi"]

        mulai_task = current

        durasi_sisa = durasi

        while durasi_sisa > 0:

            sisa_hari = (
                batas_harian -
                jam_terpakai
            )

            if sisa_hari <= 0:

                hari += 1

                jam_terpakai = 0

                current = datetime.combine(
                    datetime.today()
                    +
                    timedelta(
                        days=hari - 1
                    ),
                    jam_mulai
                )

                sisa_hari = batas_harian

            jam_dikerjakan = min(
                durasi_sisa,
                sisa_hari
            )

            current += timedelta(
                hours=jam_dikerjakan
            )

            jam_terpakai += (
                jam_dikerjakan
            )

            durasi_sisa -= (
                jam_dikerjakan
            )

        selesai_task = current

        result.append({

            "Hari": hari,

            "Tugas":
            task["nama_tugas"],

            "Mulai":
            mulai_task,

            "Selesai":
            selesai_task,

            "Durasi":
            durasi,

            "Bobot":
            task["bobot"],
            
            "Deadline":
            task["deadline_efektif"]

        })

    return result