import sys

value = sys.argv[1].split()
new_list = []

for i in value:
    new_list.append(i[::-1])

new_list = ' '.join(new_list)
print(new_list)
