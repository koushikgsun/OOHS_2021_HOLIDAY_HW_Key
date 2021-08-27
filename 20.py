n = int(input('Enter a number'))
i = 0 
while i <= n :
    i+=1
    if i%2==0 or i%5==0 :
        continue
    print(i)