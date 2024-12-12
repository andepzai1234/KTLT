print("Sinh viên: Tran Duc An")
print("MSSV: 215748020110273")
print("####################")

class HinhChunhat:
    def __init__(self, chieu_dai, chieu_rong):
        # Khởi tạo với chiều dài và chiều rộng
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def dien_tich(self):
        # Phương thức tính diện tích hình chữ nhật
        return self.chieu_dai * self.chieu_rong

# Ví dụ sử dụng:
hcn = HinhChunhat(5, 3)  # Khởi tạo đối tượng HinhChunhat với chiều dài 5 và chiều rộng 3
print("Diện tích hình chữ nhật là:", hcn.dien_tich())
