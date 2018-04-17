with open('shopping_list_1.txt', encoding = 'utf-8', mode = 'r') as file1:
    file1 = file1.read().split('\n')
    popped1 = file1.pop()
    #print(file1)

with open('shopping_list_2.txt', encoding = 'UTF-8', mode = 'r') as file2:
    file2 = file2.read().split('\n')
    popped2 = file2.pop()
    #print(file2)

with open('shopping_list_3.txt', encoding = 'utf-8', mode = 'r') as file3:
    file3 = file3.read().split('\n')
    popped3 = file3.pop()
    #print(file3)

final = file1 + file2 + file3
final = list(set(final))
final = '\n'.join(sorted(final)).title()
#print(final)

with open('shopping_list.txt', encoding = 'utf-8', mode ='w') as final_file:
    final_file.write(final)
    final_file.close()
