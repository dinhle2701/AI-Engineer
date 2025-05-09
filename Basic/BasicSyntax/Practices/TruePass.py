# Viết chương trình nhập mật khẩu đúng mới thoát (dùng while True)
while True:
    print("Nhập mật khẩu: ")
    n = input()
    if n == "123456":
        print("Mật khẩu đúng")
        break
    else:
        print("Mật khẩu sai")
print("-----------------------")