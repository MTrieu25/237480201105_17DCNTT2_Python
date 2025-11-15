n= int(input("Nhập số lượng sv: "))
ds = []
for i in range(n):
    ten = input("Nhập tên sv thứ {i +1} : ")
    ds.append(ten)

ten_tim = input("Nhập tên sv cần tìm: ")

if ten_tim in ds:
    print("Tìm thấy sv trong ds")
else:
    print("Không tìm thấy sv trong ds")

