print("Sinh viên: Tran Duc An")
print("MSSV: 215748020110273")
print("####################")

# Nhập chuỗi số nhị phân từ người dùng, cách nhau bởi dấu phẩy
binary_string = input("Đầu vào là: ")
binary_list = binary_string.split(',')

# Danh sách chứa các số nhị phân chia hết cho 5
divisible_by_5_list = []

# Duyệt qua từng số nhị phân trong danh sách
for binary_num in binary_list:
    # Chuyển đổi số nhị phân sang số thập phân
    decimal_num = int(binary_num, 2)
    # Kiểm tra xem số thập phân có chia hết cho 5 không
    if decimal_num % 5 == 0:
        divisible_by_5_list.append(binary_num)

# In ra kết quả
print('Đầu ra là:', ','.join(divisible_by_5_list))
