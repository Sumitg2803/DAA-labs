class ItemValue:
    def __init__(self, wt, val, ind):
        self.wt = wt
        self.val = val
        self.ind = ind
        self.cost = val / wt

    def __lt__(self, other):
        return self.cost < other.cost

def fractional_knapsack(capacity, items):
    # Sort items by their cost (value/weight ratio) in descending order
    items.sort(reverse=True)
    
    total_value = 0.0
    for i in items:
        cur_wt = i.wt
        cur_val = i.val
        
        if capacity - cur_wt >= 0:
            # Capacity allows full item
            capacity -= cur_wt
            total_value += cur_val
        else:
            # Capacity only allows a fraction of the item
            total_value += cur_val * (capacity / cur_wt)
            capacity = 0 # Knapsack is full
            break
            
    return total_value

if __name__ == "__main__":
    # Example usage
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50

    items = []
    for i in range(len(weights)):
        items.append(ItemValue(weights[i], values[i], i))

    max_val = fractional_knapsack(capacity, items)
    
    print("Capacity:", capacity)
    print("Weights:", weights)
    print("Values:", values)
    print("Maximum value we can obtain:", max_val)
