# coding=utf-8

PI = 3.14

radius = [1, 2, 3]
result = {}

def circle_area(r):
    area = PI * r ** 2
    return area


for r in radius:
    result[str(r)] = circle_area(r)

print(result)
