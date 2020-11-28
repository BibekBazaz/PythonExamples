# Dictionary are key value pairs in python with keys being unique in a dictionary.
# Any immutabnle type can eb a string for example strings, numbers or tuples containing only string, numbers

# 1. Declare a Dictionary
# 1.1 normal key value pair declaration
sample_dict_num = {1:'one',2:'two',3:'three'}
sample_dict_str = {'key_1':"apple",'key_2':"banana",'key_3':"orange"}
print("Normal key value declaration")
print(sample_dict_num)
print(sample_dict_str)

# 1.2 Creating dictionary using list of tuples ;  dict() gives {}
print("Creating list using array of tuples")
sequence = [(1,'assam'),('key_1','demow')]
sample_dict_dict = dict(sequence)
print(sample_dict_dict)

# 1.3 dict comprehensions
print("Using comprehensions")
dict_comprehension = {x:x**3 for x in range(6)}
print(dict_comprehension)

# 1.4 Creating dictionary passing parameters to dict()
print("Creating dictionary passing parameters to dict()")
print(dict(sape=4139, guido=4127, jack=4098))

# 1.5 Creating dictionary using a list of keys with initialization to same value
var = [1,2,3,4,5,6]
print("Creating a dictionary from a list of keys, all keys will be initialized to 0")
print(dict.fromkeys(var))

# 1.6 Creating a dictionary by two lists
list_1 = [1,2,3,4,5,6,7,8,9,0]
list_2 = ['one','two','three','four','five','six','seven','eight','nine','ten']
dict_merge_list = dict(zip(list_2,list_1))
print("Created dictionary by merging two lists : ")
print(dict_merge_list)

print("-*-"*20)

# 2. Printing dictionaries
print("Printing dictionaries")

#2.1 Using for loop and items
print("Using for loop and items")
for key,value in sample_dict_str.items() :
    print(key,':',value)

# 2.2 iterating over keys
print("Printing dictionary by iterating over key")
for key in sample_dict_dict :
    print(key,':',sample_dict_dict[key])

# 2.3 Using List comprehensions
print("Using List comprehensions")
[print(key,value) for key,value in sample_dict_num.items()]


# 3. Adding elements to a Dictionary
# 3.1 Adding elemnts one at a time
sampleDict = {0:'zero',1:'one',2:'two'}
print(sampleDict)
print("Adding elemnts one at a time")
sampleDict[3] = 'three'
print(sampleDict)

# 3.2 Adding multiple elements at a time
print("Adding multiple elements at a time")
morePairs= {4:'four',5:'five'}
sampleDict.update(morePairs)
print(sampleDict)

# 3.3 update existing key value pair
print("update existing key value pair")
sampleDict.update({4:'updatedFour'})
print(sampleDict)

# 4. Deleting items from a dictionary
print("To remove items from a dictonary, we can use del, pop, popitem and clear ")
