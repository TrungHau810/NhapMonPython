# Bài 1: Cho người dùng nhập số nguyên n và xuất các hình giống trong các ví dụ sau:
n = int(input("n = "))
# n = 5
# *****
# *****
# *****
# *****
# *****
print(("*"*n + "\n")*n)
# n = 5
# *
# **
# ***
# ****print
# *****
for i in range(1,n):
    print(("*"*i +"\n"))
# n = 5
#  *
#  **
#  ***
# ****
# *****
# n = 5
#  *
# ***
# *****
