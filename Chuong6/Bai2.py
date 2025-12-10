class Person:
    def __init__(self, ho_ten, gioi_tinh, nam_sinh, noi_sinh, dia_chi):
        self.ho_ten = ho_ten
        self.gioi_tinh = gioi_tinh
        self.nam_sinh = nam_sinh
        self.noi_sinh = noi_sinh
        self.dia_chi = dia_chi

    def __str__(self):
        return (f"Họ tên: {self.ho_ten}, Giới tính: {self.gioi_tinh}, "
                f"Năm sinh: {self.nam_sinh}, Nơi sinh: {self.noi_sinh}, "
                f"Địa chỉ: {self.dia_chi}")


class GiaoVien(Person):
    def __init__(self, ho_ten, gioi_tinh, nam_sinh, noi_sinh, dia_chi,
                 so_nam_giang_day, hoc_vi):
        super().__init__(ho_ten, gioi_tinh, nam_sinh, noi_sinh, dia_chi)
        self.so_nam_giang_day = so_nam_giang_day
        self.hoc_vi = hoc_vi

    def __str__(self):
        return (super().__str__() +
                f", Số năm giảng dạy: {self.so_nam_giang_day}, Học vị: {self.hoc_vi}")


class HocSinh(Person):
    def __init__(self, ho_ten, gioi_tinh, nam_sinh, noi_sinh, dia_chi,
                 toan, ly, hoa):
        super().__init__(ho_ten, gioi_tinh, nam_sinh, noi_sinh, dia_chi)
        self.toan = toan
        self.ly = ly
        self.hoa = hoa

    def tinh_dtb(self):
        return (self.toan + self.ly + self.hoa) / 3

    def xep_loai(self):
        dtb = self.tinh_dtb()
        min_diem = min(self.toan, self.ly, self.hoa)

        if dtb >= 8 and min_diem >= 6.5:
            return "Giỏi"
        elif dtb >= 6.5 and min_diem >= 5:
            return "Khá"
        elif dtb >= 5 and min_diem >= 3:
            return "Trung bình"
        else:
            return "Yếu"

    def __str__(self):
        dtb = self.tinh_dtb()
        return (super().__str__() +
                f", Toán: {self.toan}, Lý: {self.ly}, Hóa: {self.hoa}, "
                f"ĐTB: {dtb:.2f}, Xếp loại: {self.xep_loai()}")


gv = GiaoVien("Nguyễn Văn A", "Nam", 1980, "Hà Nội", "Q.1",
              12, "Thạc sĩ")

hs = HocSinh("Trần Thị B", "Nữ", 2007, "TP.HCM", "Q.7",
             7.5, 8.0, 9.0)

print("=== Giáo viên ===")
print(gv)

print("\n=== Học sinh ===")
print(hs)
