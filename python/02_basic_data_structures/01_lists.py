# https://www.hackerrank.com/challenges/python-lists/problem
if __name__ == '__main__':
    a_list = []
    N = int(input())
    for _ in range(N):
        params = input().split()
        command = params[0]

        if command == 'insert':
            a_list.insert(int(params[1]), int(params[2]))
        elif command == 'print':
            print(a_list)
        elif command == 'remove':
            a_list.remove(int(params[1]))
        elif command == 'append':
            a_list.append(int(params[1]))
        elif command == 'sort':
            a_list.sort()
        elif command == 'pop':
            a_list.pop()
        elif command == 'reverse':
            a_list.reverse()
