L=list(map(int,input('Nhập list số nguyên cách nhau bởi khoảng trắng:').split()))
vt=[]
for i in range(1,len(L) -1):
    if L[i]== L[i-1] * L[i+1]:
        vt.append(i)
if len(vt)==0:
    print(-1)
else:
    print('Các vị trí thỏa điều kiện: ',vt)
