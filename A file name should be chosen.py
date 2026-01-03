import math

angle_degrees = int(input("Enter a number: "))

angle_radians = math.radians(angle_degrees)

sine_value = math.sin(angle_radians)
cos_value = math.cos(angle_radians)

print(f"The sine of {angle_degrees} degrees is: {sine_value}")
print(f"The cos of {angle_degrees} degrees is: {cos_value}")