a=input('Nhập chuỗi:')
hoa=0
thuong=0
so=0
for i in a:
    if i.isupper():
        hoa=hoa+1
    elif i.islower():
        thuong=thuong+1
    elif i.isdigit():
        so=so+1
print('Số ký tự hoa: ',hoa)
print('Số ký tự thường: ',thuong)
print('Số ký tự số',so)