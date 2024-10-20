# Cú pháp tạo mảng
from itertools import count

a = [10, 4, 5, 12, 10, 5, 6, -3, 4, 12, 23, 53, 10]
# Nhập n phần tử
# n = int(input("n = "))
# Khởi tạo giá trị cho mảng a
# for i in range(n):
#     a.append(int(input(f"a[{i}] = ")))
print(a)
# Xử lý max, min, số dương, số âm
if (max(a) > 0):
    print("Số dương lớn nhất: ", max(a))
else:
    print("Số dương lớn nhất: *")
if (min(a) < 0):
    print("Số âm bé nhất: ", min(a))
else:
    print("Số âm bé nhất: *")
# Số lần xuất hiện trong mảng
for i in set(a):
    print(f"Số lần {i} xuất hiện: {a.count(i)}")
# Hiển thị phần tử có k lần xuất hiện (k nhập từ bàn phím)
k = int(input("k = "))
for i in set(a):
    if a.count(i) == k:
        print(f"Số {i} có {k} lần xuất hiện")
#Sắp xếp mảng
#Tăng dần
a.sort()
print(a)
#Giảm dần
a.sort(reverse=True)
print(a)