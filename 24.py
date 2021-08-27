x = int(input("Input number: "))
d = []
for i in range(1,x+1):
    c = x/i
    cs = -1*i
    if (c).is_integer():
        d.append(i)
        d.append(cs)
d.sort()
print (str(d)[1:-1])