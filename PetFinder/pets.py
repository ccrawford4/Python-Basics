class Dog: # Creates a class 'Dog'
    def __init__(self, pName, pBirthdate, pBreed, pColor): # Initalizes the variables
        self.name = pName
        self.birthdate = pBirthdate
        self.breed = pBreed
        self.color = pColor
        self.type = 'Dog'
    
    def __str__(self): # Print statement
        return f'Name: {self.name} Birthdate: {self.birthdate} Breed: {self.breed} Color: {self.color}'
    
    def get_name(self): # Returns the name of the pet
        return self.name

class Cat: # Creates a class 'Cat'
    def __init__(self, pName, pBirthdate, pBreed, pColor): # Initalizes the variables
        self.name = pName
        self.birthdate = pBirthdate
        self.breed = pBreed
        self.color = pColor
    
    def get_name(self): # Returns the name of the pet
        return self.name
    
    def __str__(self): # Creates the print statement
        return f'Name: {self.name} Birthdate: {self.birthdate} Breed: {self.breed} Color: {self.color}'
    
class Fish: # Creates class 'Fish'
    def __init__(self, pName, pBirthdate, pBreed, pColor): # Initalizes variables 
        self.name = pName
        self.birthdate = pBirthdate
        self.breed = pBreed
        self.color = pColor
    
    def get_name(self): # Returns the name of the pet
        return self.name
    
    def __str__(self): # Creates the print statement
        return f'Name: {self.name} Birthdate: {self.birthdate} Breed: {self.breed} Color: {self.color}'


class Bird: # Creates a class 'Bird'
    def __init__(self, pName, pBirthdate, pBreed, pColor): # Initalizes variables
        self.name = pName
        self.birthdate = pBirthdate
        self.breed = pBreed
        self.color = pColor

    def get_name(self): # Returns the name 
        return self.name
    
    def __str__(self): # Creates the print statement
        return f'Name: {self.name} Birthdate: {self.birthdate} Breed: {self.breed} Color: {self.color}'
    

class Hamster: # Creates the 'Hamster' class
    def __init__(self, pName, pBirthdate, pBreed, pColor): # Initializes variables
        self.name = pName
        self.birthdate = pBirthdate
        self.breed = pBreed
        self.color = pColor
    
    def get_name(self): # Returns the name of the pet 
        return self.name
  
    def __str__(self): # Creates the print statement 
        return f'Name: {self.name} Birthdate: {self.birthdate} Breed: {self.breed} Color: {self.color}'
    