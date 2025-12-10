class Student:
    def __init__(self, ma_sv, ten_sv):
        self.ma_sv = ma_sv
        self.ten_sv = ten_sv

    def __str__(self):
        return f"{self.ma_sv} - {self.ten_sv}"


class StudentManager:
    def __init__(self):
        self.ds = []

    def them_sv(self, ma, ten):
        for sv in self.ds:
            if sv.ma_sv == ma:
                print("Mã sinh viên đã tồn tại!")
                return
        self.ds.append(Student(ma, ten))
        print("Thêm sinh viên thành công!")

    def xoa_sv(self, ma):
        for sv in self.ds:
            if sv.ma_sv == ma:
                self.ds.remove(sv)
                print("Xóa sinh viên thành công!")
                return
        print("Không tìm thấy sinh viên cần xóa!")

    def sua_sv(self, ma, ten_moi):
        for sv in self.ds:
            if sv.ma_sv == ma:
                sv.ten_sv = ten_moi
                print("Sửa thông tin thành công!")
                return
        print("Không tìm thấy sinh viên cần sửa!")

    def tim_kiem(self, tu_khoa):
        ket_qua = []
        for sv in self.ds:
            if tu_khoa.lower() in sv.ma_sv.lower() or tu_khoa.lower() in sv.ten_sv.lower():
                ket_qua.append(sv)

        if not ket_qua:
            print("Không tìm thấy sinh viên.")
        else:
            print("Kết quả tìm kiếm:")
            for sv in ket_qua:
                print(" -", sv)

    def xem_ds(self):
        if not self.ds:
            print("Danh sách sinh viên đang rỗng.")
        else:
            print("Danh sách sinh viên")
            for sv in self.ds:
                print(" -", sv)


def menu():
    ql = StudentManager()

    while True:
        print("\nMENU")
        print("1. Thêm sinh viên")
        print("2. Xóa sinh viên")
        print("3. Sửa sinh viên")
        print("4. Tìm kiếm sinh viên")
        print("5. Xem danh sách sinh viên")
        print("6. Thoát")

        chon = input("Nhập lựa chọn: ")

        if chon == "1":
            ma = input("Nhập mã sinh viên: ")
            ten = input("Nhập tên sinh viên: ")
            ql.them_sv(ma, ten)

        elif chon == "2":
            ma = input("Nhập mã sinh viên cần xóa: ")
            ql.xoa_sv(ma)

        elif chon == "3":
            ma = input("Nhập mã sinh viên cần sửa: ")
            ten_moi = input("Nhập tên mới: ")
            ql.sua_sv(ma, ten_moi)

        elif chon == "4":
            tu_khoa = input("Nhập mã hoặc tên để tìm: ")
            ql.tim_kiem(tu_khoa)

        elif chon == "5":
            ql.xem_ds()

        elif chon == "6":
            print("Thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ!")
menu()
