x = input("")
x = int(float(x))
for i in range(-x, x + 1):
    if i != 0:
        if x % i == 0:
            print(i)
