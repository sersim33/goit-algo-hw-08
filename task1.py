import heapq

def minimum_connection_cost(cable_lengths):
    heapq.heapify(cable_lengths)
    min_cost = 0
    
    while len(cable_lengths) > 1:
        print("Current heap:", cable_lengths)
        
        shortest1 = heapq.heappop(cable_lengths)
        shortest2 = heapq.heappop(cable_lengths)
        
        print("Connecting cables of lengths", shortest1, "and", shortest2)
        
        min_cost += shortest1 + shortest2
        
        combined_length = shortest1 + shortest2
        print("Total length after connection:", combined_length)
        
        heapq.heappush(cable_lengths, combined_length)
        print("Heap after connection:", cable_lengths)
        print()
    
    return min_cost

# Example usage
cable_lengths = [1, 3, 4, 8]
min_cost = minimum_connection_cost(cable_lengths)
print("Minimum connection cost:", min_cost)