print("Sinh viên:Tran Duc An")
print("MSSV:215748020110273")
print("####################")
############################

# Nhap ten nguoi tu ban phim
name = input("Nhap ten cua ban: ")

# Tach phan ho va ten rieng
first_name = name[:name.index(' ')]
last_name = name[name.index(' ') + 1:]

# In phan ho va ten rieng ra man hinh
print("Ho cua ban la:", first_name)
print("Ten rieng cua ban la:", last_name)
