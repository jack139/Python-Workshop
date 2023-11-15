from copy import deepcopy

'''
grid format:
s = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 0]]
'''

# return the positon of '0'
def zero_pos(s):
    for i in range(3):
        for j in range(3):
            if s[i][j]==0:
                return i, j
    return None

# return all next grids
def moves(s):
    m = []
    row, col = zero_pos(s)

    if row > 0: # up
        m.append(deepcopy(s))
        m[-1][row-1][col], m[-1][row][col] = \
                m[-1][row][col], m[-1][row-1][col]

    if row < 2: # down
        m.append(deepcopy(s))
        m[-1][row+1][col], m[-1][row][col] = \
                m[-1][row][col], m[-1][row+1][col]

    if col > 0: # left
        m.append(deepcopy(s))
        m[-1][row][col-1], m[-1][row][col] = \
                m[-1][row][col], m[-1][row][col-1]

    if col < 2: # right
        m.append(deepcopy(s))
        m[-1][row][col+1], m[-1][row][col] = \
                m[-1][row][col], m[-1][row][col+1]

    return m

# print a set of grids
def print_grid(s):
    for i in range(3):
        l = []
        for n in range(len(s)):
            l.append(''.join([str(x) for x in s[n][i]]))
        print(' '.join(l))
    print()

# find history grids
def find_history(grids, target_idx):
    p = [target_idx]
    while p[0]!=-1:
        p = [grids[p[0]][1]] + p
    return [grids[i][0] for i in p[1:]]

# return the difference of two grids
def grid_diff(s1, s2):
    diff = 0
    for i in range(len(s1)):
        for j in range(len(s1[i])):
            if s1[i][j] != s2[i][j]:
                diff += 1
    return diff

# return the distance (steps) between two grids
def grid_distance(s1, s2):
    def x_pos(s, x): # return the position of x
        for i in range(len(s)):
            for j in range(len(s[i])):
                if s[i][j]==x:
                    return i, j
        return None

    dist = 0
    for i in range(len(s1)):
        for j in range(len(s1[i])):
            i2, j2 = x_pos(s2, s1[i][j])
            dist += (abs(i-i2) + abs(j-j2))
    return dist


# Breadth First Search 
def bfs(start, end):
    grids = [(start, -1)] # (grid, parent)
    queue = [0] # queue, use grid index in grids

    while len(queue)>0:
        grid_s = [x[0] for x in grids]

        if end in grid_s: # check whether ending
            target_idx = grid_s.index(end)
            history = find_history(grids, target_idx)
            return history, len(grids)

        node = queue[0] # FIFO
        queue = queue[1:] # remove node from queue

        # generate new grids
        for i in moves(grids[node][0]):
            if i not in grid_s: # skip existed grids
                grids.append((i, node))
                queue.append(len(grids)-1)

    return [], len(grids)

# Depth First Search 
def dfs(start, end, max_depth=5):
    grids = [(start, -1, 0)] # (grid, parent, depth)
    stack = [0] # stack, use grid index in grids

    while len(stack)>0:
        stack_s = [grids[x][0] for x in stack]

        if end in stack_s: # check whether ending
            target_idx = stack[stack_s.index(end)]
            history = find_history(grids, target_idx)
            return history, len(grids)

        node = stack.pop() # LIFO
        depth = grids[node][2]

        if depth>max_depth: # search limit to max_depth
            continue

        history = find_history(grids, node)

        # generate new grids
        for i in moves(grids[node][0]):
            if i not in stack_s+history: # skip existed grids
                grids.append((i, node, depth+1))
                stack.append(len(grids)-1)

    return [], len(grids)

# Greedy search
def greedy(start, end, cost_fn):
    grids = [(start, -1)]
    queue = [0]

    while len(queue)>0:
        grid_s = [x[0] for x in grids]

        if end in grid_s:
            target_idx = grid_s.index(end)
            history = find_history(grids, target_idx)
            return history, len(grids)

        # find the node with minimum cost
        min_cost = 1e8
        p = 0
        for n, x in enumerate(queue):
            x_dist = cost_fn(grids[x][0], end) # cost
            if x_dist < min_cost:
                min_cost = x_dist
                p = n

        node = queue[p]
        queue = queue[:p] + queue[p+1:]  # remove from quene

        # generate new grids
        for i in moves(grids[node][0]):
            if i not in grid_s:
                grids.append((i, node))
                queue.append(len(grids)-1)

    return [], len(grids)

# A* search
def Astar(start, end, cost_fn):
    grids = [(start, -1, 0)] # (grid, parent, depth)
    queue = [0]

    while len(queue)>0:
        grid_s = [x[0] for x in grids]

        if end in grid_s:
            target_idx = grid_s.index(end)
            history = find_history(grids, target_idx)
            return history, len(grids)

        # find the node with minimum cost
        min_cost = 1e8
        p = 0
        for n, x in enumerate(queue):
            # cost + depth
            x_dist = cost_fn(grids[x][0], end) + grids[x][2]
            if x_dist < min_cost:
                min_cost = x_dist
                p = n

        node = queue[p]
        queue = queue[:p] + queue[p+1:]
        depth = grids[node][2]

        # generate new grids
        for i in moves(grids[node][0]):
            if i not in grid_s:
                grids.append((i, node, depth+1))
                queue.append(len(grids)-1)

    return [], len(grids)


if __name__ == '__main__':
    start = [[7, 1, 3],
             [2, 4, 5],
             [8, 6, 0] ]
    end   = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 0] ]

    print("BFS", "-"*80)
    r, size = bfs(start, end)
    print(f"total grids={size}\tdepth={len(r)}")
    print_grid(r)
    
    print("DFS", "-"*80)
    r, size = dfs(start, end, 15)
    print(f"total grids={size}\tdepth={len(r)}")
    print_grid(r)

    print("Greedy diff", "-"*80)
    r, size = greedy(start, end, grid_diff)
    print(f"total grids={size}\tdepth={len(r)}")
    print_grid(r)

    print("Greedy distance", "-"*80)
    r, size = greedy(start, end, grid_distance)
    print(f"total grids={size}\tdepth={len(r)}")
    print_grid(r)

    print("A-star diff", "-"*80)
    r, size = Astar(start, end, grid_diff)
    print(f"total grids={size}\tdepth={len(r)}")
    print_grid(r)

    print("A-star distance", "-"*80)
    r, size = Astar(start, end, grid_distance)
    print(f"total grids={size}\tdepth={len(r)}")
    print_grid(r)
