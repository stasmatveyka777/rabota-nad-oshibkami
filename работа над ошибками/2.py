import random
n = int(input("Bedite chislo"))
a = [random.randint(0,15) for i in range(n)]
print(a)
print(a[0],a[-1])
s=1
for i in a:
    s*=i
print(s)
