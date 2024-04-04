n, m = map(int, input("Enter the dimensions of the room (length breadth): ").split())
print("Enter room: (1 for dirt, 0 for no dirt, -1 for obstacle)")
room = [list(map(int, input().split())) for i in range(n)]

def clean_dirt(start):
    que, vis = [start], [start]
    if room[0][0] == 1:
            room[0][0] = 0
            print(f"Dirt found and cleaned at (0, 0)")
    while que:
        x, y = que.pop(0)
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in vis:
                que.append((nx, ny))
                vis.append((nx, ny))
                print(f"Vacuum is moving to ({nx}, {ny})")
                if (room[nx][ny] == 1):
                    room[nx][ny] = 0
                    print(f"Dirt found and cleaned at ({nx}, {ny})")
                    
clean_dirt((0, 0))
print('\nRoom:')
for row in room:
    print(' '.join(map(str, row)))    