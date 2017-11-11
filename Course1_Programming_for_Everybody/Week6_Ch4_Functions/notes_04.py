#Stored (and reused) Steps
def thing(): #defines function and stores like a variable no output
    print('Hello')
    print('Fun')

thing() #call/invoke the function and print defined
print('Zip')
thing()

#max and min functions
big = max('Hello world') #argument, string
print(big)

tiny = min('Hello world')
print(tiny)

#def max(inp):
    #blah
    #blah
    #for x in inp:
    #    blah
    #    blah

#Type Conversions
print (float(99) / 100)

i = 42
type(i)

f = float(i)
print(i)

type(f)

print(1 + 2 * float(3) / 4 - 5)

#string Conversions
#sval = '123'
#type(sval)

#print(sval + 1)

#ival = int(sval)
#type(ival)

#print(ival + 1)

#nsv = 'hello bob'
#niv = int(nsv)

#building our own Functions
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

x = 5
print('Hello')

def print_lyrics():  # does not run code, must invoke function
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

print('Yo')
x = x + 2
print(x)


x = 5
print('Hello')

def print_lyrics():  # does not run code, must invoke function, store
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

print('Yo')
print_lyrics() #without parameters, call, reuse, invoke
x = x + 2
print(x)


#parameters
def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang =='fr':
        print('Bonjour')
    else:
        print('Hello')

greet('en')
greet('es')
greet('fr')

#Return Values
def greet():
    return "Hello"

print(greet(),"Glenn")
print(greet(), "Sally")

def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang =='fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(greet('en'),'Glenn')
print(greet('es'), 'Sally')
print(greet('fr'), 'Michael')

def addtwo(a, b):
    added = a + b
    return added

x = addtwo(3, 5)
print(x)

#Chapter 4
#functions
#4.1 Fucntion Calls
#4.2 Built-in Functions
type(32)

max('Hello world')
min('Hello world')

len('Hello world')

#4.3 Type conversion Functions
#4.4 Random numbers

import random

for i in range(10):
    x = random.random()
    print(x)

import random
random.randint(5, 10)
random.randint(5, 10)

import random
t = [1, 2, 3]
random.choice(t)
random.choice(t)

#4.5 Math Functions
import math
print(math)

#ratio = signal_power / noise_power
#decibels = 10 * math.log10(ratio)

radians = 0.7
height = math.sin(radians)

degrees = 45
radians = degrees / 360.0 * 2 * math.pi
math.sin(radians)

math.sqrt(2) / 2.0

#4.6 Adding new Functions
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day')

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day')

print(print_lyrics)
print(type(print_lyrics))
print_lyrics()

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()

#4.7 Definitions and uses
def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day')

repeat_lyrics()

#4.8 Flow of execution

#4.9 parameters and arguments

def print_twice(bruce):
    print(bruce)
    print(bruce)

print_twice('spam')
print_twice(17)

import math
print_twice(math.pi)

print_twice('spam' *4)
print_twice(math.cos(math.pi))

michael = 'Eric, the half bee'
print_twice(michael)

#4.10 Fruitful functions and void Functions

x = math.cos(radians)
golden = (math.sqrt(5) + 1) / 2

math.sqrt(5)

result = print_twice('bing')
print(result)

print(type(None))

def addtwo(a, b):
    added = a + b
    return added

x = addtwo(3, 5)
print(x)

#4.12 Debugging
#4.13 glossary
#4.14 exercises
def fred():
    print("zap")

def jane():
    print("ABC")

jane()
fred()
jane()
