print("Sinh viên: Tran Duc An")
print("MSSV: 215748020110273")
print("####################")

# Hàm để đếm số chữ hoa và chữ thường trong câu
def count_upper_and_lower(sentence):
    upper_count = 0
    lower_count = 0
    
    # Duyệt qua từng ký tự trong câu
    for char in sentence:
        if char.isupper():  # Kiểm tra nếu ký tự là chữ hoa
            upper_count += 1
        elif char.islower():  # Kiểm tra nếu ký tự là chữ thường
            lower_count += 1
    
    return upper_count, lower_count

# Nhập câu từ người dùng
sentence = input("Nhập câu: ")

# Tính số chữ hoa và chữ thường
upper, lower = count_upper_and_lower(sentence)

# In kết quả
print(f"Chữ hoa: {upper}")
print(f"Chữ thường: {lower}")
