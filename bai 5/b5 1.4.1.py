print("Sinh viên: Tran Duc An")
print("MSSV: 215748020110273")
print("####################")

# Math functions
def square(x):
    return x * x

def cube(x):
    return x * x * x

def average(values):
    return sum(values) / len(values)

# Main script
values = [2, 4, 6, 8, 10]
print('Squares:')
for v in values:
    print(square(v))
print('Cubes:')
for v in values:
    print(cube(v))
print('Average: ' + str(average(values)))
