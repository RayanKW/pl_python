class computer:
    
    def __init__(self, name, age) -> None:
        #below are our variables. the self is a keyword saying literally self.
        # below is how you create variables in a class
        self.name= name
        self.age = age
        #methods are just 'functions' in classes. thpse verbs. what can an obvject do say bike, ride right
        #the method thus would be <def ride()>
    def say_name(self): #when creating the method you pass in self
        print('my name is ' + self.name)
per = computer('john', 12)
#per is our object. recall an object is an instance of a class and is is stored in it location.
#consider the code below:
per2 =computer('jos', 23)
#per2 is another object in the class computer. to see the ID we do:
print(id(per))
print(id(per2))
#frim the above you can see they are both located in different memory, 2 instnce
per.say_name() #calling a method of per
print(per.age)
print(per.name)