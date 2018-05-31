# https://www.hackerrank.com/challenges/list-comprehensions/problem
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print([[_x, _y, _z] for _x in range(x + 1) for _y in range(y + 1)
           for _z in range(z + 1) if _x + _y + _z != n])
