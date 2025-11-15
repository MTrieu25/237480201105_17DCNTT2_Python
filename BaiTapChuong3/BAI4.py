def vi_tri(lst):
    if not lst:
        return None

    max_value = lst[0]
    vi_tri = 0

    for i in range(1, len(lst)):
        if lst[i] > max_value:
            max_value = lst[i]
            vi_tri = i
    return vi_tri


chuoi = input("Nhập các số nguyên, cách nhau bởi dấu cách: ")
lst = [int(x) for x in chuoi.split()]

# Gọi hàm tìm vị trí lớn nhất
vt = vi_tri(lst)
if vt is None:
    print("Danh sách rỗng!")
else:
    print(f"Vị trí phần tử lớn nhất: {vt}")
    print(f"Giá trị lớn nhất: {lst[vt]}")
