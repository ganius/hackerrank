# https://www.hackerrank.com/challenges/crush/problem

nm = input().split()
n = int(nm[0])
m = int(nm[1])
queries = []
nums = [0] * n

for _ in range(m):
    queries.append(list(map(int, input().rstrip().split())))


def initial_attempt():
    """
    This straight-forward solution is O(n^2)
    and fails the tests after #6 because of time limits.
    """
    for query in queries:
        start = query[0] - 1  # Convert 1-based index to 0-based index
        end = query[1]
        num = query[2]
        for index in range(start, end):
            nums[index] += num
    print(max(nums))


def better_solution():
    """
    Since we are only interested in the max value and initial array consists of all 0s
    we can store only the diff array instead of the whole array and do a cumulative sum
    as we go over the array.
    """
    diff_arr = [0] * (n + 1)  # we need to include the latest item to the summation
    for query in queries:
        start = query[0] - 1  # Convert 1-based index to 0-based index
        end = query[1]
        num = query[2]
        diff_arr[start] += num
        diff_arr[end] -= num
    max_sum = 0
    current_sum = 0
    for num in diff_arr:
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
    print(max_sum)


# initial_attempt()
better_solution()