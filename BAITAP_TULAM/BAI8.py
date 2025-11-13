n=int(input('Nhập số nguyên có 4 chữ số:'))
while n<1000 or n>9999:
    n=int(input('Nhập lại số nguyên có 4 chữ số:'))
nghin = n // 1000
tram = (n // 100) % 10
chuc = (n // 10) % 10
donvi = n % 10
tong = nghin + tram + chuc + donvi
print("Tổng các chữ số là:", tong)