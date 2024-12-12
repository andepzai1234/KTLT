print("Sinh viên: Tran Duc An")
print("MSSV: 215748020110273")
print("####################")

# Hàm để đếm số chữ cái và chữ số trong câu
def count_letters_and_digits(sentence):
    letter_count = 0
    digit_count = 0
    
    # Duyệt qua từng ký tự trong câu
    for char in sentence:
        if char.isalpha():  # Kiểm tra nếu ký tự là chữ cái
            letter_count += 1
        elif char.isdigit():  # Kiểm tra nếu ký tự là chữ số
            digit_count += 1
    
    return letter_count, digit_count

# Nhập câu từ người dùng
sentence = input("Nhập câu: ")

# Tính số chữ cái và chữ số
letters, digits = count_letters_and_digits(sentence)

# In kết quả
print(f"Số chữ cái là: {letters}")
print(f"Số chữ số là: {digits}")
