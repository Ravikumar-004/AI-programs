def bfs_recursive(graph, queue, visited):
    if not queue:
        return
    vertex = queue.pop(0)
    print(vertex, end=" ")
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            queue.append(neighbor)
            visited.add(neighbor)
    bfs_recursive(graph, queue, visited)

graph = {}
nodes = int(input("Enter the number of nodes in the graph: "))
for i in range(nodes):
    node = input("Enter node name: ")
    neighbors = input("Enter neighbors of {} separated by spaces: ".format(node)).split()
    graph[node] = neighbors

start_node = input("Enter the starting node for BFS traversal: ")

print("\n\nRecursive BFS Traversal:")
bfs_recursive(graph, [start_node], {start_node})
