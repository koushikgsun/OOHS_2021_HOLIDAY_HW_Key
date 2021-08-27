def a(x,y):
    return (x+y)
def s(x,y):
    return (x-y)
def m(x,y):
    return (x*y)
def d(x,y):
    return (x/y)
o = int(input("num1 : "))
p = int(input("num2 : "))
operation = input("operation A,S,M,D : ")
if operation == "A":
    print(a(o,p))
    exit()
if operation == "S":
    print(s(o,p))
    exit()
if operation == "M":
    print(m(o,p))
    exit()
if operation == "D":
    print(d(o,p))
    exit()
if o == o :
    print("please start again since you have made an error")