print("Sinh viên:Tran Duc An")
print("MSSV:215748020110273")
print("####################")
############################

def sum_of_divisors(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum
n = int(input("Nhap so n: "))

for i in range(1, n):
    if sum_of_divisors(i) > i:
        print(i)
