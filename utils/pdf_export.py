from fpdf import FPDF

def export_pdf(schedule):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font(
        "Arial",
        size=12
    )

    pdf.cell(

        200,

        10,

        txt=
        "Smart Task Schedule",

        ln=True

    )

    for task in schedule:

        pdf.cell(

            200,

            10,

            txt=

            f"{task['Tugas']} | "
            f"{task['Mulai']} - "
            f"{task['Selesai']}",

            ln=True

        )

    pdf.output(
        "schedule.pdf"
    )