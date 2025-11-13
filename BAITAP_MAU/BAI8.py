a,b,c=eval(input('Nhap 3 so cach nhau boi dau phay:'))
if(a+b>c)and(a+c>b)and(b+c>a):
    if a*a+b*b==c*c or a*a+c*c==b*b or c*c+b*b==a*a:
        print('Day la tam giac vuong')
    elif a==b==c:
        print('day la tam giac deu')
    elif a==b or a==c or b==c:
        print('day la tam giac can')
    else:
        print('day la tam giac thuong')
else:
    print('Ba gia vua nhap khong la tam giac')