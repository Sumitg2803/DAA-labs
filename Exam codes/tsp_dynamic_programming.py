# TSP using Dynamic Programming (Bitmasking)

def tsp(mask, pos):
    # If all cities are visited, return cost to go back to start
    if mask == (1 << n) - 1:
        return graph[pos][0]

    if dp[mask][pos] != -1:
        return dp[mask][pos]

    ans = float('inf')

    # Try all cities
    for city in range(n):
        if (mask & (1 << city)) == 0:
            new_cost = graph[pos][city] + tsp(mask | (1 << city), city)
            ans = min(ans, new_cost)

    dp[mask][pos] = ans
    return ans


# Function to print path
def print_path():
    mask = 1
    pos = 0
    path = [0]

    while True:
        next_city = -1
        min_cost = float('inf')

        for city in range(n):
            if (mask & (1 << city)) == 0:
                cost = graph[pos][city] + tsp(mask | (1 << city), city)
                if cost < min_cost:
                    min_cost = cost
                    next_city = city

        if next_city == -1:
            break

        path.append(next_city)
        mask |= (1 << next_city)
        pos = next_city

    path.append(0)  # return to start
    print("Path:", path)


# Main program
n = int(input("Enter number of cities: "))

print("Enter cost matrix:")
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dp = [[-1] * n for _ in range(1 << n)]

min_cost = tsp(1, 0)

print("Minimum cost:", min_cost)
print_path()