#concept used:
#list
#len()
#math 
#aggregation

print("========Student Marks Analyzer========")

marks = [78, 85, 90, 66, 21, 95, 88, 76, 92, 80]

print("student marks:",marks)
print("total student:", len(marks))
print("Highest marks:", max(marks))
print("Lowest marks:", min(marks))
average = sum(marks) / len(marks)

print("Average marks:", average)

