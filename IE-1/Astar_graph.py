g = {}
h = {}
n = input("Nodes (comma-separated): ").split(',')
for i in n:
    h[i] = int(input(f"Heuristic for {i}: "))
    g[i] = {}
e = input("Edges & costs(A:B:2,B:C:1) (comma-separated): ").split(',')
for i in e:
    x, y, c = i.split(':')
    g[x][y] = int(c)
    
s = input("Start node: ")
t = input("Goal node: ")

def astar_search(s, t, g, h):
    open = [(0, s)]
    gc = {s: 0} 
    cf = {} 

    while open:
        c = min(open, key=lambda x: x[0]) 
        open.remove(c) 

        if c[1] == t:
            p = [t]
            while c[1] in cf:
                c = cf[c[1]]
                p.append(c[1])
            p.reverse()
            return p, gc[t]

        for n in g[c[1]].keys():
            tg = gc[c[1]] + g[c[1]][n]
            if n not in gc or tg < gc[n]:
                gc[n] = tg
                fc = tg + h[n]
                open.append((fc, n))
                cf[n] = c

    return None

path, cost = astar_search(s, t, g, h)
print("Path:", path)
print("Cost:", cost)
