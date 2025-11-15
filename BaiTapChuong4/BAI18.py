L = list(map(int, input("Nhập list L (các cách nhau bằng khoảng trắng): ").split()))

is_sorted = True
for i in range(len(L) - 1):
    if L[i] > L[i + 1]:
        is_sorted = False
        break

print(is_sorted)