# Viết chương trình tính tổng các số từ 1 đến n với for
print("Nhập các số từ 1 tới ")
n = int(input())
total = 0
for i in range(1, n + 1):
    total+=i
    print(i, ": ", total)
print("Tổng các số từ 1 tới", n, "là: ", total)
print("-----------------------")

# Nhập các số từ 1 tới
# 5
# 1 :  1
# 2 :  3
# 3 :  6
# 4 :  10
# 5 :  15
# Tổng các số từ 1 tới 5 là:  15