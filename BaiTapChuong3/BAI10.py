import math
def sochan(n):
        return n % 2 == 0

def sohoanhao(n):
    if n <= 1:
        return False
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong == n

def snt(n):
    if n < 2:
        return 0
    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1

def sochinhphuong(n):
    if n < 0:
        return False
    can = int(math.sqrt(n))
    return can * can == n

def nguyen_to_cung_nhau(a, b):
    return math.gcd(a, b) == 1

def ucln(a,b):
    return math.gcd(a,b)

def bcnn(a,b):
    return (a*b)//ucln(a,b)

n=int(input('n='))
m=int(input('m='))
print(ucln(m,n))