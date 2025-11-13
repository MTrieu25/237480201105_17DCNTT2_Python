a=int(input('Nhap so nguyen duong a:'))
b=int(input('Nhap so nguyen duong b:'))
c=int(input('Nhap so nguyen duong c:'))
if(a+b>c)and(a+c>b)and(b+c>a):
    print('Ba gia vua nhap la tam giac')
else:
    print('Ba gia vua nhap khong la tam giac')