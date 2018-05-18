def dynamic_array():
    """
    Updates and prints an element of a dynamically sized array based on some input.
    Unnecessarily complicated problem, straightforward solution.
    https://www.hackerrank.com/challenges/dynamic-array/problem
    """
    first_input = input().strip().split()
    array_size = int(first_input[0])
    num_of_queries = int(first_input[1])
    last_answer = 0
    seq_list = [[] for i in range(array_size)]

    for num in range(num_of_queries):
        query = input().strip().split()
        query_type = int(query[0])
        x = int(query[1])
        y = int(query[2])
        index = (x ^ last_answer) % array_size
        if query_type == 1:
            seq_list[index].append(y)
        else:
            last_answer = seq_list[index][y % len(seq_list[index])]
            print(last_answer)


dynamic_array()
