# main.py

import sinhvien as sv

def menu():
    print("\n=== CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN ===")
    print("1. Thêm sinh viên")
    print("2. Xóa sinh viên")
    print("3. Sửa sinh viên")
    print("4. Xem danh sách sinh viên")
    print("0. Thoát")

while True:
    menu()
    chon = input("Nhập lựa chọn: ")

    if chon == "1":
        ma = input("Nhập mã sinh viên: ")
        ten = input("Nhập tên sinh viên: ")
        if sv.themSV(ma, ten):
            print("Thêm thành công!")
        else:
            print("Mã sinh viên đã tồn tại!")

    elif chon == "2":
        ma = input("Nhập mã sinh viên cần xóa: ")
        if sv.xoaSV(ma):
            print("Đã xóa!")
        else:
            print("Không tìm thấy mã sinh viên!")

    elif chon == "3":
        ma = input("Nhập mã sinh viên cần sửa: ")
        ten_moi = input("Nhập tên mới: ")
        if sv.suaSV(ma, ten_moi):
            print("Sửa thành công!")
        else:
            print("Không tìm thấy mã sinh viên!")

    elif chon == "4":
        ds = sv.xemDS()
        if len(ds) == 0:
            print("Danh sách rỗng!")
        else:
            print("\n--- DANH SÁCH SINH VIÊN ---")
            for sv in ds:
                print(f"Mã: {sv['ma']}, Tên: {sv['ten']}")

    elif chon == "0":
        print("Bye!")
        break

    else:
        print("Lựa chọn không hợp lệ!")