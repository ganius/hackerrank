# https://www.hackerrank.com/challenges/nested-list/problem
if __name__ == '__main__':
    students = [[input(), float(input())] for _ in range(int(input()))]
    second = sorted(list(set([student[1] for student in students])))[1]
    print('\n'.join(sorted([student[0] for student in students if student[1] == second])))
