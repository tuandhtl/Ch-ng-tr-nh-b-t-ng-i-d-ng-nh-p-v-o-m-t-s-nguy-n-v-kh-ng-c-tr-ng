x = input("Nhập số x:")

# Xử lý không được để trống

while x == "":
    x = input("Bạn không được để trống:")

# Xử lý dữ liệu nhập vào phải là số

for i in x:
    if x.isdigit():
        print("Xin chúc mừng bạn đã nhập đúng!!!")
    else:
        x = input("Bạn phải nhập dữ liệu là số:")


print("x = " + x)
