def chuoi_ngan_nhat(lst):
    if not lst:
        return None

    ngan_nhat = lst[0]
    for s in lst[1:]:
        if len(s) < len(ngan_nhat):
            ngan_nhat = s
    return ngan_nhat

chuoi = input("Nhập các chuỗi, cách nhau bởi dấu cách: ")
lst = chuoi.split()
ket_qua = chuoi_ngan_nhat(lst)

if ket_qua is None:
    print("Danh sách rỗng!")
else:
    print(f"Chuỗi ngắn nhất là: '{ket_qua}'")
    print(f"Độ dài: {len(ket_qua)} ký tự")
