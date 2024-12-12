print("Sinh viên: Tran Duc An")
print("MSSV: 215748020110273")
print("####################")

class Nguoi:
    def __init__(self, ten):
        # Khởi tạo với tên
        self.ten = ten

    def getGender(self):
        # Phương thức chung cho tất cả các lớp con (sẽ được ghi đè)
        pass

class Nam(Nguoi):
    def __init__(self, ten):
        # Khởi tạo với tên, sử dụng constructor của lớp cha
        super().__init__(ten)

    def getGender(self):
        # Phương thức của lớp Nam, in ra "Nam"
        return "Nam"

class Nu(Nguoi):
    def __init__(self, ten):
        # Khởi tạo với tên, sử dụng constructor của lớp cha
        super().__init__(ten)

    def getGender(self):
        # Phương thức của lớp Nu, in ra "Nữ"
        return "Nữ"

# Ví dụ sử dụng:
nam = Nam("Tran Duc An")
nu = Nu("Nguyen Kieu Trang")

print(f"{nam.ten} là giới tính: {nam.getGender()}")
print(f"{nu.ten} là giới tính: {nu.getGender()}")
