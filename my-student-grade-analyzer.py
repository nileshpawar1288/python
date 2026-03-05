grades = [78, 85, 90, 72, 88, 95, 80, 82, 91, 87, 94, 89, 92, 84, 86]

print("Grades:", grades)
print("total number of students:", len(grades))
print("heighest grades:", max(grades))
print("lowest grades:", min(grades))
print("average grades:", sum(grades) / len(grades))
print("First 3 grades:", grades[:3])
print("grades in reverse order:", grades[::-1])
print("grades in acsending order:", sorted(grades))
print("grades in descending order:", sorted(grades, reverse=True))
