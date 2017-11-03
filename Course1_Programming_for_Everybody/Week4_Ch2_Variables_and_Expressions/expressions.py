print('what are hours and rate?')

print ('pay=hours*rate')
hours = 35.0
rate = 12.5
pay = hours * rate
print(pay)

print('pay=hours*hours')
hours = 35.0
rate = 12.5
pay = hours * hours
print(pay)

print('equation: x=3.9*x*(1-x) what is x?')
x=0.6
x=3.9*x*(1-x)
print(x)

print('Addition: xx=2, x=xx+2')
xx=2
xx=xx+2
print(xx)

print('Multiplication: yy=440*12')
yy=440*12
print(yy)

print('division: zz=yy/1000')
zz=yy/1000
print(zz)

print('remainder: jj=23, kk=jj%5')
jj=23
kk=jj%5
print(kk)

print('power: 4**3')
print(4**3)

x=1+(2*3)-(4/(5**6))
print(x)

x=1+2**3/4*5
print(x)

ddd=1+4
print(ddd)

eee='hello '+'there'
print(eee)

type(ddd)
type(eee)

print(float(99)+100)
i=42
type(i)
f=float(i)
print(f)
type(f)

print(10/2)
print(9/2)
print(99/100)
print(10.0/2.0)
print(99.0/100.0)

nam=input('What is your name?')
fro=input('Where are you from?')

print('Welcome to San Diego ',nam, 'I hear ',fro,'is nice!')

# Get the name of the file and open it
name = input('Enter file:')
handle = open(name, 'r')

# Count word frequency - make histogram
counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

# Find the most common word
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

# All done
print(bigword, bigcount)

# Convert elevator floors
inp = input('Europe floor?')
usf = int(inp) + 1
print('US floor', usf)
