from queue import Queue

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

class Node:
    def __init__(self, level, profit, bound, weight):
        self.level = level    # Level of node in decision tree
        self.profit = profit  # Profit of nodes on path from root to this node
        self.bound = bound    # Upper bound of maximum profit in subtree
        self.weight = weight  # Total weight at this node

# Returns bound of profit in subtree rooted with u
def bound(u, n, W, arr):
    # if weight overcomes the knapsack capacity
    if u.weight >= W:
        return 0
    
    profit_bound = u.profit
    
    j = u.level + 1
    totweight = u.weight
    
    # Grab as many items as possible
    while j < n and totweight + arr[j].weight <= W:
        totweight += arr[j].weight
        profit_bound += arr[j].value
        j += 1
        
    # If we couldn't grab the whole item, include its fractional part
    if j < n:
        profit_bound += (W - totweight) * arr[j].value / arr[j].weight
        
    return profit_bound

def copy_node(node):
    return Node(node.level, node.profit, node.bound, node.weight)

def knapsack_branch_bound(W, arr):
    n = len(arr)
    
    # Sort items based on value per unit weight in descending order
    arr.sort(key=lambda x: x.value / x.weight, reverse=True)
    
    Q = Queue()
    
    # Root node at level -1
    u = Node(-1, 0, 0, 0)
    v = Node(-1, 0, 0, 0)
    
    Q.put(copy_node(u))
    
    maxProfit = 0
    
    while not Q.empty():
        u = Q.get()
        
        # If it is starting node, assign level 0
        if u.level == -1:
            v.level = 0
        
        # If there is nothing on next level
        if u.level == n - 1:
            continue
            
        # Increment level and compute profit of children nodes
        v.level = u.level + 1
        
        # 1. Option: Taking the item
        v.weight = u.weight + arr[v.level].weight
        v.profit = u.profit + arr[v.level].value
        
        if v.weight <= W and v.profit > maxProfit:
            maxProfit = v.profit
            
        v.bound = bound(v, n, W, arr)
        
        # If bound value is greater than profit, then push into queue for further exploration
        if v.bound > maxProfit:
            Q.put(copy_node(v))
            
        # 2. Option: Not taking the item
        v.weight = u.weight
        v.profit = u.profit
        v.bound = bound(v, n, W, arr)
        
        if v.bound > maxProfit:
            Q.put(copy_node(v))
            
    return maxProfit


if __name__ == "__main__":
    W = 10
    
    # List of items: Item(weight, value)
    arr = [
        Item(2, 40), 
        Item(3.14, 50), 
        Item(1.98, 100),
        Item(5, 95), 
        Item(3, 30)
    ]
    
    print("Items (Weight, Value):")
    for item in arr:
        print(f"Weight: {item.weight}, Value: {item.value}")
        
    print(f"\nKnapsack Capacity: {W}")
    print("Maximum possible profit =", knapsack_branch_bound(W, arr))
