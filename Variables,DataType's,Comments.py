print('\nVariable diclaration and Printing')

x = 5       # x is a variable and of type int
y = "John"      # y is a variable and of type string
print(x)
print(y)
print('---------------x--------------x------------')

# If you want to specify the data type of a variable, this can be done with casting.

print('\nTo specify the data type of a variable')

a = str(3)        # a will be '3'
b = int(3)        # b will be 3
c = float(3)      # c will be 3.0

print( 'a=',a,'\nb=',b,'\nc=',c)

print('---------------x--------------x------------')

#you can get the data type of a variable with the type() function.

print('\nGet the data type of a variable with the type() function.')

print(type(a)) 
print(type(b))
print(type(c))
print('---------------x--------------x------------')

#Python allows you to assign values to multiple variables in one line:

print("\nPython allows you to assign values to multiple variables in one line:")

d, e, f = "Orange", "Banana", "Cherry"

print(d)
print(e)
print(f)
print('---------------x--------------x------------')

print("\nif you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.")

fruits = ["apple", "banana", "cherry"] # give list as a value

x, y, z = fruits
print(x)
print(y)
print(z)

print('---------------x--------------x------------')
 
#Create a variable outside of a function, and use it inside the function

print('\nCreate a variable outside of a function, and use it inside the function')

x = "awesome"

def myfunc():
  print("\nPython is " + x)

myfunc()


#Create a variable inside a function, with the same name as the global variable

print('\nCreate a variable inside a function, with the same name as the global variable')

x = "awesome"

def myfunc():
  x = "fantastic"
  print("\nPython is " + x)

myfunc()

print("Python is " + x)

print('---------------x--------------x------------')

# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

print('\nIn Python, the data type is set when you assign a value to a variable:')

x = "Hello World"	# data type is String
print('\nx is "x = "Hello World"" and of data Type:', type(x))

x = 20 	# data type	is int.
print('\nx is "x = 20" and of data Type:', type(x))

x = 20.5	# data type is float.
print('\nx is "x = 20.5" and of data Type:', type(x))

x = 1j		# data type is complex.
print('\nx is "x = 1j" and of data Type:', type(x))

x = ["apple", "banana", "cherry"]		# data type is list.
print('\nx is "x = ["apple", "banana", "cherry"]"	and of data Type:', type(x))

x = ("apple", "banana", "cherry")		# data type is tuple.
print('\nx is "x = ("apple", "banana", "cherry")" and of data Type:', type(x))

x = range(6)	# data type is range.
print('\nx is "x = range(6)" and of data Type:', type(x))

x = {"name" : "John", "age" : 36}	# data type is dict.
print('\nx is "x = {"name" : "John", "age" : 36}" and of data Type:', type(x))

x = {"apple", "banana", "cherry"}	# data type is set.
print('\nx is "x = {"apple", "banana", "cherry"}" and of data Type:', type(x))

x = frozenset({"apple", "banana", "cherry"}) # data type is frozenset.
print('\nx is "x = ({"apple", "banana", "cherry"})" and of data Type:', type(x))

x = True		# data type is bool.
print('\nx is "x = True" and of data Type:', type(x))

x = b"Hello"		# data type is bytes.
print('\nx is "x = b"Hello"" and of data Type:', type(x))

x = bytearray(5)		# data type is bytearray.
print('\nx is "x = bytearray(5)" and of data Type:', type(x))

x = memoryview(bytes(5))		# data type is memoryview.
print('\nx is "x = memoryview(bytes(5))" and of data Type:', type(x))

x = None		# data type is NoneType.
print('\nx is "x = None" and of data Type:', type(x))

print('---------------x--------------x------------')

