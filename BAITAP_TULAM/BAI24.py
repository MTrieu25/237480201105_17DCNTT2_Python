n=int(input('Nhập số nguyên dương:'))
while n<=0:
    n = int(input('Nhập lại số nguyên dương:'))
t=n
chan = 0
le = 0

if n == 0:
    chan = 1
else:
    while n > 0:
        so = n % 10
        if so % 2 == 0:
            chan += 1
        else:
            le += 1
        n //= 10
print(t,'có',chan,'số chữ số chẵn',le,'chữ số lẻ')