# Function for Fractional Knapsack
def fractional_knapsack(weights, profits, capacity):
    n = len(weights)

    # Calculate profit/weight ratio
    items = []
    for i in range(n):
        ratio = profits[i] / weights[i]
        items.append((weights[i], profits[i], ratio))

    # Sort items by ratio (descending)
    items.sort(key=lambda x: x[2], reverse=True)

    total_profit = 0.0

    for w, p, r in items:
        if capacity >= w:
            capacity -= w
            total_profit += p
        else:
            total_profit += r * capacity
            break

    return total_profit


# Main program
weights = list(map(int, input("Enter weights: ").split()))
profits = list(map(int, input("Enter profits: ").split()))
capacity = int(input("Enter capacity: "))

max_profit = fractional_knapsack(weights, profits, capacity)

print("Maximum profit:", max_profit)