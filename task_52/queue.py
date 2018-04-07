f = open('queue.txt', 'r')

data = f.read().split()
#data = ' '.join(sorted(data, reverse = True)) # high to low sort
max = max(data)
data.remove(max)
data.insert(0, max)
data = ' '.join(data)
print(data)
