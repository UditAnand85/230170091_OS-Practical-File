processes = [
    {"pid": 1, "arrival": 0, "burst": 5},
    {"pid": 2, "arrival": 1, "burst": 3},
    {"pid": 3, "arrival": 2, "burst": 8},
    {"pid": 4, "arrival": 3, "burst": 6},
]

def fcfs(procs):
    time = 0
    gantt = []
    wt, tat = {}, {}

    for p in sorted(procs, key=lambda x: x["arrival"]):
        if time < p["arrival"]:
            time = p["arrival"]

        start = time
        finish = time + p["burst"]
        gantt.append((p["pid"], start, finish))

        tat[p["pid"]] = finish - p["arrival"]
        wt[p["pid"]] = tat[p["pid"]] - p["burst"]

        time = finish

    return gantt, wt, tat


def sjf(procs):
    time = 0
    gantt = []
    done = set()
    wt, tat = {}, {}

    while len(done) < len(procs):
        ready = [p for p in procs if p["arrival"] <= time and p["pid"] not in done]
        if not ready:
            time += 1
            continue

        p = min(ready, key=lambda x: x["burst"])
        start = time
        finish = time + p["burst"]
        gantt.append((p["pid"], start, finish))

        tat[p["pid"]] = finish - p["arrival"]
        wt[p["pid"]] = tat[p["pid"]] - p["burst"]

        time = finish
        done.add(p["pid"])

    return gantt, wt, tat


def round_robin(procs, q):
    time = 0
    rem = {p["pid"]: p["burst"] for p in procs}
    gantt = []
    wt, tat = {}, {}
    ready = []
    i = 0
    n = len(procs)

    while len(tat) < n:
        while i < n and procs[i]["arrival"] <= time:
            ready.append(procs[i]["pid"])
            i += 1

        if not ready:
            time += 1
            continue

        pid = ready.pop(0)
        use = min(q, rem[pid])
        start = time
        finish = time + use
        gantt.append((pid, start, finish))

        rem[pid] -= use
        time = finish

        while i < n and procs[i]["arrival"] <= time:
            ready.append(procs[i]["pid"])
            i += 1

        if rem[pid] > 0:
            ready.append(pid)
        else:
            p = next(x for x in procs if x["pid"] == pid)
            tat[pid] = time - p["arrival"]
            wt[pid] = tat[pid] - p["burst"]

    return gantt, wt, tat


def show(name, gantt, wt, tat):
    print(f"\n=== {name} ===")
    for pid, s, e in gantt:
        print(f"{s} [{pid}] {e}")

    print("WT:", wt)
    print("TAT:", tat)

g1, w1, t1 = fcfs(processes)
g2, w2, t2 = sjf(processes)
g3, w3, t3 = round_robin(processes, q=4)

show("FCFS", g1, w1, t1)
show("SJF", g2, w2, t2)
show("Round Robin", g3, w3, t3)
