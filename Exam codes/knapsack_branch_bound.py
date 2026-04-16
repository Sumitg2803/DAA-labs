# Node structure
class Node:
    def __init__(self, level, profit, weight, bound):
        self.level = level
        self.profit = profit
        self.weight = weight
        self.bound = bound


# Function to calculate upper bound
def bound(node, n, capacity, weights, profits):
    if node.weight >= capacity:
        return 0

    profit_bound = node.profit
    j = node.level + 1
    total_weight = node.weight

    # Take items while possible
    while j < n and total_weight + weights[j] <= capacity:
        total_weight += weights[j]
        profit_bound += profits[j]
        j += 1

    # Take fraction of next item
    if j < n:
        profit_bound += (capacity - total_weight) * (profits[j] / weights[j])

    return profit_bound


# Branch and Bound Knapsack
def knapsack_bb(weights, profits, capacity):
    n = len(weights)

    # Sort items by profit/weight ratio
    items = sorted(zip(weights, profits), key=lambda x: x[1]/x[0], reverse=True)
    weights, profits = zip(*items)

    from queue import Queue
    Q = Queue()

    u = Node(-1, 0, 0, 0)
    v = Node(0, 0, 0, 0)

    max_profit = 0

    u.bound = bound(u, n, capacity, weights, profits)
    Q.put(u)

    while not Q.empty():
        u = Q.get()

        if u.level == n - 1:
            continue

        # Next level
        v = Node(u.level + 1, u.profit, u.weight, 0)

        # Include item
        v.weight = u.weight + weights[v.level]
        v.profit = u.profit + profits[v.level]

        if v.weight <= capacity and v.profit > max_profit:
            max_profit = v.profit

        v.bound = bound(v, n, capacity, weights, profits)

        if v.bound > max_profit:
            Q.put(v)

        # Exclude item
        v = Node(u.level + 1, u.profit, u.weight, 0)
        v.bound = bound(v, n, capacity, weights, profits)

        if v.bound > max_profit:
            Q.put(v)

    return max_profit


# Main program
weights = list(map(int, input("Enter weights: ").split()))
profits = list(map(int, input("Enter profits: ").split()))
capacity = int(input("Enter capacity: "))

result = knapsack_bb(weights, profits, capacity)

print("Maximum profit:", result)