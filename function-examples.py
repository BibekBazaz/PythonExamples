#This is a Python function example

#Required Parameters
def printStringWithBaner(sampleInput) :
    lengthOfInput = len(sampleInput)
    finalString = ("*" * lengthOfInput) + "\n" + sampleInput + "\n" +  ("*" * lengthOfInput)
    print(finalString)

var = input("Required Parameters Function \n Enter your String : \t ")
printStringWithBaner(var)

#Default Parameters
def calculateAreaOfCircle(radius, pi=3.14):
    print("Area of a circle is : " + str(pi*(int(radius)**2)))

var = input("Default parameter example : Enter the radius of a circle : ")
calculateAreaOfCircle(var)

#Keyword Parameter
def printDetails(name,age,gender):
    var = "Name : " + name + " age: " +age +" Gender : " + gender
    printStringWithBaner(var)

name=input("Enter name : ")
age=input("Enter age : ")
gender=input("Enter gender : " )

printDetails(gender=gender,name=name,age=age)

#Lambda Examples
print("Lambda method example")
square= lambda x : x**2
print("Squaring with lamdas : " + str(square(11)))
