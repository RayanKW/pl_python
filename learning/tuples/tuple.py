a = () # empty tuple
ab = 1, 2, 3, 4 #this is treated as a tuple
ac = (1, 3, 5, 6, 7)
c = ab + ac #concatenating
print(c)
print(len(c)) #printing the length of the tupple
print(type(c))
print (c[1:4]) #slicing
print(c*2) #repeats the tupple twice
#membership
print(10 in c) #checks if 10 is a member of the tupple c note we can also use not in
# iterative statement
print('the loop below iterates through all the values of the tupple and prints the values')
for i in c:
    print(i, end=" ")
    break
print(a.count(1))#lists the occurence of the specified value
print(min(c)) # prints min value in the tupple
print(max(c)) #prints the max value of the elements in tuple c
y = tuple("hello")
print(y)#  cponverts the string "hello" into a tuple
print(type(y))# check the type of y
z = ['w', 1, 'e']
m = tuple(z)#turns the list z into a tupple.
print(m)