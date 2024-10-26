import heapq
from collections import defaultdict, deque

def find_project_order(N, M, group_ids, dependencies):
    # Create graph and in-degree count
    graph = defaultdict(list)
    in_degree = [0] * N
    
    for A, B in dependencies:
        graph[A - 1].append(B - 1)  
        in_degree[B - 1] += 1

    # Initialize priority queue with nodes having zero in-degree
    initial_nodes = []
    for i in range(N):
        if in_degree[i] == 0:
            initial_nodes.append((group_ids[i], i))
    
    
    heapq.heapify(initial_nodes)
    
    result = []
    while initial_nodes:
        # Pick the smallest node 
        _, project_id = heapq.heappop(initial_nodes)
        result.append(project_id + 1)  # Store the result with 1-based indexing

        #  Process its neighbors
        for neighbor in graph[project_id]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                heapq.heappush(initial_nodes, (group_ids[neighbor], neighbor))
    
    #  Check if all projects are processed
    if len(result) == N:
        print(" ".join(map(str, result)))
    else:
        print("-1")

N, M = map(int, input().split())
group_ids = list(map(int, input().split()))
dependencies = [tuple(map(int, input().split())) for _ in range(M)]


find_project_order(N, M, group_ids, dependencies)
