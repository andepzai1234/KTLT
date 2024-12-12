print("Sinh viên:Tran Duc An")
print("MSSV:215748020110273")
print("####################")
############################

binary_string = input("Nhap chuoi cac so nhi phan,cach nhau boi dau phay:")
binary_list = binary_string.split(",")
decimal_list = []
for binary in binary_list:
    decimal_list.append(int(binary, 2))
print("Cac gia tri da nhap: ", decimal_list)
    
