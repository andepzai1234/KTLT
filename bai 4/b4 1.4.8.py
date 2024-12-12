print("Sinh viên:Tran Duc An")
print("MSSV:215748020110273")
print("####################")
############################

words = input("Nhap day cac tu, cach nhau bang khoang trang: ").split()
max_len = max(len(word) for word in words)
print("Tu dai nhat trong day la:")
for word in words:
    if len(word) == max_len:
        print(word)
