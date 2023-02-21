# concepts of Oop
- class
- objects
- Encapsulation
- Inheritance
- polymorphism
- Abstraction
## CLASS
+ It is a blueprint followed by objects. It is also a logical structure with a behaviour.
+ A class can have atttributes and functions(the functions are also called class methods)
{attributes and methods are called class members}
+ a class can have multiple objects.
## Object
+ It is an instance of a class. 
an oject can also have attributes and methods of the class.
## Abstraction
+ Hidding the implimentation details and showing the essential  details
> The concrete class should implement all the abstract methods of the abstract class. if it fails then it is also an abstact class. see img
![Alt text](resources/Screenshot%20from%202023-02-21%2016-03-52.png)
## Encapsulation
+ Wrapping up of data and funtion in a single entity
Public - Accesed by any function in any class(low level data protection)
protected - accessed by the only class the data was declared or inherited(medium)
private - only class the data is declared(high level)
## Inheritance
Derived class(chilld) inherits the properties of the base class(parent).
### Single inheritance
+ it inherits the variables and mothods of the parent class.
### multi level inheritance
+ A child(derived class) inherits from the base class and that child acts as a parent to another child
### Heirachichal inheritance
+ A base class can have multiple children.
+ Note that the methods of child1 cannot and are not available to child2 and vice versa in this case
### Multiple inheritance
+ A derived class acquires or inherits from multiple base classes
## Polymorphism
+ Implimenting same methods in different context.
+ Method overriding>> the latest method will be executed rather than the first one.
