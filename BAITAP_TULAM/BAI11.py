n=int(input('Nhập số nguyên dương:'))
while n<=0:
    n = int(input('Nhập lại số nguyên dương:'))
if (n%5==0) and (n%7==0):
    print(n,'chia hết cho 5 và 7')
else:
    print(n,'không chia hết cho 5 và 7')