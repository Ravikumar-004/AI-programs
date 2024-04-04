def dfs_recursive(graph, start, visited):
    if start not in visited:
        print(start, end=" ")
        visited.add(start)
        for neighbor in graph[start]:
            dfs_recursive(graph, neighbor, visited)

graph = {}
nodes = int(input("Enter the number of nodes in the graph: "))
for i in range(nodes):
    node = input("Enter node name: ")
    neighbors = input("Enter neighbors of {} separated by spaces: ".format(node)).split()
    graph[node] = neighbors

start_node = input("Enter the starting node for DFS traversal: ")

print("\n\nRecursive DFS Traversal:")
dfs_recursive(graph, start_node,set())
