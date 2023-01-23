count = 0
while count <= 10:
    print(count)
    count+=2
    
# example 2. the progam counts from zero only and when the user wants to -
# -continue by pressing N and n or Y or y.
countt = 0
entry = 'Y'
while entry == 'Y' or entry == 'y':
    entry = input('please entry Y(es) or N(o)')
    if entry == 'y' or entry == 'Y':
        print(countt)
        countt+=2
    elif entry == 'N' or entry == 'n':
        break
    else:
        print('invalid')

# product table
