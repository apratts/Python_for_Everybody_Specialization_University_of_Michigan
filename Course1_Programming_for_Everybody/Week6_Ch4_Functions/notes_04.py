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

def max(inp):
    blah
    blah
    for x in inp:
        blah
        blah

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
