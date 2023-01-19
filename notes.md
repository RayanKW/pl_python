## DICTIONARY (other languages might be called hashmaps or associative array)
- Keys must be unique; you can have only one value associated
with a key. Values do not have to be unique; many keys may
have the same value.
- EG IN:
    personalDetails = {'firstName':'John',
                   'LastName':'Ouko',
                #    'Age': ,
                   'PhoneNumber':'0712345678',
                   'Email':'student@gmail.com'}
                personaldetails['phonenumber'] will return '0712345678' and if you use the wrong key you'll get a key error.

                personaldetails.get('Age') works like personaldetails['Age'], except that if the
key is not found, the value None is returned.
            personaldetails.get(age, default_value) returns the value asso-
ciated with key, or the default_value if there is no such key.
- There is a special command, del, for removing something from
a dictionary an dyou'll get a key error if the key is not found in the dict
- Keys must be immutable
- Lists and tuples are convenient for storing collections of data, but they have some limitations. For one, we
locate an element within a list or tuple based on its position (index).
- The placement and lookup of an element within a dictionary uses a process known
as hashing
-> we copy a dictionary using .copy() ie thisdic = dict.copy()
- .pop(keywor)removes the specified key word, .popitem() removes the last item in the dictionary
- The del keyword removes the item with the specified key name:
{ del dict['it']}
- The clear() method empties the dictionary: