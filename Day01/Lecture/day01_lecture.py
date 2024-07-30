# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.3
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# #### Data Structures

# ##### Part 2: Syntax, Loops, and Functions
#
# Types of Objects: 
# 1. Variable: A simple object, for example, `a = 1`
# 2. List: [], A list is a collection of objects which is ordered and mutable 
# 3. Tuple: (), A tuple is a collection of objects which is ordered and immutable
# 4. Dictionary: {}, A dictionary is a collection which is unordered, changeable and indexed objects

# Operators: 
# - Addition					x `+` y
# - Subtraction				x `-` y	
# - Multiplication			x `*` y	
# - Division					x `/` y	
# - Modulus					x `%` y	
# - Exponentiation  			x `**` y	
# - Floor division			x `//` y
# - Equal						x `==` y	
# - Not equal					x `!=` y	
# - Greater than				x `>` y	
# - Less than					x `<` y	
# - Greater than or equal to	x `>=` y	
# - Less than or equal to		x `<=` y
#
# - `and`, Returns True if both statements are true
# - `or`, Returns True if one of the statements is true
# - `not`, Reverse the result, returns False if the result is true
# - `is`, Returns True if both variables are the same object
# - `in`, Returns True if a sequence with the specified value is present in the object
#
# <br>
#
# Tips: 
# - Be careful! Python is case-sensitive!
# - See https://www.w3schools.com/python/python_operators.asp for a complete list.

# #### 2.1 Data Type: Strings

# Single Quotes
name = 'Cecilia'

# Double Quotes 
# Can only use double quotes for strings that contain single quote characters 
age = "24"

# Combining strings, using .format{}
intro =  "Hi, my name is {}. I'm {} years old.".format(name, age)

# Combining strings, using +
intro = "Hi, I'm " + name + ", I'm " + age

# Triple Quotes, it produces a string that spans multiple lines
new_intro = """Hello!,
I'm Alma. 
What's up?"""
print(new_intro)
# new_intro

# Characters in a string are indexable
intro

intro[0] # Indexing starts at 0! not 1! 
# intro[3]

# +
# Strings are immutable, we cannot replace a character in a string
# intro[0] = "a"
# -

# But, we can use a string to modify itself
intro = intro + ". I'm from China."
intro

# We can also use +=
name += ' Sui' # same as name = name + ' Sui'
name

# Though strings are immutable, we can split them
name.split() # Using ' ' as the default separator

# We can use any separator
name.split(sep = 'i')
# new_intro.split('\n') ## Using line break as separator

# +
# We can index using negative numbers 
wustl = 'WashingtonUniversity'
wustl[-1] 

# Check how the characters are positioned...
#  0   1   2   3   4   5   6   7   8   9  10 11 12 13 14 15 16 17 18 19
#  W   a   s   h   i   n   g   t   o   n   U  n  i  v  e  r  s  i  t  y
#-20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
# Notice that W is 0, but y is -1
# -

# We can recover multiple characters from a string:
wustl[2:] ## index 2 through end

wustl[-2:] ## index -2 through end

wustl[:2] ## up to index 2, NOT inclusive at the index

wustl[:-2] # up to index -2

wustl[1:8] # sequence, from index 1 to 7, 
# remember: Python indexes are n through i exclusive; we drop the 'W' (index 0) and do not include 'o' (index 8)

wustl[::2] ## sequence, every other

wustl[::-1] ## sequence, reverse the string

# We can use a loop to split a string into characters
[letter for letter in wustl] # the output is a list, more on this below

# We can join strings in a list using join
wustl_chr = [letter for letter in wustl] 
# wustl_chr
'-'.join(wustl_chr) # the output is a string

# #### 2.2 Data Type: Integers

# We can use all mathematical operators with them
# Integers are not rounded down in Python 3
3/2 # result is a float not integer 
# type(3/2)

whole = 5//3
whole

remainder = 5 % 3
remainder

# these two formats are similar, however, format is more flexible in many instances 
print('This will print both a string: a name {} and a number: {}'.format(name, whole))
print('This will print both a string: a name %s and a number: %d' % (name, whole))
# print('This will cause an error: %d, %d' % (name, whole))

# As with strings, the assignment is flexible
five = 5

five += 1

five /= 3

five -= 1

five *= 2

five

type(five)

# #### 2.3 Data Type: Float 

# Real numbers
# Add decimal to integer
# type(12) # integer
type(12.0) # float

# In Python 3, these are equal. 
12/5 == 12.0/5

12 == 12.0
# type(12) is type(12.0)

# #### 2.4 Data Type: List

# +
# A list is a collection of objects which is ordered and mutable 
# Lists can be changed
# Lists can include multiple object types
# Lists will probably be your go-to storage in Python
# Similar to vectors in R, but more flexible
# -

wustl_chr 
# type(wustl_chr)

# We can add a new element to a list using the method append()
wustl_chr.append('P')
wustl_chr

# Lists can include multiple types of objects
wustl_chr.append(1)
wustl_chr.append(['1'])
wustl_chr

# We can index lists
# wustl_chr[0]
# wustl_chr[-1][0]
wustl_chr[:2]

# We can also replace objects in a list
wustl_chr[0] = 'X'
wustl_chr

# We can use len() to get the length of a list
len(wustl_chr)

# But, be careful because indexing starts at 0
# print(wustl_chr[len(wustl_chr)]) # IndexError
print(wustl_chr[len(wustl_chr) - 1]) # Return the object at the last index

# We can insert into any position using the method inset()
wustl_chr.insert(5, "!")
wustl_chr

# We can also remove from any position
wustl_chr.pop(1)
wustl_chr

# We can remove the object at the last index using 
wustl_chr.pop()
wustl_chr

# We can also remove using a value with the method remove()
# but notice, this removes the first instance
wustl_chr.remove('n')
wustl_chr 

# We can remove all instances from a list using list syntax
# More on this later
wustl_chr = [i for i in wustl_chr if i != 'i']
wustl_chr

# We can check all the methods and attributes in a list using
dir(wustl_chr)

# #### 2.5 Data Type: Tuples

l = [7, 'a', '6']
type(l)
l

l2 = (7, 'a', '6')
type(l2)
l2

# +
# Tuple: (), A tuple is a collection of objects which is ordered and immutable 
# Not very common, but useful occasionally and will appear from time to time

# We use () to create a tuple
tup = (1, 'a', 'a', 11, 6, 5, 'Apple', ['python', 'R'])
# -

tup[1]
# tup[1] = 'b'

# Let's check the methods available for tuples
dir(tup)

# #### 2.6 Data Type: Dictionary

# +
# A dictionary is a collection which is unordered, changeable and indexed 

# We use {} to create a dictionary
myInfo = {"name" : "Cecilia", "age" : 24, "research" : ["Methods", "American"]}
myInfo
# -

# myInfo.keys() # return the dictionary's key
myInfo.values() # return the dictionary's value

# +
# myInfo[0] # We cannot use index

# We can call entries by key
myInfo["name"]
# -

# We can add new elements to a dictionary
myInfo["last_name"] = "Sui"
myInfo

# We can modify elements
myInfo["name"] = 'Yuan'
myInfo["research"] = 'Methods'
myInfo

# #### 2.7 Data Type: Booleans & Conditionals

# +
# Perform an operation (or several) if condition is met (or not)
x = 1

if x == 1:
	print('x is one')
elif x == 2:
	print('x is two')
else:
	print('x is neither one nor two')
	

# +
# # Multiple lines of code:
# # - Indentation matters!
# # - Even an empty line with spaces can cause errors, 
# #   Python is very picky about this
# if x == 1:
# 	print('x is one')
# elif x == 2:
# 	print('x is two')
# else:
# print('x is neither one nor two') # IndentationError
# -

# Can be conditions or boolean (True or False)
True == (1 == 1.0) 
# TRUE == (1 == 1.0)  # Be careful, case sensitive. TRUE does not work

True == 1
# False == 0

# #### 2.8 Data Type: Loops

# +
# Two types of loops: for and while
# for loop: loops over iterable objects
# while loop: runs until condition is met 

# A string is an iterable object
for i in wustl:
	print(i)
# -

# We can iterate over a dictionary items in Python 3
for i in myInfo: # .items(): # .keys(): # .values(): 
	print(i) # Tuples!

# We can unpack the elements of a dictionary
for k, v in myInfo.items():
	print(k, '->', v) # What does this do? 

# Sometimes is useful to write a short version of the for loop
sum([.05**i for i in range(1,10)]) # What is happening here?

mynum = [] # instantiate an empty list
for i in range(1,10):
	mynum.append(.05**i)
# mynum
sum(mynum) # Sum the values in the list

sum(mynum) == sum([.05**i for i in range(1,10)])

# While loop: loops while condition is true
while len(wustl_chr) > 1:
	wustl_chr.pop()
# What happened to wustl_chr?
wustl_chr 

# +
# # Be careful with while loops, they can go forever
# # in ipython or terminal, stop with 'control + c'
# while True:
# 	print(i)
# -

# Useful statements when using loops:
# break: stop the loop and go to the previous level
for i in range(1, 10):
	if i == 5:
		break
	print(i)

for j in ['a', 'b', 'c']:
	print(j)
	for i in range(1, 10):
		if i == 5:
			break
		print(i)

# pass: continue the evaluation to the next level
for i in range(1,10):
	if i == 5:
		print("I have 5")
	else:
		pass

# continue: skip the evaluation and return to the same level
for i in range(1, 10):
	if i == 5:
		continue
	print(i)


# #### 2.9 Functions 

# +
# Use them to write cleaner code 
# keep them simple
# We can return any type of object
# Don't forget to add return for output

# def function_name(parameters){
#       DO SOMETHING HERE
#       return values
# }

# Input, output
def add_squares(x = 2, y = 2):
	return x**2 + y**2

# Method operates the data in the class, while a function is used to return or pass data. 
# A function can be directly called by its name, but a method cannot. --> OOP
# -

add_squares()


def add_squares_2(x, y):
	x += 1
	return x**2 + y**2

# add_squares_2()
add_squares_2(1, 2) 

# +
# Copyright of the original version:

# Copyright (c) 2014 Matt Dickenson
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# -

#
