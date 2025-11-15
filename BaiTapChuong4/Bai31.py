def max_key_value(d):
    if not d:               # kiểm tra dictionary rỗng
        return None
    return max(d, key=d.get)


data = {"a": 10, "b": 25, "c": 7, "d": 25}


result = max_key_value(data)
print("Key có giá trị lớn nhất:", result)
