print("Sinh viên: Tran Duc An")
print("MSSV: 215748020110273")
print("####################")

class Chuoi:
    def __init__(self):
        self.string = ""

    def get_String(self):
       
        self.string = input("Nhập chuỗi: ")

    def print_String(self):
       
        print("Chuỗi in hoa:", self.string.upper())
        
chuoi = Chuoi()

chuoi.get_String()

chuoi.print_String()
