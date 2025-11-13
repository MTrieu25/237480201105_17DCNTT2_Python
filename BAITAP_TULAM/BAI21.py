n=int(input('Nhập số nguyên dương:'))
while n<=0:
    n = int(input('Nhập lại số nguyên dương:'))

if n < 2:
    print(n, "không phải là số nguyên tố")
else:
    dem = 0
    for i in range(2, n):
        if n % i == 0:
            dem += 1
            break
    if dem == 0:
        print(n, "là số nguyên tố")
    else:
        print(n, "không phải là số nguyên tố")