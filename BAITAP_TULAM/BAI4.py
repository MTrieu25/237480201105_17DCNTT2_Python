import math
a,b,c=eval(input('Nhập độ dài 3 cạnh tam giác cách mhau bởi dấu phẩy:'))
p=(a+b+c)/2
s=math.sqrt(p*(p-a)*(p-b)*(p-c))
print('Chu vi tam giac:',p)
print('Diện tích tam giác:',s)