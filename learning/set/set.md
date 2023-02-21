- List of elements of different data types, comma separated, enclosed in {}
- it does not have duplicates unlike tuples and lists.
- it is MUTABLE
## Adding elements
>> we use set_name.add(value)
- we can also update with another set.
# Set Operations
we cannot perform indexing and slicing in a set
>> adding
- we use .add(value)
>> Finding the length
- len(set_name)
>> .remove(value) - removes the specified value and if the value is not found it returns a KeyError
>> Updating
- .update(value/set2_name)
>> .discard(value) => removes the given element and if the element is not found it does not return any error
- .pop() => this unlike in list it removes the first element of the set and returns the element thst has been removed
- .clear()
## Further Set operations. 
- issubset() => 
- issuperset() =>
- union()
- intersectoin() => most must be present in both sets