import sys

word = sys.argv[1]
vowels = 'AaEeIiOoUuYy'
result = []

for i in word:
    if i in vowels:
        result.append(i)

result = ''.join(result)
print(result)
