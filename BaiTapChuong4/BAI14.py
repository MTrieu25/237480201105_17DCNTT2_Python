L = list(map(int, input("Nhập list L (các cách nhau bằng khoảng trắng): ").split()))

found = -1
for x in L:
    if x > 0:
            found = x
            break
if found != -1:
    print("Giá trị dương đầu tiên là : ",found)
else:
    print(-1)