# class Temperature:
#     def __init__(self,celsius):
#         self.celsius=celsius 
#     def to_fahrenetie(self,celsius):
#          return (self.celsius * 9/5) + 32
#     def to_kelvin(self,kelvin):
#         return self.kelvin + 273.15
         
# ciel=float(input("enter your temprature in celsius :"))
# c=Temperature(ciel)
# print("fahranite",c.to_fahrenetie(c))
# print("kelvin:",c.to_kelvin(c))           

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32

    def to_kelvin(self):
        return self.celsius + 273.15


c = float(input("Enter Tempreture in Celsius: "))

temp = Temperature(c)

print("Temperature in Fahrenheit:", temp.to_fahrenheit())
print("Temperature in Kelvin:", temp.to_kelvin()) 