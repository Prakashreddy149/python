# ------ Syntax -------

# print(object(s), sep=separator, end=end, file=file, flush=flush)

# ------ Parameter Values -------

#object(s)	Any object, and as many as you like. Will be converted to string before printed

#sep='separator'	Optional. Specify how to separate the objects, if there is more than one. Default is ' '

#end='end'	Optional. Specify what to print at the end. Default is '\n' (line feed)

#file	Optional. An object with a write method. Default is sys.stdout

#flush	Optional. A Boolean, specifying if the output is flushed (True) or buffered (False). Default is False


# ------------- Example -------------

# Print more than one object:

print("Hello", "how are you?")
print('---------------x--------------x------------')

# Print a tuple:

x = ("apple", "banana", "cherry")
print(x)
print('---------------x--------------x------------')

# Print two messages, and specify the separator:

print('Print two messages, and specify the separator:')
print("Hello", "how are you?", sep="---")
print('---------------x--------------x------------')

# Print two messages, and specify the separator:

print('Print two messages, and specify the separator:')
print("Hello", "how are you?", sep="\n")  
# """hear separator is \n so it will be printed in next line."""
print('---------------x--------------x------------')

# Changing the Default value of end: 
print('Changing the Default value of end:')
print('rahul', 23, end=" ")
print('ram', 21)
print('---------------x--------------x------------')

# Changing the Default value of End and Separator: 
print('Changing the Default value of end and Separator:')
print('rahul', 23, sep='\n', end="->")
print('ram', 21)
print('---------------x--------------x------------')
