# Priority Scheduling (Non-Preemptive)

class Process:
    def __init__(self, pid, at, bt, priority):
        self.pid = pid
        self.at = at
        self.bt = bt
        self.priority = priority
        self.ct = 0
        self.tat = 0
        self.wt = 0


def priority_scheduling(processes):
    n = len(processes)
    time = 0
    completed = [False] * n
    completed_count = 0

    while completed_count < n:
        idx = -1
        highest_priority = float("inf")  

        for i in range(n):
            if not completed[i] and processes[i].at <= time:
                if processes[i].priority < highest_priority:
                    highest_priority = processes[i].priority
                    idx = i
                elif processes[i].priority == highest_priority:
                    if processes[i].at < processes[idx].at:
                        idx = i

        if idx != -1:
            if time < processes[idx].at:
                time = processes[idx].at

            time += processes[idx].bt
            processes[idx].ct = time
            completed[idx] = True
            completed_count += 1
        else:
            time += 1

    # Calculate TAT and WT
    for i in range(n):
        processes[i].tat = processes[i].ct - processes[i].at
        processes[i].wt = processes[i].tat - processes[i].bt


def main():
    n = int(input("Enter number of processes: "))
    processes = []

    for i in range(n):
        print(f"\nProcess P{i+1}:")
        at = int(input("Enter Arrival Time: "))
        bt = int(input("Enter Burst Time: "))
        priority = int(input("Enter Priority (Lower number = Higher priority): "))
        processes.append(Process(f"P{i+1}", at, bt, priority))

    priority_scheduling(processes)

    print("\nPID\tAT\tBT\tPriority\tCT\tTAT\tWT")
    for p in processes:
        print(f"{p.pid}\t{p.at}\t{p.bt}\t{p.priority}\t\t{p.ct}\t{p.tat}\t{p.wt}")

    avg_tat = sum(p.tat for p in processes) / n
    avg_wt = sum(p.wt for p in processes) / n

    print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
    print(f"Average Waiting Time: {avg_wt:.2f}")


if __name__ == "__main__":
    main()
