a = int(input("Input any number: "))
b = str(a)
c = []
for digit in b:
    c.append (int(digit))
d = c[0]
e = c[-1]
c[0] = e
c[-1] = d
f = [str(g) for g in c]
h = "".join(f)
i = int(h)
print(i)