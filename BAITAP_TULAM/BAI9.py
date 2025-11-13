tien = int(input("Nhập số tiền: "))

to_50 = tien // 50000
tien = tien % 50000

to_20 = tien // 20000
tien = tien % 20000

to_10 = tien // 10000
tien = tien % 10000

to_5 = tien // 5000
tien = tien % 5000

to_2 = tien // 2000
tien = tien % 2000

to_1 = tien // 1000
tien = tien % 1000

# In kết quả (chỉ in loại có tờ)
print("Số tờ tiền là:")
if to_50 > 0:
    print(to_50, "tờ 50000")
if to_20 > 0:
    print(to_20, "tờ 20000")
if to_10 > 0:
    print(to_10, "tờ 10000")
if to_5 > 0:
    print(to_5, "tờ 5000")
if to_2 > 0:
    print(to_2, "tờ 2000")
if to_1 > 0:
    print(to_1, "tờ 1000")