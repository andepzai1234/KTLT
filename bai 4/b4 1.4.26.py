print("Sinh viên: Tran Duc An")
print("MSSV: 215748020110273")
print("####################")

balance = 0  # Số dư ban đầu của tài khoản

while True:
    transaction = input("Nhập giao dịch (D [số tiền] hoặc W [số tiền], hoặc để trống để kết thúc): ").split()
    
    if not transaction:  # Nếu không có giao dịch nhập vào (nhấn Enter để kết thúc)
        break
    
    trans_type, amount = transaction  # Lấy loại giao dịch và số tiền
    amount = int(amount)  # Chuyển số tiền thành số nguyên

    if trans_type == 'D':  # Giao dịch gửi tiền
        balance += amount  # Cộng số tiền vào số dư
    elif trans_type == 'W':  # Giao dịch rút tiền
        balance -= amount  # Trừ số tiền từ số dư

print(f"Số dư cuối cùng của tài khoản là: {balance} VND")

