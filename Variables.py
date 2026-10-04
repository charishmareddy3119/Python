''' 
Types of variables

1.Global Variable
2.Local Variable

'''
'''
A Group of line with some name is called function
A group of functions saved in one file 
A Group of modeuals 
A Group of pakage is nothing but a library
if
'''
# a = 'This is global variable'
# b = 10

# def  g():
#     print(a)
#     print(b)

#     #Creating another function

# def g1():
#     print(a)
#     print(b)

# # Calling Function

# g()    
# g1()

#Local variable

# def l():
#      a = 'This is local variable'
#      b = 10
#      print(a)
#      print(b)

#  # Creating another function

# def l1():
#       print(a) # Name Error 
#       print(b) # Name Error

#  # Calling a function

# l()
# l1()

'''
LAMBDA Function 
(or)
ANONYMOUS Function :
------------------------
* Sometimes we can declare a function without name,such type of nameless 
functions are called as anonymous functions or lambda expressions.
* The main advantage of anonymous function is just for instant use 
(i.e for one time usage.)
Syntax:
       lambda arguments_list:expression

Note:
By using lambda functions we can write concise code so that readability of the program 
will be improved.

Note:
    Lambda function internally returns expression value and we are not required 
    to write return statement explicitly.


Some times we can pass function as argument to another function.
In such case lambda functions are best choice.

We can use lambda functions very commanly with filter(),map() and reduce()
functions bcoz these functions expect function as argument.

# Normal functions:
#-------------------
def squareit(n):
    return n*n
print(squareit(3))
print(squareit(4))

# # lambda function:
# # -----------------
s = lambda n:n*n
print('The square of 3 is:',s(3))
print('The square of 5 is:',s(5))

# Recursive Function:

def factorial(n):
    if n==0:
       return 1
    else:
    return n * factorial(n-1)
print(factorial(5))

# Factorial:

def factorial(n):
    result = 1
    while n >= 1:
        result = result * n
        n = n-1
    return result
 print(factorial(5)

'''

# Normal function

# def square(n):
#     return n*n
# result = square(5)
# print(result)

# Lambda

# S=lambda n:n*n
# print(S(5))

# S=lambda n:n+n
# print(S(5))

# Recursive Method

# def factorial(n):
#     if n==0:
#        return 1
#     else:
#     return n * factorial(n-1)
# print(factorial(5))

# Normal Function or Factorial Method

# def factorial(n):
#     result = 1
#     while n >= 1:
#       result = result * n
#       n = n-1
#     return result
# print(factorial(5)

# Palindrome by using recursive function.

def palindrome(n, rev=0):
    if n == 0:
        return rev
    else:
        return palindrome(n // 10, rev * 10 + n % 10)

n = int(input("Enter a number: "))

if n == palindrome(n):
    print("Palindrome")
else:
    print("Not Palindrome")