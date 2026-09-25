''' 
   

'''

# def greet():
#     print("Hello")

# greet()

#Parameters

# def sum(a,b,c):
#     result = a+b+c
#     print("The sum of 3 numbers:",result)

#     sum(10,20,30)#valid
#     sum(10)#Invalid
#     sum(10,20,30,40)#Invalid

#     def area_circle(radius):
#     pi = 3.14
#     area=pi * r * r
# print(area)
# area_circle(3)

# def square_value(a):
#     sq = 6
#     square= sq * a
#     print(square)

# square_value(4)

# def bill_value(a,b):
#     bill=a * b
#     print(bill)

# bill_value(100,10)

# def number_value(a, b):

#      if a % 2 == 0:
#          print("Even")
#      else:
#          print("Not Even")

# number_value(100, 10)

#Return State ment

# def add(a,b):
#     return a+b  
# result = add(5,3)
# print( "The sum of:",result)
'''
   #Types of Arguments
 1.Positional
 2.Keyword
 3.Default
 4.Variable-lenth
'''
#Positional

# def greet(name,wish):
#     print("Hello",name,wish)
# greet('Cherry','Good Morning')

# def sum_sub(a,b):
#     sum = a+b
#     sub = a-b
#     result = sum,sub
#     print(result)
# sum_sub(100,500)
# sum_sub(500,100)

#Keyword arg

# def greet(name,wish):
#     print("Hello",name,wish)

# greet(name="Cherry",wish='Good Morning')
# greet(wish='Good Afternoon',name="Cherry")

#Default

# def greet(name,age,city):
#     print("Iam",name,"Iam",age,"Iam live in",city)

# greet(name="Cherry",age='17 years old',city='Rly Kodur')

# def greet(name="Charishma",age=17):
#     print("Hello",name,age)

# greet() 

#Variable-lenth arg

def add(*numbers):
    print(sum(numbers))

add(10, 20, 30, 40)


