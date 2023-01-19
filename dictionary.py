det = {'firstName':'John',
                   'LastName':'Ouko',
                   'Age': 22,
                   'PhoneNumber':'0712345678',
                   'Email':'student@gmail.com'}
a = det.get('Age')
b= det['PhoneNumber']
print(a)
q= det['firstName']
print(q)
#below sets the age default to 20 incase Age doesnt exist. see notes.md
Ag= det.get('Age', 20)
print(Ag)
# print(det)

# list slicing, revisit why the liat length doesn't have to be the same
# x= [1,2,3,4]
# x[1:3]=[11,22,33]
# print(x)

#2 dimensional list
x = [0] * 3
for i in range(0, 3):
    x[i] = [0] * 5
    # print(x)
    ##exercise

if 'Age' in det:
    print('hey')
else:
    print('noooo')


#update the age to 55.
print('the age is')
det['Age'] = 55;
#print lastname
print('print the lastname')
print(det['LastName'])
#print the length of the dictionary
print('the length of the dictionary')
print(len(det))
for ky in det.keys():
    # pass
    print(ky, end=' ')
print()
d = {'Fred': 44, 'Ella': 39, 'Owen': 40, 'Zoe': 41}
for v in d.values():
    print(v, end=' ')
print()
##asumiing we have names and values in a separate we, can zip them together unsing zip()

names=['jonh', 'jude', 'joseph', 'isaiah']
ages=[23, 32,12,43]
deta = dict(zip(names, ages))
print(deta)
#and thus generating a dictionary.