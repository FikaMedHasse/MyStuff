num2test = int(input("number to test: "))
divisors = []
op = ""

def printDivisors(n): 
    i = 1
    while i <= n : 
        if n % i == 0: 
            divisors.append(i), 
        i+=1

printDivisors(num2test)        

divisors.remove(1)
divisors.remove(num2test)


for i in divisors:
    op += str(i)
    if i == divisors[-2]:
        op += " and "
    if i != divisors[-1] and i != divisors[-2]:
        op += ", "
    


if not divisors:
    print("That's prime!")
else:
    print(f"{num2test} is divisible by", op)
