import sys

num = int(sys.argv[1])

num = '{:,}'.format(num).replace(',', ' ')

print(num)
