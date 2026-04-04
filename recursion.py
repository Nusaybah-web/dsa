"""for i in range(5,0,-1):
    print(i)

print("happy newyear")

#recursion

def countdown(n):
    if n==0:
        print(" happy newyear")
    else:
        print(n)
        countdown(n-1)

countdown(5)

#factorial
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(5))

#sum
def sum(n):
    if n==1:
        return 1
    else:
        return n+sum(n-1)
    
print(sum(5))

#name
def name(n):
    if n==1:
        print("nusaybah")
    else:
        print("nusaybah")
        name(n-1)
name(5)

#reverse
def reverse(n):
    if n=="":
        return ""
    else:
        return reverse(n[1:])+n[0]

print(reverse("python"))

#sierpinski
import turtle

def triangles(size,order):
    if order==0:
        for i in range(3):
            turtle.forward(size)
            turtle.left(120)
    else:
        turtle.speed(10)
        size/=2
        order-=1
        triangles(size,order)
        turtle.forward(size)
        triangles(size,order)
        turtle.right(240)
        turtle.forward(size)
        turtle.left(240)
        triangles(size,order)
        turtle.left(240)
        turtle.forward(size)
        turtle.right(240)

triangles(200,1)
turtle.done()

def exponants(b,e):
    if e==0:
        return 1
    else:
        return b*exponants(b,e-1)

print(exponants(2,0))"""

def fibonacci(b,e,n):
    if n==0:
        return b
    else:
        return fibonacci(e,b+e,n-1)
    
print(fibonacci(0,1,4))
