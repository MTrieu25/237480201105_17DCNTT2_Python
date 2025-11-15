n=input('Nhập chuỗi:')
hoa=False
thuong=False
so=False
dacbiet=False
for i in n:
    if i.isupper():
        hoa=True
    if i.islower():
        thuong=True
    if i.isdigit():
        so=True
    else:
        dacbiet=True
if len(n)>6 and hoa and thuong and so and dacbiet:
    print('Mật khẩu mạnh!')
else:
    print('Mật khẩu yếu!')