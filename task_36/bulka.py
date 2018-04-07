# import sys
#
# data = sys.argv[1]
# data = data.split(',')
# data[0] = data[0].title() + ','
# data[1] = data[1] + ' и'
# data[-1] = data[-1] + '.'
# data = ' '.join(data)
# print(data)

# import sys
# w = sys.argv[1].split(',')
# last = w.pop()
# print(', '.join(w).capitalize() + ' и ' + last)

import sys

data = sys.argv[1].split(',')
last = data.pop()
print(', '.join(data).capitalize() + ' и ' + last + '.')
