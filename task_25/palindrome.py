import sys

num = sys.argv[1]
rev_num = num[::-1]

if num == rev_num:
    print(1)
else:
    print(0)
