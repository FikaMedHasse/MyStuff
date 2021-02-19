num2test = int(input("number to test: "))
divisors = []
op = ""

def printDivisors(n): 
    i = 1
    while i <= n : 
        if (n % i==0): 
            divisors.append(i), 
        i+=1

printDivisors(num2test)        

divisors.remove(1)
divisors.remove(num2test)


for j in divisors:
    op += str(divisors[j])

if not divisors:
    print("That's prime!")
else:
    print(f"{num2test} is divisible by", op)
