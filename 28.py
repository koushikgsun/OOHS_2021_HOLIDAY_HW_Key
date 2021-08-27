def divisiors(x):
    return [y for y in range(1, int(x / 2) + 1) if x % y == 0]

def perfect_numbers_in_range(a,b):
    return [x for x in range(a,b+1) if sum(divisiors(x)) == x]
n = int(input("Enter any number: "))
sum1 = 0
for i in range(1, n):
    if(n % i == 0):
        sum1 = sum1 + i
if (sum1 == n):
    print("The number is a Perfect number!")
else:
    print("The number is not a Perfect number!")
print ("printing all numbers from 1 - 500")
print (str(perfect_numbers_in_range(1, 500))[1:-1])