def greedy(tasks):

    sorted_tasks = sorted(

        tasks,

        key=lambda x:
        x["density"],

        reverse=True

    )

    current = 0

    profit = 0

    selected = []

    for task in sorted_tasks:

        finish = (

            current +

            task["durasi"]

        )

        if (

            finish <= 24

            and

            finish <=
            task[
                "deadline_efektif"
            ]

        ):

            selected.append(
                task
            )

            profit += (
                task["bobot"]
            )

            current = finish

    return {

        "profit":
        profit,

        "tasks":
        selected

    }