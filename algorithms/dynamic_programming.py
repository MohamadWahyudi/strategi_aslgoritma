def dynamic_programming(tasks):

    capacity = 24

    n = len(tasks)

    M = [

        [0]*(capacity+1)

        for _ in range(n+1)

    ]

    tasks = sorted(

        tasks,

        key=lambda x:
        x["deadline_efektif"]

    )

    # =========================
    # FILL TABLE
    # =========================

    for i in range(1,n+1):

        task = tasks[i-1]

        for t in range(1,capacity+1):

            if (

                task["durasi"] <= t

                and

                t <= task["deadline_efektif"]

            ):

                without_task = M[i-1][t]

                with_task = (

                    task["bobot"]

                    +

                    M[i-1][

                        t -
                        task["durasi"]

                    ]

                )

                M[i][t] = max(

                    without_task,

                    with_task

                )

            else:

                M[i][t] = M[i-1][t]

    # =========================
    # BACKTRACK
    # =========================

    selected_tasks = []

    t = capacity

    for i in range(n,0,-1):

        if (

            M[i][t]

            !=

            M[i-1][t]

        ):

            selected_tasks.append(

                tasks[i-1]

            )

            t -= tasks[i-1][
                "durasi"
            ]

            if t < 0:

                t = 0

    selected_tasks.reverse()

    # =========================
    # RETURN
    # =========================

    return {

        "profit":
        M[n][capacity],

        "tasks":
        selected_tasks

    }