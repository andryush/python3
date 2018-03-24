import sys

first = sys.argv[1]
first = set(first)

second = ''.join(sorted(first))

print(second)
