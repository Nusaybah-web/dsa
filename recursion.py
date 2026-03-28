for i in range(5,0,-1):
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