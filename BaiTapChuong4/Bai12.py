L=list(map(int,input('Nhập list số nguyên cách nhau bởi khoảng trắng:').split()))
a=int(input('Nhập a:'))
b=int(input('Nhập b:'))
x=L[a:b+1]
nho=min(x)
print(f'Giá trị nhỏ nhất từ vị trí {a} đến {b} là {nho}')