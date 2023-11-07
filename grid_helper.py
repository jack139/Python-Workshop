from copy import deepcopy

'''
grid 表示：

s = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
'''


# 返回 0 的位置
def zero_pos(s):
    for i in range(3):
        for j in range(3):
            if s[i][j]==0:
                return i, j
    return None


# 返回 布局s 的所有 下一步
def moves(s):
    m = []
    row, col = zero_pos(s)

    if row > 0: # 上
        m.append(deepcopy(s))
        m[-1][row-1][col], m[-1][row][col] = m[-1][row][col], m[-1][row-1][col]

    if row < 2: # 下
        m.append(deepcopy(s))
        m[-1][row+1][col], m[-1][row][col] = m[-1][row][col], m[-1][row+1][col]

    if col > 0: # 左
        m.append(deepcopy(s))
        m[-1][row][col-1], m[-1][row][col] = m[-1][row][col], m[-1][row][col-1]

    if col < 2: # 右
        m.append(deepcopy(s))
        m[-1][row][col+1], m[-1][row][col] = m[-1][row][col], m[-1][row][col+1]

    return m


# 输出 一组 布局
def print_grid(s):
    for i in range(3):
        l = []
        for n in range(len(s)):
            l.append(''.join([str(x) for x in s[n][i]]))
        print(' '.join(l))
    print()



# 回溯输出结果
def print_result(grids, target_idx):
    print("total grids=", len(grids))
    print("target idx=", target_idx)
    p = [target_idx]
    while p[0]!=-1:
        p = [grids[p[0]][1]] + p
    #print("parents:", p)
    print("depth=", len(p)-1)
    print_grid([grids[i][0] for i in p[1:]])


# 计算两个布局间的差异
def grid_diff(s1, s2):
    diff = 0
    for i in range(len(s1)):
        for j in range(len(s1[i])):
            if s1[i][j] != s2[i][j]:
                diff += 1
    return diff


# 计算两个布局间的距离
def grid_distance(s1, s2):
    # 返回 x 的位置
    def x_pos(s, x):
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


# 测试
def test():
    s = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 8, 5]
    ]

    print_grid([s])

    s2 = moves(s)

    print_grid(s2)


if __name__ == '__main__':
    test()