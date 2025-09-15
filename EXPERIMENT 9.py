from itertools import permutations

# Distance matrix between cities
# Example for 4 cities (0, 1, 2, 3)
distance = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

def traveling_salesman(dist):
    n = len(dist)
    cities = list(range(n))
    min_path = None
    min_cost = float('inf')

    for perm in permutations(cities[1:]):  # fix the first city as 0 to avoid duplicate cycles
        current_cost = 0
        k = 0  # start from city 0
        for j in perm:
            current_cost += dist[k][j]
            k = j
        current_cost += dist[k][0]  # return to starting city

        if current_cost < min_cost:
            min_cost = current_cost
            min_path = (0,) + perm + (0,)

    return min_path, min_cost

path, cost = traveling_salesman(distance)
print(f"Optimal path: {path}")
print(f"Minimum cost: {cost}")
