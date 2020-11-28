import sys
inputList=[]

while(True):
    print("1.Addition\n 2.Subtraction\n 3.Multiplication\n 4.Division\n 5.Sum of squares\n 6.Advanced Menu")
    operation_choosen = int(input("Choose Operation : "))
    if(operation_choosen >0 and operation_choosen<6):
            num_1 = int(input("Enter First Number"))
            num_2 = int(input("Enter second number"))
    if(operation_choosen == 1) : print("Addition : " + str(num_1+num_2))
    elif(operation_choosen == 2) : print("Subtraction : " + str(num_1 - num_2))
    elif(operation_choosen == 3) : print("Multiplication : " + str(num_1*num_2))
    elif(operation_choosen == 4) : print("Division : " + str(num_1/num_2))
    elif(operation_choosen == 5) :
        print("Sum of squares : " + str(num_1**2 + num_2**2))
    elif(operation_choosen == 6):
        mapOfOperations={7:'squares of list',8:'cube'}
        print(mapOfOperations)
        operation_choosen = int(input("Choose advanced option"))
        if(operation_choosen==7):
            print("Enter a list of 5 numbers")
            for i in range(5) :
                inputList.append(int(input("Enter the number for position " + str(i) + " : ")))
            list_iterator = iter(inputList)
            while True :
                try:
                    print(str(next(list_iterator)**2))
                except StopIteration:
                    inputList.clear()
                    break
        elif(operation_choosen==8):
            print("Enter a list of 5 numbers")
            for i in range(5) :
                inputList.append(int(input("Enter the number for position " + str(i) + " : ")))
            for i in inputList :
                print(str(i**3))
            inputList.clear()
    else :
        print("Wrong Operation : " + str(operation_choosen))

    isContinue = input("To continue press Y else press N : ")
    if(isContinue=='N'):
        print("End of Program")
        sys.exit(0)
