import sys

num1 = int(sys.argv[1])

for num2 in range(1, 10):
    '''
    Решение с использованием f строк
    print(f'{num1} x {num2} =', num1 * num2)
    '''
    # Решение без f строк
    print('%d x %d = %d' % (num1, num2, num1 * num2))
