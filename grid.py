from grid_helper import *


# 广度优先 Breadth First Search 
def bfs(start, end):
    grids = [start]
    parent = [-1]
    n = 0

    while n < len(grids):
        print("n=", n)
        print_grid(grids)

        if end in grids:
            print_result(end, grids, parent) # 输出结果
            return 1

        node = grids[n]

        new_leafs = []

        for i in moves(node):
            if i not in grids:
                new_leafs.append(i)

        grids += new_leafs
        parent += [n]*len(new_leafs)

        n += 1

    return 0




if __name__ == '__main__':
    #test()

    '''
    start = [
        [7, 1, 3],
        [2, 4, 5],
        [8, 6, 0]
    ]
    '''

    start = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 5, 8]
    ]

    end = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    r = bfs(start, end)
    print(r)
