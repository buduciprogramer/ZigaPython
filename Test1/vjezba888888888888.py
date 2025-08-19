def faktorijel(x):
    proizvod = 1
    for i in range(1, x + 1):
        proizvod *= i
    return proizvod

ft1 = faktorijel(1)
fk2 = faktorijel(2)

print("1! =", ft1)
print("2! =", fk2)