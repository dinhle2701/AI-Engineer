# Nhập một số và kiểm tra số đó chẵn hay lẻ.
print("~~~Nhập một số và kiểm tra số đó chẵn hay lẻ~~~")
print("Nhập số nguyên n: ")
n = int(input())
if n % 2 == 0:
    print(n, "là số chẵn")
else:
    print(n, "là số lẻ")