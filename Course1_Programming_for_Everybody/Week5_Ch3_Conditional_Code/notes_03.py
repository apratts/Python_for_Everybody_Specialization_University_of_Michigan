x = 5
if x < 10:
    print('smaller')
if x > 20:
    print('bigger')

print('Finis')

x = 5
if x == 5:
    print("Equals 5")
if x > 4:
    print("Greater than 4")
if x >= 5:
    print('Greater then  or Equals 5')
if x < 6: print('Less than 6')
if x <= 5:
    print('Less then or Equals 5')
if x != 6:
    print('Not equal 6')

x = 5
print('Before 5')
if x==5:
    print('Is 5')
    print('Is Still 5')
    print('Third 5')
print('Afterwards 5')
print('Before 6')
if x == 6:
    print('Is 6')
    print('Is Still 6')
    print('Third 6')
print('Afterwards 6')

x = 5
if x > 2:
    print('Bigger than 2')
    print('Still bigger')
print('Done with 2')

for i in range (5):
    print(i)
    if i > 2:
        print('Bigger than 2')
    print('Done with i', i)
print('All Done')

#Git commands
#git clone [url],git add ., git commit -"[comments]",  git push

x = 42
if x > 1:
    print('More than one')
    if x < 100:
        print('Less than 100')
print('All done')

x = 4
if x > 2:
    print('Bigger')
else:
    print('smaller')
print('All done')

#3.2 More Conditional Statements
#Multi-way if
x=0
if x < 2:
    print('small')
elif x < 10:
    print('Medium')
else:
    print('LARGE')
print('All done')

x=5
if x < 2:
    print('small')
elif x < 10:
    print('Medium')
else:
    print('LARGE')
print('All done')

x=20
if x < 2:
    print('small')
elif x < 10:
    print('Medium')
else:
    print('LARGE')
print('All done')

#no else
x=5
if x < 2:
    print('small')
elif x < 10:
    print('Medium')

print('All done')

x=50
if x < 2:
    print('small')
elif x < 10:
    print('Medium')

print('All done')

#elifs
x = 15
if x < 2:
    print('Small')
elif x < 10:
    print('Medium')
elif x < 20:
    print('Big')
elif x < 40:
    print('Large')
elif x < 100:
    print('Huge')
else:
    print('Ginormous')

#Multi-way Puzzles
x=27

if x < 2:
    print('Below 2')
elif x >=2:
    print('Two or more')
else:
    print('Something else')

X=29

if x < 2:
    print('Below 2')
elif x < 20:
    print('Below 20')
elif x < 10:
    print('Below 10')
else:
    print('Something else')

#without try / except with traceback

#astr = 'Hello Bob'
#istr = int(astr) #traceback
#print('First', istr)
#astr = '123'
#istr = int(astr)
#print('Second', istr)

#try / except without traceback

astr = 'Hello Bob'
try:
    istr = int(astr)
except: #kind of like else in if/then else
    istr = -1

print('First', istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1

print('Second', istr)

astr = 'Bob'
try:
    print('Hello')
    istr = int(astr) #traceback
    print('There')
except:  #will execute and not go back to try block
    istr = -1

print('Done', istr)


rawstr = input('Enter a number:')
try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0:
    print ('Nice work') #will execute if integer
else:
    print('Not a number') #will execute if text

#book notes
3.1 Boolean expressions
True or false
== operator
5==5
5==6
x!=y # x is not equal to y

3.2 Logical operators
and, or, not

and
x > 0 and x < 10
x is greater than 0 and less than 10

or
n%2 == 0 or n%3 == 0
n is divisible by 2 or 3

not
not (x > y)
x > y is false, x is less than or equal to y

3.3 Conditional execution

if x > 0:
    print('x is positive’)

if x < 0:
    pass

x = 3
if x < 10:
    print('Small’)

3.4 Alternative execution

if x%2 == 0:
    print('x is even’)
else :
    print('x is odd’)

3.5 Chained conditionals

if x < y:
    print('x is less than y’)
elif x > y:
     print('x is greater than y’)
else:
    print('x and y are equal’)

3.6 Nested conditionals

3.7 Catching exceptions using try and except

inp = input('Enter Fahrenheit Temperature: ‘)
fahr = float(inp)
cel = (fahr - 32.0) * 5.0 / 9.0
print(cel)

inp = input('Enter Fahrenheit Temperature: ‘)
try:
fahr = float(inp)
cel = (fahr - 32.0) * 5.0 / 9.0
print(cel)
except:
print('Please enter a number’)

3.8 Short-circuit evaluation of logical expressions

3.9 Debugging
