from datetime import timedelta

def reschedule(
        schedule,
        current_index,
        actual_finish
):

    planned_finish = schedule[
        current_index
    ]["Selesai"]

    delay = (
        actual_finish -
        planned_finish
    )

    if delay.total_seconds() <= 0:
        return schedule

    for i in range(
        current_index + 1,
        len(schedule)
    ):

        schedule[i]["Mulai"] += delay

        schedule[i]["Selesai"] += delay

    return schedule