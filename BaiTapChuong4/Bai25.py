L = list(map(int, input("Nhập list số nguyên: ").split()))

ket_qua = sorted(L, key=lambda x: (x % 2 != 0, x == 0))

print("Kết quả:", ket_qua)
