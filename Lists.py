#Lists are used to store multiple items in a single variable.

#Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

mylist = ["apple", "banana", "cherry"]   # list syntax
print("\n",mylist)   # printing the list "mylist"
print("-----------x-----------x------------\n")
# List items are ordered, changeable, and allow duplicate values. 

# Indexed: List items are indexed, the first item has index [0], the second item has index [1] etc.

# Ordered: In lists items have defined order, and that will not change when you add or remove items.

# If you add new items to a list, the new items will be placed at the end of the list.

# Changeable: In lists items can be added, removed and changed after they have been created.

# Duplicates are allowed since each and every item in the list have indexes.


thislist = ["apple","banana", "orange", "apple", "pineapple"]
print("\n",thislist)
print("-----------x-----------x------------\n")


# List Length
# To determine how many items a list has, use the len() function:

print("\nlength of the list mylist = ",len(mylist),"\nmylist = ", mylist) # mylist is declared at the start.
print("-----------x-----------x------------\n")

# List Items and its Data Types
# String, int and boolean data types:

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print('\nlist1 = ', list1, '\n\n','list2 = ', list2, '\n\n','list3 = ', list3)   # printing multiple lists
print("-----------x-----------x------------\n")

# List items can be of different data types.
list4 = ["abc", 34, True, 40, "male"]
print("List with multiple Data Types =",list4)
print("-----------x-----------x------------\n")

# type()
# The type() function returns the data type of the specified object.

print(type(list4))
print("-----------x-----------x------------\n")

# using list() to declare a list.
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
print("-----------x-----------x------------\n")

# Access Items
# List Items - Accessing List Items
# List items are indexed, the first item has index [0], the second item has index [1] etc.
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Negative Indexing
# Negative indexing is a way to access the items of a list in reverse order.
# The last item has index -1, the second last item has index -2, etc.
# Example_1:
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
print("-----------x-----------x------------\n")

# Range of Indexes
# Range of Indexes - Accessing List Items
# To access all items in a list, use the range() function:  
thislist = ["apple", "banana", "cherry"]
print(thislist[0:2])

# Example_2:
list5 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list5[2:5])

# Example_3;
# This example returns the items from the beginning to, but NOT including, "kiwi":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

# Example_4:
# By leaving out the end value, the range will go on to the end of the list:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

# Example_5:
# This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

print("-----------x-----------x------------\n")

# Check if Item Exists
# To determine if a specified item is present in a list use the 'in' keyword:

# Check if "apple" is present in the list:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
print("-----------x-----------x------------\n")

# Change Item Value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

print("-----------x-----------x------------\n")

# Change a Range of Item Values
# To change a range of items in a list, use the range() function:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist[2:5] = ["blackcurrant", "watermelon", "pineapple"]
print(thislist)

print("-----------x-----------x------------\n")

# Insert Items
# To insert a list item at a specified index, use the insert() method.
# Example_1:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
print("-----------x-----------x------------\n")

# Append Items:
# To add an item to the end of a list, use the append() function. 
# Example_1:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
print("-----------x-----------x------------\n")

# Add Any Iterable
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

# Example_1:
# Add elements of a tuple to a list:

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
print("-----------x-----------x------------\n")

# Remove "banana":

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
print("-----------x-----------x------------\n")

#If there are more than one item with the specified value, the remove() method removes the first occurance:

# Example_1
#Remove the first occurance of "banana":

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
print("-----------x-----------x------------\n")

# Remove Items with the pop() Method:
# The pop() method removes the last item from a list.
# Example_1:
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
print("-----------x-----------x------------\n")

# If you do not specify the index, the pop() method removes the last item.
# Remove the last item:

# Example_2:


thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
print("-----------x-----------x------------\n")

# Remove Items with the del Keyword:
# The del keyword removes the specified index:
# Example_1:
thislist = ["apple", "banana", "cherry"]
del thislist[1]
print(thislist)

# Delete the entire list:

thislist = ["apple", "banana", "cherry"]
del thislist
print("-----------x-----------x------------\n")

# Clear the list content:

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
print("-----------x-----------x------------\n")

#Print all items, using a while loop to go through all the index numbers

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

print("-----------x-----------x------------\n")

# A short hand for loop that will print all items in a list:

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

print("-----------x-----------x------------\n")

# Without list comprehension you will have to write a for statement with a conditional test inside:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# With list comprehension you can do all that with only one line of code:

# Example_1
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

print("-----------x-----------x------------\n")

# The Syntax

# {newlist = [expression for item in iterable if condition == True]}

# The return value is a new list, leaving the old list unchanged.
# Condition
# The condition is like a filter that only accepts the items that valuate to True.

# Example_1
# Only accept items that are not "apple":

newlist = [x for x in fruits if x != "apple"]




"""
==========================
Output
==========================
['apple', 'banana', 'cherry']
-----------x-----------x------------


 ['apple', 'banana', 'orange', 'apple', 'pineapple']
-----------x-----------x------------


length of the list mylist =  3 
mylist =  ['apple', 'banana', 'cherry']
-----------x-----------x------------


list1 =  ['apple', 'banana', 'cherry'] 

 list2 =  [1, 5, 7, 9, 3] 

 list3 =  [True, False, False]
-----------x-----------x------------

List with multiple Data Types = ['abc', 34, True, 40, 'male']
-----------x-----------x------------

<class 'list'>
-----------x-----------x------------

['apple', 'banana', 'cherry']
-----------x-----------x------------

banana
cherry
-----------x-----------x------------

['apple', 'banana']
['cherry', 'orange', 'kiwi']
['apple', 'banana', 'cherry', 'orange']
['cherry', 'orange', 'kiwi', 'melon', 'mango']
['orange', 'kiwi', 'melon']
-----------x-----------x------------

Yes, 'apple' is in the fruits list
-----------x-----------x------------

['apple', 'blackcurrant', 'cherry']
-----------x-----------x------------

['apple', 'banana', 'blackcurrant', 'watermelon', 'pineapple', 'melon', 'mango']
-----------x-----------x------------

['apple', 'banana', 'watermelon', 'cherry']
-----------x-----------x------------

['apple', 'banana', 'cherry', 'orange']
-----------x-----------x------------

['apple', 'banana', 'cherry', 'kiwi', 'orange']
-----------x-----------x------------

['apple', 'cherry']
-----------x-----------x------------

['apple', 'cherry', 'banana', 'kiwi']
-----------x-----------x------------

['apple', 'cherry']
-----------x-----------x------------

['apple', 'banana']
-----------x-----------x------------

['apple', 'cherry']
-----------x-----------x------------

[]
-----------x-----------x------------

apple
banana
cherry
-----------x-----------x------------

apple
banana
cherry
-----------x-----------x------------

['apple', 'banana', 'mango']
['apple', 'banana', 'mango']
-----------x-----------x------------
"""
