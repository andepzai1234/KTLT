print("Sinh viên: Tran Duc An")
print("MSSV: 215748020110273")
print("####################")

# Hàm để lọc các số lẻ trong danh sách
def filter_odd_numbers(numbers):
    # Lọc các số lẻ
    return [num for num in numbers if num % 2 != 0]

# Nhập danh sách các số từ người dùng
input_str = input("Nhập danh sách các số, phân tách bởi dấu phẩy: ")

# Chuyển chuỗi đầu vào thành danh sách các số
numbers = list(map(int, input_str.split(',')))

# Lọc các số lẻ
odd_numbers = filter_odd_numbers(numbers)

# In kết quả
print(','.join(map(str, odd_numbers)))
