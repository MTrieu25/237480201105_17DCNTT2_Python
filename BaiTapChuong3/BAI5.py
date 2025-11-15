def tim_vi_tri_k(lst, k):
    for i in range(len(lst)):
        if lst[i] == k:
            return i
    return -1

chuoi = input("Nhập các số nguyên, cách nhau bởi dấu cách: ")
lst = [int(x) for x in chuoi.split()]
k = int(input("Nhập số nguyên dương k: "))
vt = tim_vi_tri_k(lst, k)
if vt == -1:
    print(f"Không tìm thấy giá trị {k} trong danh sách.")
else:
    print(f"Giá trị {k} xuất hiện đầu tiên tại vị trí: {vt}")
