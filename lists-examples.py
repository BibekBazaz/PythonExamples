#This python script will contain all the examples of lists in python

# 1. List Declaration
listSample_1 = []
listSample_2 = ["qwerty","apple","banana","orange","mango","strawberry"]
listSample_3 = ["stringExample",1,1.2,1+2j,True,("Bibek",28,36.5)]

# 2. list iteration
# 2.1 Using iterator
print("List Iteration using iterator\n")
list_iterator = iter(listSample_3)
position = 0
while(True):
    try:
        var = next(list_iterator)
        print("Heterogenous List Item Number " + str(position+1) +
    " : " + str(var) + " having type : " + str(type(var)) +"\n")
        position+=1
    except StopIteration :
        print("Reached end of list")
        break

# 2.2 using for
print("List iteration using for")
position = 0
for i in listSample_3:
    print("Heterogenous List Item Number " + str(position+1) +
" : " + str(i) + " having type : " + str(type(i)) +"\n")
    position+=1

# 2.3 using [:]
print("List iteration using [:]")
position = 0
print(listSample_3[:])

print("End of iteration examples \n " + "---"*29)

# 3. Appending Data to Lists
print("Empty List  : ")
print(listSample_1)
# 3.1 append()
print("Appending APPLE to list using append() method. Result :  ")
listSample_1.append("APPLE")
print(listSample_1)
print("Appending 1+220j to list using insert method at index 0. Result :  ")
# 3.2 insert()
listSample_1.insert(0,1+220j)
print(listSample_1)
# 3.3. extend()
print("Combining two lists using extend method. [1,2,3,4] Result :  ")
listSample_1.extend([1,2,3,4])
print(listSample_1)
# 3.4 using +
print("using the + opeartor to concatenate lists [1,2,3,4,5] and [6,7,8,9,0] : " )
print([1,2,3,4,5] + [6,7,8,9,0])

print("End of Adding data to lists examples \n " + "---"*29)

# 4. Printing Arrays
# 4.1 using for loop
print("Printing list using for loop")
for x in listSample_3:
    print(x)

# 4.2 using * and sep
print("Printing list using * and sep")
print(*listSample_3, sep=",")
print(*listSample_3, sep="\t")

# 4.3 converting list to string and printing
print("Converting a list containing only strings to one string using join method  ")
print(' '.join(listSample_2))

print("Converting a list of string and integers to one string ")
var = [1,2,3,4,5,"string sample",1+2j,(1,2,3,"qerty")]
print('list as string : ' + str(var[:]))


#4.4 using map() method
print("We will see the map method later when we learn lambdas")

# 5.Other important methods of lists
print("Other important methods")

# 5.1 clear()
print("Before clearing listSample_1 : " + str(listSample_1[:]))
listSample_1.clear()
print("After clearing listSample_1 : " + str(listSample_1[:]))

# 5.2 pop method
print("Before popping qwerty listSample_2 : " + str(listSample_2[:]))
listSample_2.pop(0)
print("After popping qwerty listSample_2 : " + str(listSample_2[:]))

# 5.3 sum(), count(), index(), min(), max(),len(),reverse(),sort(),del(),remove()
var = [1,2,34,56,6,7,88,8,54,3,2,5,-9,-4,-3]
print("Sum : "  + str(sum(var)))
print("Count of 2 : "  + str(var.count(2)))
print("Index of 88 : " + str(var.index(88)))
print("Length of list  " + str(len(var)))
print("Min of list : " + str(min(var)))
print("Max of list is : " + str(max(var)))
var.reverse()
print("Reverse the list : " + str(var[:]))
var.sort(reverse=True)
print("Sort in descending : " + str(var[:]))
print("Delete an element using list name and index for example at 8th position: " )
del var[8]
print(var[:])
print("Remove element using list name and elment : " )
var.remove(2)
print(var[:])
