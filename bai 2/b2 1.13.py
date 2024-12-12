print("Sinh viên:Tran Duc An")
print("MSSV:215748020110273")
print("####################")
############################

a = float(input("Nhap he so a:"))
b = float(input("Nhap he so b:"))
c = float(input("Nhap he so c:"))
delta = b*b - 4*a*c
if delta < 0:
    print ("phuong trinh vo nghiem")
elif delta == 0:
    print("phuong trinh co nghiem kep x1 = x2= ",-(b/2*a))
else:
    import math
    print("x1 = ",(-(b) + math.sqrt(delta))/(2*a))
    print("x2 = ",(-(b) - math.sqrt(delta))/(2*a))
