print("Sinh viên:Tran Duc An")
print("MSSV:215748020110273")
print("####################")
############################

def benefit(t, n, k):
    # Chuyển lãi suất từ % sang số thập phân
    t = t / 100
    # Tính số tiền sau k tháng với lãi suất gộp hàng tháng
    total_amount = n * (1 + t) ** k
    return total_amount

# Nhập dữ liệu từ người dùng
t = float(input("Nhập lãi suất (%/tháng): "))
n = float(input("Nhập số vốn ban đầu: "))
k = int(input("Nhập số tháng gửi: "))

# Gọi hàm benefit để tính số tiền nhận được sau k tháng
result = benefit(t, n, k)

print(f"Số tiền nhận được sau {k} tháng là: {result:.2f} VND")
