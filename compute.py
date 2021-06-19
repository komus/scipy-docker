from calculator import Calculator

my_cal = Calculator()


print(my_cal.sum(10))

my_cal.reset

print(my_cal.sum(10, 2))
print(my_cal.sum(2))
print(my_cal.sum([10, 12.90, 14, 5, 7]))

my_cal.reset

print(f"{my_cal.sum(3, 2)}")

my_cal.reset

print(my_cal.subtract(5))
my_cal.reset
print(my_cal.subtract(10, 4))
print(my_cal.subtract(2))
print(my_cal.subtract(3, 1))

val = [2, 4, 5, 2, 1]
print(my_cal.multiply(1000))
print(my_cal.multiply(val))
print(my_cal.multiply(10, 4))
print(my_cal.multiply(12, 2))
print(my_cal.subtract(4))

print(my_cal.divide(100, 5))
print(my_cal.sum(10))
print(my_cal.divide(2))
print(my_cal.divide(0))
print(my_cal.divide(10.78, 0))
print(my_cal.divide(0, 78))

print(my_cal.modulo(10, 2))
print(my_cal.modulo(15, 4))
print(my_cal.modulo(10, 0))
print(my_cal.modulo(14.67, 3))

my_cal.reset
print(my_cal.root(16, 2))

print(my_cal.power(5, 3))
print(my_cal.power(3.5, 3))
print(my_cal.power(2, 5))

