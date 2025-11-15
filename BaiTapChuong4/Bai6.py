n=input('Nhập chuỗi:')
s=0
for i in n:
    if i.isdigit():
        s=s+int(i)
print('Tổng các chữ số trong chuỗi:',s)