import sys

word = sys.argv[1]

m = word.count('m')
w = word.count('w')

m_symbol = m * '*'
w_symbol = w * '*'

print('m (%s) %s' % (m, m_symbol))
print('w (%s) %s' % (w, w_symbol))
