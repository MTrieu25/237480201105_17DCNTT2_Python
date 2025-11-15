L = list(map(int, input("Nhập list L (các cách nhau bằng khoảng trắng): ").split()))

x = int(input("Nhập số nguyên x: "))

closest = L[0]
for num in L:
    if abs(num - x) < abs(closest - x):
        closest = num

print("Giá rị gần x nhất trong list là:", closest)