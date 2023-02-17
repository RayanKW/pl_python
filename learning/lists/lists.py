# #it isa data type containng a sequence of data. we can have elements of different data types.
# # elements are represented in square braces.
# ab = [1, 2,3 ,4 ,5 ]
# abc = ['a', 's','f','g','hg',]
# abcd = [1, 'e', 5]

# # .append(item)
# seq = []
# for i in range (4):
#     ele = input()
#     seq.append(ele)
# print (seq)
# print(type(seq))
# # .split(item)
# mes = "hello there how are you!"
# token = mes.split()
# print(token)
# print(type(token))
# sent = ' '.join(token)
# print(sent)
# print(type(sent))
# # print(type(spl))

## Acessing and Updating a list.
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#we use list_name[index] eg
print(a[1])
# adding an element
a.append(21)
print(a)
# reassigning
a[1] = 34
print(a)
# deleting
del a[0]
print(a)
c = a.count(6)
print(c)
d = a.index(6, 1)
print(d)
a.extend([7, 4, 7])
print (a)
a.insert(0, 45)
print(a)
a.sort()
print(a)
d = a[1:5]
print(d)
print('prints from the first index upto the 4th element')
print(a[:4])
print('prints all the elements starting from the first index')
print(a[1:])
print('prints from index 1 upto the 7th index in steps of 2')
print(a[1:7:2])
for i in a:
    print(i, end=' ')
print(' ')
#Using the map() to turn input into int type. input takes in values as str
print(list(map(int, input().split()))) # the input is of string data type which is then converted into
# in data type by the map function. that output is then stored in a list.
