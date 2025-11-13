s1=s2=0
n=int(input('Nhập số nguyên dương:'))
while n<=0:
    n = int(input('Nhập lại số nguyên dương:'))
for i in range(0,n):
    if(i%2!=0):
        s1=s1+i
    else:
        s2=s2+i
print('Tổng các số lẻ <',n,'là:',s1,)
print('Tổng các số chẳn <',n,'là:',s2)