import sys

def tsp(mask, pos, n, dist, dp):
    # Base case: if all cities have been visited
    if mask == (1 << n) - 1:
        return dist[pos][0] # Return to the starting city (0)

    # If this state has already been computed, return it
    if dp[mask][pos] != -1:
        return dp[mask][pos]

    ans = sys.maxsize

    # Try to go to an unvisited city
    for city in range(n):
        if (mask & (1 << city)) == 0:
            # City is unvisited
            new_ans = dist[pos][city] + tsp(mask | (1 << city), city, n, dist, dp)
            ans = min(ans, new_ans)

    dp[mask][pos] = ans
    return ans


if __name__ == "__main__":
    n = 4 # Number of cities
    
    # Distance matrix
    # dist[i][j] represents distance from city i to city j
    dist = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    # dp memoization table initialized with -1
    # 2^n states for the mask, and n positions
    dp = [[-1 for _ in range(n)] for _ in range(1 << n)]

    # Start from city 0, so mask is 1 (0th bit set), and position is 0
    min_cost = tsp(1, 0, n, dist, dp)
    
    print("The minimum cost for the Traveling Salesperson is:", min_cost)
