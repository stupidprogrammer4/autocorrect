def sort(ls):
    n = len(ls)
    for i in range(n-1):
        for j in range(0, n-i-1):

            if ls[j][1] < ls[j + 1][1]:
                ls[j], ls[j + 1] = ls[j + 1], ls[j]



n = int(input())

nom = input().split(',')
h = list(map(int, input().split('|')))
pe = input().strip()

ls = []

for i in range(n):
    ls.append((nom[i], h[i]))

sort(ls)

for i, p in enumerate(ls):
    if p[0] == pe:
        print(i+1)
        break
    

##################################################################


import math, json

try:
    s = input()
    d = json.loads(s)
    edges = (d['a'], d['b'], d['c'])
    if edges[0] >= edges[1]+edges[2] or edges[1] >= edges[0]+edges[2] or edges[2] >= edges[1] + edges[0]:
        print('Invalid edges')
    else:
        p = (edges[0] + edges[1] + edges[2])/2
        s = math.sqrt(p*(p-edges[0])*(p-edges[1])*(p-edges[2]))

        edges = list(edges)
        edges.sort()

        if edges[2]**2 == edges[0]**2 + edges[1]**2:
            print('{:.3f},right'.format(s))
        elif edges[2] == edges[0] and edges[0] == edges[1]:
            print('{:.3f},Equalteral'.format(s))
        elif edges[2] == edges[1] or edges[2] == edges[0] or edges[0] == edges[1]:
            print('{:.3f},Isoscles'.format(s))
        else:
            print('{:.3f}'.format(s))
except:
    print("Wrong input!")


def is_armstrong(n, p):
    m = n
    s = 0
    while n:
        rem = n%10
        s = s + (rem**p)
        n //= 10

    return m == s
for i in range(100_000):
    if is_armstrong(i, len(str(i))):
        print(i, end=' ')

print()    
