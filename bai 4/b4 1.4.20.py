print("Sinh viên: Tran Duc An")
print("MSSV: 215748020110273")
print("####################")

def pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)  # Phần tử đầu và cuối của mỗi dòng là 1
            else:
                # Cộng hai phần tử phía trên của dòng trước để tạo ra giá trị mới
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)

    # In tam giác Pascal
    for row in triangle:
        print(' '.join(str(num) for num in row))

# Nhập số hàng của tam giác Pascal
n = int(input("Nhap n : "))
pascal_triangle(n)
