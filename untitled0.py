# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/aayushbhawsar/PythonAayush/blob/master/pythonbasic.ipynb
"""

32 % 10

z = 1 + 3 * 2 - 8 / 4 
print(z)

x = int(89.7) 
print(x)

x = 0/1
 int(89.7)
 print(x)

Days = input('Enter number of Days')

Rate = input('Enter rate per Day')

TotalPay = float(Days)*float(Rate)
print('Total Pay:', TotalPay)

num=float(input("Enter the number"))
if num > 0:
  print("positive number")
elif num < 0:
  print("negative number")
else:
  print("zero")

#try except
num=input("Enter a number")
try:
  val=int(num)
  print ("conersion successful")
except:
  val=-1

if val > 0:
  print("number is ",val)
else:
  print("not a positve number")

#try except
#num=input("Enter a number")
try:
  val=4/2
  print ("division successful")
except:
  val=-1

if val > 0:
  print("answer is ",val)
else:
  print("can't divide by zero")

xh = input("Enter Days:")
xr = input("Enter Rate:")
try:
  fh = float(xh)
  fr = float(xr)
except:
  print("Error, please enter numeric input")

TotalPay = float(xh)*float(xr)
print('Total Pay:', TotalPay)



#even and odd using function
def evenodd(num):
  if num==0:
    print("Number is zero")
  elif num%2==0:
    print("Number is even")
  else:
      print("Number is odd")

evenodd(int(input("Enter the number")))



#function with return value
def greet():
  return "Hello"
print(greet(),"Aayush")
print(greet(),"ram")

#function with multiple parameter
def add(a,b):
  return a+b
add(3,3)

def greet():
  print ("Hello")

  return

  print ("Hello1")

greet()

def say(message,time =1):
  print(message* time)
say("aayush")
say("good",5)

def computeTotalpay(Days,Rate):
  TotalPay = float(Days)*float(Rate)
  print('Total Pay:', TotalPay)

computeTotalpay(45,10)

def computepay(hour, rate):
    pay = hour * rate
    return pay

xh = input("Enter Hours:")

xr = input("Enter Rate:")


try:
    fh = float(xh)
    fr = float(xr)

    print("Pay: ",computepay(fh,fr))
except:
    print("Error, please enter numeric input")

#while loop
count=0
while (count<=5):
  print("Aayush")
  count=count+1

#break
while True:
  line=input("Enter the data")
  if line == 'done':
    break
  print("line")
print("Done!")

#continue
while True:
  line=input("Enter the data")
  if line[0]=='#':
    continue
  if line == 'done':
    break
  print("line")
print("Done!")

#for loop
I=["aayush","Shadab","aamir"]
for i in I:
  print(i)

#find the largest number
large = -1
I=[1,2,3,4,5,6,7,8,9]
for num in I:
  if num > large:
    large=num
print(large)

#count element in th list
count= 0
I=[1,2,3,4,5,6,7,8,9]
for num in I:
  count=count+1
print(count)

#sum the elements in the list
count= 0
sum=0
I=[1,2,3,4,5,6,7,8,9]
for num in I:
  sum=sum + num
  count=count+1
print(sum)

#Average of the elements in the list
count= 0
sum=0
I=[1,2,3,4,5,6,7,8,9]
for num in I:
  sum=sum + num
  average=sum/len(I)
  count=count+1
print(sum)
print(average)

#filtering in a loop
I=[1,2,3,4,5,6,7,8,9]
for num in I:
  if num>5:
    print(num)

#searching in a loop
I=[1,2,3,4,5,6,7,8,9]
for num in I:
  if num==5:
    print("found")
  else:
      print("not found")

#finding the smallest value
small=None
I=[1,2,3,4,5,6,7,8,9]
for num in I:
  if small==None:
    small=num
  elif num < small:
    small=num
print(small)

#Write a program which repeatedly reads numbers until the user enters "exit". Once "exit" is entered, print out the sum, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number. Enter a number: 4 Enter a number: 5 Enter a number: bad data Invalid input Enter a number: exit 9.0 2 4.5

sum=0
count=0 
while True: 
  num=input('Enter Number: ') 
  if num=='exit': 
    break 
  try: 
    x=float(num) 
  except: 
    print('Data Invalid Input')
    continue
  count=count+1
  sum=sum+x  
print('Sum= ',sum) 
print('Count= ',count) 
print('Average= ',sum/count)

#Python Program for factorial of a number
num = int(input("Enter the number"))
fact = 1
if num<= 0:
   print("no factorial of zero and negative number")
else:
   for i in range(1,num + 1):
       fact = fact*i
print(fact)

# Python Program for simple interest
def simpleinterest():
  SI=principle*rate*time/100
  return SI


p = input("Enter the principle")
r = input("Enter the rate")
t = input("Enter the time")
try:
  principle=float (p)
  rate=float (r)
  time=float (t)
  print(simpleinterest())
except:
  print("something wrong with data")

#Python Program for compound interest
def compoundinterest():
  SI=principle * (pow((1 + rate / 100), time))
  return SI


p = input("Enter the principle")
r = input("Enter the rate")
t = input("Enter the time")
try:
  principle=float (p)
  rate=float (r)
  time=float (t)
  print(compoundinterest())
except:
  print("data is wrong")

#Python Program to check Armstrong Number
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum =sum +digit ** 3
   temp //= 10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

#Python Program to Find Armstrong Number in an give range
lower = 100
upper = 2000

for num in range(lower, upper + 1):
  order = len(str(num))
  sum = 0
  temp = num
  while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
  if num == sum:
    print(num)

#Python program to print all Prime numbers in an Interval
lower = 2
upper = 50
for num in range(lower, upper ):
  if num > 1:
    for i in range(2,num):
       if (num % i) == 0:
         print(num,"is not a prime number")
         break
    else:
          print(num,"is a prime number")

#Python program to check whether a number is Prime or not
num=int(input("Enter the number"))
if num > 1:
    for i in range(2,num):
       if (num % i) == 0:
         print(num,"is not a prime number")
         break
    else:
          print(num,"is a prime number")

#Python Program for n-th Fibonacci number using recursion wrong
def fib(num):
  if num <= 1:
    return num
  else:
    return(fib(num-1)+fib(num-2))
n1=(int(input("Enter the number")
if n <= 0:
  print("please enter positive number")
else:
    for i in range(n1):
      print(fib(i))

#Python Program for n-th Fibonacci number using recursion right
def recur_fibo(n):  
   if n <= 1:  
       return n  
   else:  
       return(recur_fibo(n-1) + recur_fibo(n-2))  
# take input from the user  
nterms = int(input("How many terms? "))  
# check if the number of terms is valid  
if nterms <= 0:  
   print("Plese enter a positive integer")  
else:  
   print("Fibonacci sequence:")  
   for i in range(nterms):  
       print(recur_fibo(i))

# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

#Python Program for How to check if a given number is Fibonacci number?
# python program to check if x is a perfect square 
import math 
  
# A utility function that returns true if x is perfect square 
def isPerfectSquare(x): 
    s = int(math.sqrt(x)) 
    return s*s == x 
  
# Returns true if n is a Fibinacci Number, else false 
def isFibonacci(n): 
  
    # n is Fibinacci if one of 5*n*n + 4 or 5*n*n - 4 or both 
    # is a perferct square 
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4) 
     
# A utility function to test above functions 
for i in range(1,11): 
     if (isFibonacci(i) == True): 
         print (i,"is a Fibonacci Number")
     else: 
         print (i,"is a not Fibonacci Number ")

#Program to print ASCII Value of a character
val = input("enter the character")
print("The ASCII value of ",val ,"is", ord(c))

#Python Program for Sum of squares of first n natural numbers
def squaresum(n) : 
    sum = 0
    for i in range(1, n+1) : 
        sum = sum + (i * i) 
    return sum 
print(squaresum(4))

#Python Program for cube sum of first n natural numbers
def cube(n) : 
    sum = 0
    for i in range(1, n+1) : 
        sum = sum + (i * i * i) 
    return sum 
print(cube(5))