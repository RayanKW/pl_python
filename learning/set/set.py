a = {'a', 2, 're', 21} # this is a set
#addiong a value into the set
a.add(91)
print(a)
b = {1, 3}
b.update(a)
print(b)
b = {1, 2, 3, 4, 5, 6}
b.add(20)
print(b)
b.discard(20)
b.update(a)
c = {4, 5 ,6 ,7 ,8, 9}
print(c.pop())
# c.clear()
print(max(c))
print(min(c))
print(b.issubset(c))
print(c.issubset(b)) #every element of set c is availble in b thus c is a subset of b.
#issuperset
print(" ")
print(b>=c)
print(" ")
print(b.issuperset(c)) # every element of b is available in b thus b is a superset of c
print(c.issuperset(b))
print(b.union(c))# mer
print(b.intersection(c))# returns the elements both present in both sets