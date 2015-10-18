""" Assume that we execute the following statements
width= 17
height=12.0
delimiter='.'

for each of the expressions below write down the expression and the type

1. width/2
2. width/2.0
3. height/3
4. 1+2*5
5. delimiter*5
"""
width= 17
height=12.0
delimiter='.'

#1. Width /2 should give an integer value of 8.5-float
first=width/2
print (first)
print(type(first))

#Width /2.0 should give an integer value of 8.5-float
second=width/2.0
print(second)
print(type(second))

#height/3 should give 4.0 as float
third=height/3
print(third)
print(type(third))

# Printing a simple mathematical expression will give an int value
maths= 1+2*5
print(maths)
print(type(maths))

#delimiter*5 will print the delimiter five times and the type will be string
print(delimiter*5)
FiveDelimiter=delimiter*5
print(type(FiveDelimiter))
