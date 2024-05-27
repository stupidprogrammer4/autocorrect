import random, string

n = random.randint(1, 10)
nom, h = [], []
for i in range(n):
    nom.append(''.join(random.choice(string.ascii_lowercase) for _ in range(5)))
    h.append(str(random.randint(150, 210)))

print(n)
print(','.join(nom))
print('|'.join(h))
print(nom[random.randint(0, n-1)])


a = random.randint(1, 7)
b = random.randint(a, 7)
c = random.randint(b, a+b+1)

print('{'+f'"a" : {a}, "b" : {b}, "c" : {c}'+'}')

