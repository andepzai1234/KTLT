print("Sinh viên:Tran Duc An")
print("MSSV:215748020110273")
print("####################")
############################

s = input("Nhap chuoi: ")
new_s = ""
for char in s:
    if not char.isdigit():
        new_s += char
print("Chuoi moi: ", new_s)
