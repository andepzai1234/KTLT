print("Sinh viên: Tran Duc An")
print("MSSV: 215748020110273")
print("####################")

# Hàm kiểm tra xem tất cả các chữ số của số có phải là số chẵn không
def all_even_digits(number):
    for digit in str(number):
        if int(digit) % 2 != 0:  # Nếu có chữ số lẻ
            return False
    return True

# Duyệt qua các số trong đoạn từ 1000 đến 3000
even_digit_numbers = [str(num) for num in range(1000, 3001) if all_even_digits(num)]

# In các số tìm được thành chuỗi phân tách bởi dấu phẩy
print(','.join(even_digit_numbers))
