#BTW VERY IMPORTANT CTRL+/ TO TOGGLE LINE COMMENTS


# Strip method and whitespace: -------------------------------------------

# lastName = "  mendo za  "
# print(lastName.strip())  *Removes the whitespace from either sides of a string (you can also do lstrip and rstrip for whitespace on left and right)

# Intro to variables: -----------------------------------------------

# age, firstName, lastName, isAdult, CONSTANT_NUM = 123_123_123, "Nico", "Mendoza", True, 5
# print(age, firstName, lastName, isAdult, CONSTANT_NUM)

# Intro to lists: -----------------------------------------------------

# cars = ["mercedes", "kia",  "ferari", 'toyota', 'honda'] #do car[-1] for the last element, cars[-2] for the second to last and so on
# print("My first car was a " + cars[1])

# cars[0] = "mazda"
# cars.append("tesla")
# cars.insert(1, "nissan")

# print(cars)
# cars.remove("mazda")
# del cars[5]

# poppedCar = cars.pop()
# poppedCar2 = cars.pop(3)
# print(cars , "\n" , poppedCar, "\n", poppedCar2)

# Sorting lists: --------------------------------------------

# cars = ["bmw", "audi", "toyota", "subaru"]
# print("This is the original list:", cars)
# cars.reverse()
# print("This is the reversed list:", cars)
# print("This is the sorted list(temporarily):", sorted(cars))
# cars.sort()
# print("This is the permanently sorted list:", cars)
# cars.sort(reverse=True)
# print("This is the list in reverse alphabetical order:", cars)
# print("The length of the list is:", len(cars))

# Intro to loops: ---------------------------------------------------

# magicians = ["alice", "david", "carolina"]
# for magician in magicians:
#     print(magician.title(), "that was a great trick!")
#     print("I wonder what's up next", magician.title(), "\n")
# print("Thank you all that was a great show!")

# Numerical lists intro: ----------------------------------------------

# for value in range(1,5):
#     print(value)
# print("\n")
# for value in range(6):
#     print(value)
# print("\n")

# numbers = list(range(1,6))
# print(numbers)
# evenNumbers = list(range(2, 11, 2))
# print(evenNumbers)

# squares = []
# for value in range(1, 11):
#     squares.append(value**2)
# print(squares)
# print("The minimum is:", min(squares), "The maximum is:", max(squares), "The sum is:", sum(squares))

# sqauresShort = [value**2 for value in range(1, 11)] **This is called a list comprehension, consider using it if youre making a bunch of small lists or something to get comfortable with it
# print(sqauresShort)

# Working with part of a list: ----------------------------------------------------

# players = ["charles", "martina", "michael", "florence", "eli"]
# print(players[:4])
# print(players[2:])
# print(players[0:3])
# print(players[-3:])

# print("These are the first three players on my team:")
# for player in players[:3]:
#     print(player.title())

# myFavFoods = ["sushi", "pizza twists", "poke nachos", "matcha waffles"]
# myFavFoodsCpy = myFavFoods[:] # **This will produce an exact copy of the list as it starts at the beggining and ends at the end index)
# myFavFoods.append("tacos")
# myFavFoodsCpy.append("ramen")
# print(myFavFoods, myFavFoodsCpy)

# myFavCars = ["lambo", "kia"]
# myFavCarsCpy = myFavCars # **This will make a reference to the original list so if you change one you change the other
# myFavCars.append("honda")
# myFavCarsCpy.append("tesla")
# print(myFavCars, myFavCarsCpy)

# Tuples: ------------------------------------------------------------------------------
# **They are immutable lists(can't change the values in them) 

# dimensions = (200, 50)
# print(dimensions[0], dimensions[1])
# for dim in dimensions:
#     print(dim)
# dimensions = (400, 100)
# print("New dimensions tubple:", dimensions)

# Conditional test: -------------------------------------------------------------------------------

# **Just a note Python is case sensitive so Audi and audi !=, so if you want to compare them do car.lower() == "audi" where car = "Audi", this expression will result in True
# cars = ["audi", "bmw", "subaru", "toyota"]

# for car in cars:
#     if car == "bmw":
#         print(car.upper())
#     elif car != "subaru" and car != "audi":
#         print(car.lower())
#     elif car == "audi" or car == 0:
#         print(car.upper())
#     else:
#         print(car.title())

# carTest1 = "audi"
# carTest2 = "mazda"

# if carTest1 in cars:
#     print("It's in the list!")
# if carTest2 not in cars:
#     print("Not in the list ")

# isBoolean = True

# if Statements: ----------------------------------------------------------

# age = 12

# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# elif age <  65:
#     price = 40
# else:
#     price = 20
# print(f"Your admission cost is ${price}.")

# ***Series of if statements is useful for checking multiple conditions

# requestedToppings = ["pepperoni", "extra cheese"]

# if "mushrooms" in requestedToppings:
#     print("Adding mushrooms")
# if "pepperoni" in requestedToppings:
#     print("Adding pepperoni")
# if "extra cheese" in requestedToppings:
#     print("Adding extra cheese")

# Using if statements with lists: -----------------------------------------------------------

# requestedToppings = ["pepperoni", "green peppers", "extra cheese"]
# availableToppings = ["pepperoni", "olives", "green peppers", "pineapple"]

# if requestedToppings: #This checks if the list is empty
#     for requestedTopping in requestedToppings:
#         if requestedTopping in availableToppings:
#             print("Adding", requestedTopping)
#         else:
#             print("Sorry, we don't have", requestedTopping)
# else:
#     print("Are you sure you want a plain pizza?")

# Simple dictionary: ----------------------------------------------------------------------

# alienStats = {"color": "green", "points": 5, "health": 50} #Key value pairs?!

# print("The alien is", alienStats["color"], "and worth", alienStats["points"], "points and has", alienStats["health"], "health points.")

# alienStats["xPos"] = 0
# alienStats["yPos"] = 25
# alienStats["color"] = "yellow"
# alienStats["height"] = 5.9
# del alienStats["height"]

# print(alienStats)

# height = alienStats.get("height", "No height assigned.") #Will atttempt to get the value from the list but if it doesn't exist it will give you the default message you just set
# print(height)

# Looping through a dictionary: ---------------------------------------------------------------------

# userInfo = {"username": "magiccow", "first": "nico", "last": "mendoza", "points": 5, "altName": "magiccow"}

# setExample = {"car", "house", "vroom", "vroom"} #This is a set idk what it is tho other than that it removes duplicates
# print(setExample)

# for key, value in userInfo.items():
#     print("\nKey:", key)
#     print("Value:", value)
    
# for key in userInfo: #**This is the same thing as writing in userInfo.keys()
#     print("\nKey:", key)

# if "height" not in userInfo:
#     print("Add a height!")

# for key in sorted(userInfo):
#     print(key.title(), "is some good info.")

# for info in userInfo.values():
#     print(info)

# for info in set(userInfo.values()): #Creates a new list of the items in the previous list but removes the duplicates
#     print(info)

# Nesting: --------------------------------------------------------------------------------------------

# aliens = []

# for alienNumber in range(30):
#     newAlien = {"color": "green", "points": 5, "speed": "slow"}
#     aliens.append(newAlien)

# for alien in aliens[:3]:
#     if alien["color"] == "green":
#         alien["color"] = "yellow"
#         alien["speed"] = "medium"
#         alien["points"] = 10

# for alien in aliens[:5]:
#     print(alien)
# print("...")

# print("Total number of aliens:", len(aliens))

# pizza = {"crust": "thick", "toppings": ["pepperoni", "extra cheese", "green peppers"]}

# print("You ordered a", pizza["crust"], "crust pizza along with the following toppings:")

# for topping in pizza["toppings"]:
#     print("\t" + topping)

# users = {"Mr.Einstein": {"first": "albert", "last": "Einstein"}, "Ms.Mcurie": {"first": "marie", "last": "curie"}}

# for username, userInfo in users.items():
#     print("\nUsername:", username)
#     print(userInfo["first"].title(), userInfo["last"].title())

# How user input works (Ch.7): ---------------------------------------------------------------------------------------------------

# message = input("Tell me your name:")
# print("Hello", message.title())

# age = int(input("How old are you?"))
# print(age>15)
# print("Your age mod 2 is:", (age % 2))
# if (age % 2 == 0):
#     print("Your age is even.")
# else:
#     print("Your age is odd.")

# While loops intro: -------------------------------------------------------------------------------------------------------------------

# curNum = 0
# while curNum < 5:
#     print(curNum)
#     curNum += 1

# promt = "\nSay something and I will make it uppercase:"
# promt += "\nEnter 'quit' to end the program."

# message = ""
# active = True

# while active:
#     message = input(promt)
#     if (message == "quit"):
#         active = False
#         break
#     print(message.upper())

# curNum = 0
# while curNum < 10: #Only prints odd nums and continues if num is even
#     curNum += 1
#     if curNum % 2 == 0:
#         continue
#     print (curNum)
    
# Using a while loop with lists and dictionaries: ---------------------------------------------------------------------

# unconfirmedUsers = ["alice", "brian", "josh"]
# confirmedUsers = []

# while unconfirmedUsers:
#     curUser = unconfirmedUsers.pop()

#     print("Verifying user:", curUser.title())
#     confirmedUsers.append(curUser)

# pets = ["dog", "cat", "fish", "dog", "cat", "rock", "cat"]
# print(pets)

# while "cat" in pets:
#     pets.remove("cat")
# print(pets)

# responses = {}

# isPolling = True

# while isPolling:
#     name = input("\nWhat is your name? ")
#     response = input("Which mountain would you like to climb someday? ")

#     responses[name] = response

#     repeat = input("Would you like to let another person response (yes / no) ")
#     if (repeat == "no"):
#         isPolling = False

# print("\n--- Poll Results ---")
# for name, response in responses.items():
#     print(f"{name.title()} would like to climb {response}.")

# Functions (Ch. 8): --------------------------------------------------------------------------------------------------------

# def greetUser(name):
#     """Display a simple greeting."""
#     print("Hello", name.title())

# greetUser("nico")

# Passing arguments: ----------------------------------------------------------------------------

# def describePet(animalTyp, petName): # You can set the default of value of animalTyp like (animalTyp="dog")
#     print("I have a", animalTyp)
#     print(f"My {animalTyp}'s name is {petName.title()}.")

# describePet("dog", "lobo") # You can also do (petName="lobo", animalTyp="dog") and it will output the same thing but idk why you would ever need that...
# describePet("cat", "tj")

# Return values: --------------------------------------------------------------------------------------------------------------------------------------------------

# def getFormattedName(first, last, middle=""): #This makes the middle name optional
#     if (middle):
#         fullName = f"{first} {middle} {last}"
#     else:
#         fullName = f"{first} {last}"
#     return fullName.title()

# while True:
#     print("\nWhat is your name?")
#     print("enter 'q' at anytime to quit")
#     first = input("First name: ")
#     if (first == "q"):
#         break;
#     last = input("Last name: ")
#     if (last == "q"):
#         break;
#     formattedName = getFormattedName(first, last)
#     print("\nHello,", formattedName)

# urName = getFormattedName("nick", "mendez", "jacob")
# print(urName)

# def buildPerson(first, last, age=None):
#     person = {"first": first, "last": last}
#     # if there was an age given assign it into the dictionary
#     if (age):
#         person["age"] = age
#     return person

# dude = buildPerson("jonathan", "joestar", 35)
# print(dude)

# Passing a list: -------------------------------------------------------------------------------

# def greetUsers(namesList):
#     for name in namesList:
#         msg = f"Hello, {name.title()}!"
#         print(msg)

# usernames = ["jasmine", "jenny", "nico", "willy", "willis"]
# greetUsers(usernames)

# unfinishedModels = ["web scraper", "key logger", "password cracker"]
# completedModels = []

# def makeModels(unfinishedList, completedList):
#     while unfinishedList:
#         curDesign = unfinishedList.pop()
#         print("Making current model, ", curDesign)
#         completedList.append(curDesign)

# def printCompleted(completedList):
#     print("\nThe following models have been completed:")
#     for completedM in completedList:
#         print(completedM)

# #If we didnt want to pop all the elements of unfinished models we can pass in a copy of the list like so (unfinishedModels[:])
# makeModels(unfinishedModels[:], completedModels) 
# printCompleted(completedModels)

# Passing an arbitrary number of arguments: ----------------------------------------------------------------------------------------------

# def makePizza(size, *toppings): # The * lets you pass in an arbitrary number of variables
#     print(f"\nYour {size}-in pizza has the following on it: ")
#     for topping in toppings:
#         print(f"- {topping}")

# makePizza(15, "pepperoni")
# makePizza(12, "mushrooms", "green peppers", "extra cheese")

# def buildProfile(first, last, **userInfo): # I think the double astriks means it creates an arbitrary dictionary that you can add to through the parameters
#     userInfo["firstName"] = first
#     userInfo["lastName"] = last
#     return userInfo

# userProfile = buildProfile("albert", "einstein", location="princeton", field="physics")
# print(userProfile)

# Storing your functions in modules: --------------------------------------------------------------------------------------------------------------------------------

# YOU just need to uncomment the line 406 function 

# Classes (Ch.9): --------------------------------------------------------------

# class Dog:
#     # A simple dog model

#     def __init__(self, name, age): # This exact format is very important to remember
#         self.name = name
#         self.age = age

#     def sit(self):
#         print(f"{self.name} is now sitting.")

#     def rollOver(self):
#         print(f"{self.name} rolled over!")

# myDog = Dog("Willy", 6)
# yourDog = Dog("Jill", 3)

# print("My dog's name is", myDog.name)
# print("My dog is", myDog.age, "years old.")
# myDog.sit()
# myDog.rollOver()

# print("Your dog's name is", yourDog.name, "and is", yourDog.age, "years old.")
# yourDog.sit()

# Working with classes and instances: ---------------------------------------------------------------

# class Car:

#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometerReading = 0
    
#     def getDescriptiveName(self):
#         longName = f"{self.year} {self.make} {self.model}"
#         return longName.title()
    
#     def readOdometer(self):
#         print("This car has", self.odometerReading, "miles on it.")

#     def updateOdometer(self, mileage):
#         if mileage >= self.odometerReading:
#             self.odometerReading = mileage
#         else: #Function only works if the mileage inputted is greater than the previous odometer reading
#             print("You can't roll back an odometer!")
    
#     def incrementOdometer(self, miles):
#         if ((miles + self.odometerReading) < self.odometerReading): # If you try to add a negative number make it not work
#             print("You can't roll back an odometer!!")
#         else:
#             self.odometerReading += miles

#     def fillGasTank(self, gas):
#         print(f"This car was filled with {gas} gallons of gas!")

# myNewCar = Car("Kia", "Forte", "2023")
# print(myNewCar.getDescriptiveName())
# myNewCar.odometerReading = 23
# myNewCar.readOdometer()
# myNewCar.updateOdometer(56)
# myNewCar.readOdometer()
# myNewCar.incrementOdometer(1000)
# myNewCar.readOdometer()
# myNewCar.incrementOdometer(-10)
# myNewCar.readOdometer()
# myNewCar.fillGasTank(50)

# Inheritance (Wow really?! I did not think it would get that far lol): ----------------------------------------------------------------------------------------------

# class ElectricCar(Car):
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         self.battery = Battery()

#     # DONT NEED THIS ANY MORE:
#     # def describeBattery(self): 
#     #     print(f"This car has a {self.batterySize}-kW battery.")

#     def fillGasTank(self): #This is overriding
#         print("This car doesn't need a gas tank!")

# # If you notice you are adding too many attributes to a class
# # sometimes it is useful to take some of the specific attributes
# # and give them their own class, like so:

# class Battery:
#     def __init__(self, batterySize=75):
#         self.batSize = batterySize

#     def describeBattery(self):
#         print(f"This car has a {self.batSize}-kWh battery.")

#     def getRange(self):
#         if self.batSize == 75:
#             range = 260
#         elif self.batSize == 100:
#             range = 315

#         print (f"This car can go about {range} miles on a full charge.")

# myTesla = ElectricCar("tesla", "model y", "2020")
# print(myTesla.getDescriptiveName())
# myTesla.battery.describeBattery()
# myTesla.fillGasTank()
# myTesla.battery.getRange()

# Importing classes: ---------------------------------------------------------------------------------------

# Uncomment car, electric car, and battery class and go to importning practice

# The python stadndard library: -----------------------------------------------------------------------------------

# from random import randint
# from random import choice

# print(randint(1, 6))

# players = ["charles", "martina", "micheal", "florence", "eli"]
# firstUp = choice(players)
# print(firstUp)

# Files and Exceptions (Ch.10): ----------------------------------------------------------------------------------

# with open("txtFiles/piDigits.txt") as fileObject:
#     contents = fileObject.read()
# print(contents)
# print(contents.strip())

# filename = "txtFiles/piDigits.txt"

# with open(filename) as fileObject:
#     for line in fileObject:
#         print(line.strip())

# with open(filename) as fileObject:
#     lines = fileObject.readlines()

# piString = ""
# for line in lines:
#     piString += line.strip()

# bday = input("Enter your birthday, in the form of mmddyy: ")
# if bday in piString:
#     print("Your birthday is in the first 32 digits of pi!")
# else: 
#     print("Your birthday is not in the first 32 digits of pi.")

# print(piString[:20])
# print(len(piString))

# Writing to a file: ---------------------------------------------------------------------------------------

# filename = "txtFiles/programming.txt" # You can write this to create a file at this locaiton to then write to

# with open(filename, "w") as fileObject: # The "w" tells python you want to open the file in write mode, there's also read mode("r"), append mode("a"), read and write("r+"), and if there is no argument then it goes to read-only mode 
#     # ***WARNING*** opening the file with write mode will erase any contents already on the file if the file already exists
#     fileObject.write("I love programming.\n")
#     fileObject.write("I love creating new games.\n")

# with open(filename, "a") as fileObject: # "a" will only append to a file instead of writing over it
#     fileObject.write("I also love finding meaning in large datasets.\n")
#     fileObject.write("I love creating apps that can run in a browser.\n")

# Exceptions: -----------------------------------------------------------------------------------------------------------------------------------

# firstNum = input("\nEnter 2 numbers and I'll divide them!, first number: ")
# secondNum = input("Second number: ")
# try:
#     answer = int(firstNum) / int(secondNum)
# except ZeroDivisionError:
#     print("You can't divide by zero!")
# else:
#     print(answer)

# def countWords(filename):
#     try:
#         with open(filename, encoding="utf-8") as f:
#             contents = f.read() # Reads the contents into the variable "contents" which I believe is a string of everything in the file 
#     except FileNotFoundError:
#         print(f"Sorry, the file {filename} does not exist.")
#         # You can also just type 
#         # pass
#         # which will simply tell python to do nothing
#     else:
#         words = contents.split() # Splits every word in the string into different values in a list
#         numWords = len(words)
#         print(f"The file {filename} has about {numWords} words.")

# filenames = ["txtFiles/alice.txt", "txtFiles/piDigits.txt", "txtFiles/programming.txt", "littleWomen.txt"]
# for filename in filenames:
#     countWords(filename)

# Storing Data: --------------------------------------------------------------------------------------------------------

# import json

# numbers = [2, 3, 5, 7, 11, 13]

# filename = "jsonFiles/numbers.json"

# with open(filename, "w") as f:
#     json.dump(numbers, f)

# with open(filename) as f:
#     newNumbers = json.load(f)
# print(newNumbers)

# def greetUser():
#     username = getStoredUsername()
#     if username: # If username is None it will be false otherwise it will return true
#         print(f"Welcome back, {username}")
#     else: 
#         username = getNewUsername()
#         print(f"We'll remember you when you come back, {username}")
# def getStoredUsername():
#     filename = "jsonFiles/username.json"
#     try:
#         with open(filename) as f:
#             username = json.load(f)
#     except FileNotFoundError:
#         return None
#     else:
#         return username

# def getNewUsername():
#     username = input("What is your name?")
#     filename = "jsonFiles/username.json"
#     with open(filename, "w") as f:
#             json.dump(username, f)
#     return username

# greetUser()

# Testing your code (Ch. 11): -------------------------------------------------------------------------------------

# def getFormattedName(first, last, middle=""):
#     if middle:
#         fullName = f"{first} {middle} {last}"
#     else:
#         fullName = f"{first} {last}"
#     return fullName.title()

# Testing a class: ----------------------------------------------------------------------------------

# class AnonymousSurvey:
#     def __init__(self, question):
#         self.question = question
#         self.responses = []
    
#     def showQuestions(self):
#         print(self.quesiton)

#     def storeResponse(self, newResponse):
#         self.responses.append(newResponse)

#     def showResults(self):
#         print("Survey results:")
#         for response in self.responses:
#             print(f"- {response}")






