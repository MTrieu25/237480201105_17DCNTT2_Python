a=input('Nhập chuỗi a:')
b=input('Nhập chuỗi b:')
x=a.find(b)
if x!=-1:
    a=a[:x] + a[x+len(b):]
print('Chuỗi a sau khi xóa:',a)