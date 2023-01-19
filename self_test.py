# #pattern program.
# for i in range(1, 7):
#     for j in range(1, i+1):
#         print("*", end=" " )
#     print('')
#     for a in range(7, 1):
#         for b in range(a+1, 1):
#             print('*', end= ' ')
#         print('')
# a = int(input('How many rows? '))
# for j in range (a+1):
#     for i in range(j+1):
#         print('#', end=' ')
#     print('')
    ##
num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]
for num in num_list:
    # print(num)
    if num>45:
        print(num)
        print('over 45')
    if num<45:
        print(num)
        print('under 45')
for count, b in enumerate(num_list, 1):
    print(count, b)
