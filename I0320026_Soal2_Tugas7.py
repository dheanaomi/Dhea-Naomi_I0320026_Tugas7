string = "Program Menghitung Volume dan luas permukaan kubus"
i = string.center(55,'*')
print(i)
import math

s = float(input('Masukkan sisi : '))

luaspermukaan = math.sqrt (6**2)
print("luas permukaan kubus :",math.floor(luaspermukaan))
volume = (s**3)
volume = math.ceil(volume)
print("Volume kubus: ",math.ceil(volume))
