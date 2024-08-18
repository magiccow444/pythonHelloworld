# from helloWorld import makePizza # and you can do , more funcions, and even more
# import helloWorld
# import helloWorld as hW
# from helloWorld import makePizza as mP # you can rename functions from other files
# from helloWorld import * # This imports all the functions from helloWorld

# makePizza(16, "pepperoni") # from line 1 and can be done with line 5 too
# helloWorld.makePizza(12, "mushroom", "green pepper", "extra cheese") # from line 2
# hW.makePizza(10, "idk", "idek") # from line 3
# mP(13, "olives", "spinach") # from line 4

# ----------------------------------------------------

# from helloWorld import Car 
# from helloWorld import ElectricCar
# from helloWorld import Car, ElectricCar
# import helloWorld # JUST a tip you can also import classes with aliases just like with functions
# from helloWorld import *

# myNewCar = Car("kia", "forte", "2023")
# print(myNewCar.getDescriptiveName())

# myTesla = ElectricCar("tesla", "model y", "2020")

# myNewCar.odometerReading = 23
# myNewCar.readOdometer()

# print(myTesla.getDescriptiveName())
# myTesla.battery.describeBattery()
# myTesla.battery.getRange()

# class RaceCar(Car): -- Just showing how you can import a class and then use it as a parent
#     def blah blah blah

# --------------------------------------------------------------------------------

# import unittest

# from helloWorld import getFormattedName

# print("Enter q at anytime to quit.")
# while True:
#     first = input("\nPlease give me a first name:")
#     if first == "q":
#         break
#     last = input("Please give me a last name:")
#     if last == "q":
#         break

#     formattedName = getFormattedName(first, last)
#     print(formattedName)

# class NamesTestCase(unittest.TestCase): # This functions needs to inherit the "unittest.TestCase" so python knows how to run the tests you write
#     def testFirstLastName(self):
#         formattedName = getFormattedName("janis", "joplin")
#         self.assertEqual(formattedName, "Janis Joplin") # "assertEqual" basically compares your output with what you think you should get and then tells you if they match or not
#     def testFirstLastMiddleName(self):
#         formattedName = getFormattedName("wolfgang", "mozart", "amadeus")
#         self.assertEqual(formattedName, "Wolfgang Amadeus Mozart")

# So I think what this does is when the program is run as the main file its "__name__" variable is changed to "__main__" 
# so then we check if it is the main file being run we should call "unittest.main()" which will run the test cases.
# if __name__ == "__main__":
#     unittest.main()

# ----------------------------------------------------------------------------------------------------------------------------------------------------

# import unittest

# from helloWorld import AnonymousSurvey

# question = "What language did you first learn to speak?"
# mySurvey = AnonymousSurvey(question)

# print ("Enter 'q' at any time to quit.")
# while True:
#     response = input("Language: ")
#     if response == "q":
#         break
#     mySurvey.storeResponse(response)

# print("Thank you to everyone who participated in the survey!")
# mySurvey.showResults()

# class TestAnonymousSurvey(unittest.TestCase):
#     def setUp(self):
#         question = "What language did you first learn to speak?"
#         self.mySurvey = AnonymousSurvey(question)
#         self.responses = ["Enlish", "Spanish", "Mandarin"]

#     def testStoreSingleResponse(self):
#         question = "What a language did you first learn to speak?"
#         mySurvey = AnonymousSurvey(question)
#         mySurvey.storeResponse(self.responses[0])
#         self.assertIn(self.responses[0], mySurvey.responses)

#     def testStoreThreeResponses(self):
#         question = "What language did you first learn to speak?"
#         mySurvey = AnonymousSurvey(question)
#         responses = ["English", "Spanish", "Mandarin"]
#         for response in responses:
#             mySurvey.storeResponse(response)
            
#         for response in responses:
#             self.assertIn(response, mySurvey.responses)

# if __name__ == "__main__":
#     unittest.main()

