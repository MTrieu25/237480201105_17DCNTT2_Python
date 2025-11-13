n=int(input('Nhập số nguyên dương:'))

while n<=0:
    n = int(input('Nhập lại số nguyên dương:'))
t=n
dem=0
if n == 0:
    dem = 1
else:
    while n > 0:
        n //= 10
        dem += 1

print(t,"có", dem, "chữ số.")