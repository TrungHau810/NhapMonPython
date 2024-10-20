# Bài 1: Cho người dùng nhập số nguyên n và xuất các hình giống trong các ví dụ sau:
n = int(input("n = "))
# n = 5
# *****
# *****
# *****
# *****
# *****
print(("*" * n + "\n") * n)
# n = 5
# *
# **
# ***
# ****
# *****
for i in range(1, n + 1):
    print(("*" * i + "\n"))
# n = 5
#     *
#    **
#   ***
#  ****
# *****
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i + "\n")
# n = 5
#   *
#  ***
# *****
for i in range(1, n + 1, 2):
    print(("*" * i + "\n").center(n))
