toan = float(input("Nhập điểm Toán: "))
van = float(input("Nhập điểm Văn: "))
anh = float(input("Nhập điểm Tiếng Anh: "))

tb = (toan + van + anh) / 3

if tb >= 8.5 and toan >= 9 and toan > van and toan > anh:
    chuyen = "Toán"
elif tb >= 8.5 and van >= 9 and van >= anh:
    chuyen = "Văn"
elif tb >= 8.5 and anh >= 8.0:
    chuyen = "Tiếng Anh"
elif tb >= 8.5:
    chuyen = "Tin học"
else:
    chuyen = "Không đậu chuyên"

print("Điểm trung bình: %3.2f"%tb)
print("Học sinh đậu chuyên:", chuyen)