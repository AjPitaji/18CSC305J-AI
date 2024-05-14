import heapq

def h(state):
    """Heuristic function that calculates the Manhattan distance from each tile to its goal position."""
    distance = 0
    goal_position = [(i, j) for i in range(3) for j in range(3)]
    for x in range(3):
        for y in range(3):
            val = state[x][y]
            if val != 0:
                target_x, target_y = goal_position[val]
                distance += abs(target_x - x) + abs(target_y - y)
    return distance

def move(state, direction):
    """Generates a new state by moving a tile into the blank space in the given direction."""
    x, y = next((i, j) for i in range(3) for j in range(3) if state[i][j] == 0)
    moves = {'up': (x-1, y), 'down': (x+1, y), 'left': (x, y-1), 'right': (x, y+1)}
    if direction in moves:
        nx, ny = moves[direction]
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            return new_state
    return None

def print_state(state):
    for row in state:
        print(" ".join(map(str, row)))
    print()

def solve(initial):
    """Uses the A* algorithm to find the solution to the 8-puzzle problem."""
    parent = {tuple(map(tuple, initial)): None}
    g = {tuple(map(tuple, initial)): 0}
    open_heap = [(h(initial), initial)]
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    while open_heap:
        _, current = heapq.heappop(open_heap)
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[tuple(map(tuple, current))]
            return path[::-1]

        for direction in ['up', 'down', 'left', 'right']:
            neighbor = move(current, direction)
            if neighbor is not None:
                neighbor_tuple = tuple(map(tuple, neighbor))
                new_g = g[tuple(map(tuple, current))] + 1
                if neighbor_tuple not in g or new_g < g[neighbor_tuple]:
                    g[neighbor_tuple] = new_g
                    f = new_g + h(neighbor)
                    heapq.heappush(open_heap, (f, neighbor))
                    parent[neighbor_tuple] = current
    return None

initial_state = [[2, 8, 3], [1, 6, 4], [7, 0, 5]]
solution = solve(initial_state)
if solution:
    for state in solution:
        print_state(state)
else:
    print("No solution found.")
