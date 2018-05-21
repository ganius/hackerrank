# https://www.hackerrank.com/challenges/array-left-rotation/problem

nd = input().split()
size = int(nd[0])
rots = int(nd[1])
array = list(map(int, input().rstrip().split()))
print(" ".join(list(map(str, array[rots:] + array[:rots]))))