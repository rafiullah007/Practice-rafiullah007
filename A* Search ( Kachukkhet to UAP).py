import heapq

graph = {
    "Kachukhet Bazar": [("Shewrapara metro station", 3), ("Mohakhali bus stand", 4), ("Jahangir gate", 7)],
    "Shewrapara metro station": [("Bijoy sarani", 6)],
    "Mirpur 10 metro station": [("Khamarbari", 7)],
    "Mohakhali bus stand": [("Jahangir gate", 1), ("Bijoy sarani", 2)],  
    "Jahangir gate": [("Bijoy sarani", 2)],
    "Bijoy sarani": [("UAP", 3)],
    "Khamarbari": [("UAP", 1)],
    "UAP": []
}

heuristics = {
    "Kachukhet Bazar": 1,
    "Shewrapara metro station": 1,
    "Mirpur 10 metro station": 3,
    "Mohakhali bus stand": 1,
    "Jahangir gate": 2,
    "Bijoy sarani": 1,
    "Khamarbari": 3,
    "UAP": 0
}
#MD.Rafiullah Al Naim
def a_star_search(start, goal):
    frontier = []
    heapq.heappush(frontier, (heuristics[start], 0, start, [start]))  

    visited = set()

    while frontier:
        f, g, current, path = heapq.heappop(frontier)

        if current == goal:
            return path, g

        if current in visited:
            continue
        visited.add(current)
#rafiullah007
        for neighbor, cost in graph[current]:
            g_new = g + cost
            f_new = g_new + heuristics[neighbor]
            heapq.heappush(frontier, (f_new, g_new, neighbor, path + [neighbor]))

    return None, float("inf")


start_node = "Kachukhet Bazar"
goal_node = "UAP"
path, cost = a_star_search(start_node, goal_node)

print("Optimal Path:", " -> ".join(path))
print("Total Cost:", cost)
