# https://www.hackerrank.com/challenges/sparse-arrays/problem

strings_count = int(input())
strings = []
for _ in range(strings_count):
    string = input()
    strings.append(string)

queries_count = int(input())
queries = []
for _ in range(queries_count):
    query = input()
    queries.append(query)

for query in queries:
    print(strings.count(query))
