def valid(state):
    ml, cl, mr, cr, boat = state
    if ml< 0 or cl < 0 or mr <0 or cr < 0:
        return False
    if (ml > 0 and ml < cl) or (mr > 0 and mr < cr):
        return False
    return True

def get_moves():
    return [(2, 0), (0, 2), (1, 1), (1, 0), (0, 1)]

def dfs(state, visited = None):
    if visited is None:
        visited = set()
    if state[0] == state[1] == 0:
        return [state]
    visited.add(state)
    ml, cl, mr, cr, boat = state
    for move in get_moves():
        mx, cx = move
        if boat == "Left":
            new_state = (ml - mx, cl - cx, mr + mx, cr + cx, 'Right')
        else:
            new_state = (ml + mx, cl + cx, mr - mx, cr - cx, 'Left')
        if valid(new_state) and new_state not in visited:
            path = dfs(new_state, visited)
            if path is not None:
                return[state] + path
    if boat == "Left":
        new_state = (ml, cl, mr , cr, "Right")
    else:
        new_state = (ml, cl, mr , cr, "Left")
    if valid(new_state) and new_state not in visited:
        path = dfs(new_state, visited)
        if path is not None:
            return[state] + path
    return None

ml = int(input("Missionaries: "))
cl = int(input("Cannibals: "))

start = (ml,cl, 0, 0, "Left")

path = dfs(start)
if path is not None:
    print("Solution Found: ")
    for state in path:
        mx,cx,my,cy,boat = state
        if(boat == "Left"):
            print("%d\t%d Boat ------ %d\t%d"%(mx,cx,my,cy))
        if(boat == "Right"):
            print("%d\t%d ------ Boat %d\t%d"%(mx,cx,my,cy))

else:
    print("No Solution")