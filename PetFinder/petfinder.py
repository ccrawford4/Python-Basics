import pets # Imports the pets.py module 
def main(): # Initalizes main function
    lstPets = fReadData() # Calls fReadData function and stores it into variable lstPets
    user_input = fShowMenu() # Calls fShowMenu function and stores returned value into user_input
    while user_input != '6':
        if user_input == '1': # If the user_input == '1' then the program calls function showPetnames with lstPets as an argument
            showPetNames(lstPets)
        elif user_input == '2': # If the user_input == '2' then the program calls function searchPets with lstPets as an argument
            searchPets(lstPets)
        elif user_input == '3': # If the user_input == '3' then the program calls function showList with lstPets as an argument
            showList(lstPets)
        elif user_input == '4': # If the user_input == '4' then the program calls function showPetType with lstPets as an argument
            showPetType(lstPets)
        elif user_input == '5': # If the user_input == '5' then the program calls function sortPets with lstPets as an argument
            sortPets(lstPets)
        else: # If the user_input is equal to '6' the program prints a goodbye statement and terminates the program
            print('Goodbye!')
        user_input = fShowMenu()
    print('Goodbye!')
    exit()

def fReadData(): # Initalizes function fReadData
    lstPets = [] # Initalizes lstPets with an empty list
    file = open('pets.csv', 'r') # Opens the pets.csv file in the read mode
    list_file = file.readlines() # Converts the file into a list
    for i in range(len(list_file)): # Iterates through each element in the list
        list_file[i] = list_file[i].split(',') # Splits each element in the list created a nested list
        for x in range(len(list_file[i])): # Iterates through each element in the nested list
            list_file[i][x] = list_file[i][x].rstrip('\n') # Removes the newlines from the elements in the nested list
            if list_file[i][x] == 'Dog': # If the value of the element == 'Dog' then the program assigns a class object using class dog with the corresponding name, birthdate, breed, and color as arguments
                dog = pets.Dog(list_file[i][x+1], list_file[i][x+2], list_file[i][x+3], list_file[i][x+4])
                lstPets.append(dog) # Adds the class object to lstPets
            elif list_file[i][x] == 'Cat': # If the value of the element == 'Cat' then the program assigns a class object using class dog with the corresponding name, birthdate, breed, and color as arguments
                cat = pets.Cat(list_file[i][x+1], list_file[i][x+2], list_file[i][x+3], list_file[i][x+4])
                lstPets.append(cat) # Adds the class object to lstPets
            elif list_file[i][x] == 'Fish': # If the value of the element == 'Fish' then the program assigns a class object using class dog with the corresponding name, birthdate, breed, and color as arguments
                fish = pets.Fish(list_file[i][x+1], list_file[i][x+2], list_file[i][x+3], list_file[i][x+4])
                lstPets.append(fish) # Adds the class object to lstPets
            elif list_file[i][x] == 'Bird': # If the value of the element == 'Bird' then the program assigns a class object using class dog with the corresponding name, birthdate, breed, and color as arguments
                bird = pets.Bird(list_file[i][x+1], list_file[i][x+2], list_file[i][x+3], list_file[i][x+4])
                lstPets.append(bird) # Adds the class object to lstPets
            elif list_file[i][x] == 'Hamster': # If the value of the element == 'Hamster' then the program assigns a class object using class dog with the corresponding name, birthdate, breed, and color as arguments
                hamster = pets.Hamster(list_file[i][x+1], list_file[i][x+2], list_file[i][x+3], list_file[i][x+4])
                lstPets.append(hamster) # Adds the class object to lstPets
    return lstPets # Returns the list with all the class objects

def fShowMenu(): # Initalizes fShowMenu function
    # Prints the menu
    print('\n')
    print('\t---------Pet Finder Menu---------------')
    print('\t1. Show Pet Names')
    print('\t2. Search for Pet')
    print('\t3. Show List')
    print('\t4. Shows Pets of Certain Type')
    print('\t5. Sort all of the pets alphabetically')
    print('\t6. Exit the Program')
    print('\t---------------------------------------')
    print('\n')
    user_input = input('Please enter one of the above options: ') # Asks the user for an input
    list_options = ['1', '2', '3', '4', '5', '6']
    while user_input not in list_options: # Keeps asking for a proper input if the user input is not one of the requested options
        print('Invalid input!')
        user_input = input('Please enter one of the above options: ')
    return user_input # Returns the user input

def showPetNames(pList): # Initalizes showPetNames function with pList as a parameter
    for pet in pList: # Iterates through pList
        print(pet.get_name()) # Prints the pets name using the function get_name()


def searchPets(pList): # Initalizes searchPets function with pList as a parameter
    print('--Search Pet---------------')
    pet_name = input('Search for a Pet Name. What is the name of the pet you want to find? ') # Gets pet name from user
    found = False 
    for pet in pList: # Iterates through pList
        if pet.get_name() == pet_name: # if the pet name in the list is equal to the name searched for by the user
            found = True # Found is set to True
            pet.color = pet.color.rstrip('\n') # Removes the newline from the pet color 
            print(pet) # Prints the pet information (calls the __str__ function)
            print(f'Index: {pList.index(pet)}') # prints the list index of the pet 
    if found == False: # If found == false that indicates that the pet name searched for was never found and so it prints the statement: 
        print(f'Sorry, {pet_name} is not in the list.')

def showList(pList): # Initalizes showList function with pList as a parameter
    print('--Show Pets-----------------')
    for pet in pList: # Iterates through the list pList
        pet.color = pet.color.rstrip('\n') # Removes the newline character from the pet color item
        print(pet) # Prints the pet information (uses __str___ function)

def showPetType(pList): # Initalizes showPetType function with pList as a parameter
    print('--Show Pet Type-------------')
    pet_type = input('What kind of pet would you like to find? Please enter a number between 1-5. 1 = Dog, 2 = Cat, 3 = Fish, 4 = Bird, 5 = Hamster: ') # Initalizes pet type with 
    list_options = ['1', '2', '3', '4', '5']
    while pet_type not in list_options: # Input Validation 
        print('Invalid Input!')
        pet_type = input('What kind of pet would you like to find? Please enter a number between 1-5. 1 = Dog, 2 = Cat, 3 = Fish, 4 = Bird, 5 = Hamster: ')
    if pet_type == '1':
        for pet in pList:
            result = isinstance(pet, pets.Dog) # Checks to see if the pet is an object of the dog class
            if result: # If it is then it prints the pet information
                pet.color = pet.color.rstrip('\n')
                print(pet)
    elif pet_type == '2': 
        for pet in pList:
            result = isinstance(pet, pets.Cat)
            if result:
                pet.color = pet.color.rstrip('\n')
                print(pet)
    elif pet_type == '3':
        for pet in pList:
            result = isinstance(pet, pets.Fish)
            if result:
                pet.color = pet.color.rstrip('\n')
                print(pet)
    elif pet_type == '4':
        for pet in pList:
            result = isinstance(pet, pets.Bird)
            if result:
                pet.color = pet.color.rstrip('\n')
                print(pet)
    elif pet_type == '5':
        for pet in pList:
            result = isinstance(pet, pets.Hamster)
            if result:
                pet.color = pet.color.rstrip('\n')
                print(pet)
   

def sortPets(pList): # Initalizes function sortPets with pList as a parameter
    lstNames = [] # Initalizes lstNames with an empty list
    for pet in pList: # Iterates through the list 
        name = pet.get_name() # Assigns variable name with pet.get_name() 
        lstNames.append(name) # Adds pet name to the lstNames
    
    lstNames.sort() # Sorts the list in alphabetical order 
    
    for name in lstNames: # Prints the names from the list
        print(name)


main()

