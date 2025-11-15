L = list(map(int, input("Nhập list L (các cách nhau bằng khoảng trắng): ").split()))

even_count = sum(1 for x in L if x % 2 == 0)

if even_count <= 1:
    print("Đây là list chẳng lẻ.")
else:
    print("Đây không phải là list chẳng lẻ.")