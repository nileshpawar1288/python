lat = float(input("enter lattitude: "))
lon = float(input("enter longitude: "))

if -90 <= lat <= 90 and -180 <= lon <= 180:
    print("valid coordinate location")
else:
    print("Invalid coordinates")    