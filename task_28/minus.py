f = open('numbers.txt', 'r')
file_value = f.read().split()
sum = 0

for i in file_value:
    if int(i) < 0:
        sum += int(i)

f.close()
print(sum)
