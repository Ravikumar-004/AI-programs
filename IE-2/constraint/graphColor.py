def greedy_coloring(graph):
    colors = {}
    for vertex in sorted(graph.keys()):
        available_colors = set(range(1, len(graph) + 1))
        for neighbor in graph[vertex]:
            if neighbor in colors:
                available_colors.discard(colors[neighbor])
        color = available_colors.pop()
        colors[vertex] = color
    return colors

def main():
    num_vertices = int(input("Enter the number of vertices: "))
    num_edges = int(input("Enter the number of edges: "))

    graph = {i: set() for i in range(num_vertices)}
    print("Enter the edges (vertex1 vertex2): ")
    
    for _ in range(num_edges):
        v1, v2 = map(int, input().split())
        graph[v1].add(v2)
        graph[v2].add(v1)

    colors = greedy_coloring(graph)
    cols = ["red","green","blue","yellow","orange","purple","pink","brown","black","white"]
    print("\nVertex\tColor")
    for vertex, color in colors.items():
        print(f"{vertex}\t{cols[color-1]}")

if __name__ == "__main__":
    main()