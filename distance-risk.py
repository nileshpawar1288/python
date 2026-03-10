distance = float (input("disatace to  river(m): "))

if distance <= 100:
    print("High Flood Risk")
elif distance <= 500:
    print("Medium Flood Risk")
else:      
    print("Low Flood Risk")