# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    winner = max(arr)
    max_removed = [x for x in arr if x != winner]
    runner_up = max(max_removed)
    print(runner_up)