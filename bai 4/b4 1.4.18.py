print("Sinh viên:Tran Duc An")
print("MSSV:215748020110273")
print("####################")
############################

n = int(input("Nhap so nguyen n: "))
fib = [0,1]
while fib[-1] < n:
    fib.append(fib[-1] + fib[-2])
fib = fib[:-1]
print("Cac so Fibonacci nho hon", n, "la:")
print(fib)
