goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def manhattan_distance(state):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            goal_position = goal_state.index(state[i])
            current_row, current_col = i // 3, i % 3
            goal_row, goal_col = goal_position // 3, goal_position % 3
            distance += abs(current_row - goal_row) + abs(current_col - goal_col)
    return distance


def solve_puzzle(initial_state):
    visited = set()
    queue = [(initial_state, [], 0)]

    while queue:
        current_state, path, steps = queue.pop(0)

        if current_state == goal_state:
            return steps, path

        visited.add(tuple(current_state))
        zero_index = current_state.index(0)
        row, col = zero_index // 3, zero_index % 3

        for dr, dc in moves:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_index = new_row * 3 + new_col
                new_state = current_state[:]
                new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]

                if tuple(new_state) not in visited:
                    new_path = path + [new_state]
                    queue.append((new_state, new_path, steps + 1))

    return None


initial_state = [1, 2, 3, 4, 0, 5, 7, 8, 6]

steps, path = solve_puzzle(initial_state)

if steps is not None:
    print("Solution found in", steps, "steps.")
    print("Path:")
    for state in path:
        for i in range(3):
            print(state[i * 3:i * 3 + 3])
        print()
else:
    print("No solution found.")