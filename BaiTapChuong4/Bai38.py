ds_sinhvien = []

def them_sv ():
    ma_sinhvien = input(" nhap ma so sinh vien: ")
    ten_sinhvien = input(" nhap ten sinh vien: ")

    for sv in ds_sinhvien:
        if sv["ma"]==ma_sinhvien:
            print("Mã số sv đã tồn tại!")
            return

    ds_sinhvien.append({"ma": ma_sinhvien,"ten" : ten_sinhvien})
    print("Thêm sv thành công!")

def sua_sv():
    ma_sinhvien = input(" nhap ma so sinh vien can sua: ")
    for sv in ds_sinhvien:
        if sv["ma"]==ma_sinhvien:
            ten_moi = input("nhập tên mới: ")
            sv["ten"] = ten_moi
            print("Sửa thành công !")
            return
    print("Không tìm thấy sv !")

def xoa_sv():
    ma_sinhvien = input(" nhap ma so sinh vien can xoa: ")
    for sv in ds_sinhvien:
        if sv["ma"]==ma_sinhvien:
            ds_sinhvien.remove(sv)
            print(" Xoá thành công!")
            return
    print("Không tìm thấy sv !")

def xem_ds():
    if not ds_sinhvien:
        print("Danh sách trống")
        return
    print("\n======DANH SACH SINH VIEN======")
    for sv in ds_sinhvien:
        print(f"Mã:{sv['ma']} - Tên:{sv['ten']}")
    print("===========================================\n")

while True:
    print("\n======QUAN LY SINH VIEN======")
    print("1. Thêm sinh viên")
    print("2. Xoá sinh viên")
    print("3. Sửa sinh viên")
    print("4. Xem danh sách")
    print("5. Thoát")

    chon = input("Chọn chức năng: ")
    if chon == "1":
        them_sv()
    elif chon == "2":
        xoa_sv()
    elif chon == "3":
        sua_sv()
    elif chon == "4":
        xem_ds()
    elif chon == "5":
        print("Thoát chuong trình")
        break
    else:
        print("Lựa chọn không hợp lệ")

