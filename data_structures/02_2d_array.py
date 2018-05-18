def array_2d(arr):
    """
    https://www.hackerrank.com/challenges/2d-array/problem

    Calculates the "hourglass" sum of every hourglass in 6X6 2D array and return the max sum
    :param arr: a list
    :return: the max sum
    """
    max_sum = -1000
    for i in range(len(arr)-2):
        for j in range(len(arr[i])-2):
            s = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            if s >= max_sum:
                max_sum = s
    return max_sum
