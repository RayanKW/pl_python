- It's MUTABLE. we can change the value
## Acessing and Updating Elements in a list
### Accessing
- every element in the list has an index value.
- we use list_name[index]
### Updating
- we can either reassign, delete, add
to add we use the .append() method
to delete we use the del keyword
to reasign we set the element using the index i.e list_name[1]= 34 we are reasingning the element in index one to be 34.
## Built in functions
### There are some few values that return the value but doesn't change the existing list.
- .count()
>> list_name.count(value) => This returns the number occurence of a value in a list.
- .index()
>> list_name.index(value) => This returns the index of the value which appears first in the list.
list_name.index(value, where we start to look from) => eg a.index(2, 4) starts from index 4
### Others do not return but change the list.
- append()
>> list_name.append(value you want to add)
- extend()
>> list_name.extend([7, 4, 7]) => adds multiple values to the list
- .insert()
>> insert(index, value) => allows us to add an element in a particular index.
- .pop() => removes the last element in the list
>> .remove(value) => removes the value specified and rhats is the first occurence
- .sort() => sorts the elements in ascending order
### Slicing a list
- a[1:4] => prints elements from index 1 upto the 3rd index (n-1)