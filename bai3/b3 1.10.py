print("Sinh viên:Tran Duc An")
print("MSSV:215748020110273")
print("####################")
############################

import math
while True:
    radius =input ("Nhập bán kính của hình tròn: ")
    try:
      radius = float(radius)
      if radius <= 0:
            print ("Bán kính  nhập không hợp lệ!.")
            continue
      break
    except ValueError:
     print("Bán kính phải là một số .")
# Tính diện tích hình tròn
area = math.pi * radius**2
#Tính chu vi hình tròn
circumference = 2 * math.pi * radius
print (f"Diện tích hình tròn là: {area:.2f}")
print (f"Chu vì hình tròn là: {circumference:.2f}")
