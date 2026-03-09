#Project: Student Result Management System

#This project uses:

#if

#elif

#else

#nested conditions

#input

#type conversion

#basic calculations

#formatted output

#It will:

#ask student details

#ask marks for 3 subjects

#calculate total

#calculate percentage

#assign grade

#decide pass/fail

#decide distinction / first class / second class

#check voting eligibility

#print final report


print("==========Student Result Management System======== ")

#student details
name = input("Enter student name: ")
age = int(input("Enter the student age: "))
student_class = input("Enter the student class: ")

#marks for 3 subjects
maths_marks = float(input("Enter maths marks: "))
science_marks = float(input("Enter science marks: "))
english_marks = float(input("Enter english marks: "))

#total marks and percentage
total_marks = maths_marks + science_marks + english_marks
percentage = (total_marks / 300) * 100

# pass / fail decision
if maths_marks >= 35 and science_marks >= 35 and english_marks >= 35:
    result = "pass"
else:
    result = "fail"


# grade assignment

if percentage >= 90:
    grade ="A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

# aGE-BASED MESSAGE     
if age >= 18:
    voting_eligibility = "eligible to vote"
else:
    voting_eligibility = "not eligible to vote"

#SPECIAL PERFORMANCE MESSAGE
if result == "Fail":
    performance_message = "Needs improvement. Work harder next time."
elif grade == "A+":
    performance_message = "Outstanding performance! Keep it up!"
elif grade == "A":
    performance_message = "Excellent work! Great job!"
elif grade == "B":
    performance_message = "Good job! You can do even better!"           
elif grade == "C":
    performance_message = "Fair performance. Aim for higher grades!"
elif grade == "D":
    performance_message = "Passable, but there's room for improvement."
else:
    perfornmance_message = "pass, but try to improve your grades next time."


#scholarship eligibility
if result == "Pass":
    if percentage >= 85:
        scholarship_eligibility = "eligible for scholarship"
    elif percentage >= 70:
        scholarship_eligibility = "considered for scholarship"
    else:
        scholarship_eligibility = "not eligible for scholarship"
else:
    scholarship_eligibility = "not eligible for scholarship"


    #print final report
print("\n==========Final Report======== ")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Class: {student_class}")

print("\===========Marks======== ")
print(f"Maths: {maths_marks}")
print(f"Science: {science_marks}")
print(f"English: {english_marks}")

print("\===========Results======== ")
print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")
print(f"result: {result}")
print(f"Grade: {grade}")
print(f"Division: {division}")
print(f"Voting Eligibility: {voting_eligibility}")
print(f"Performance Message: {performance_message}")


#final topper-Level note

if result == "Pass" and percentage >= 90:
    print("Special Note:Congratulations! You are among the top performer.")
elif result == "Pass" and percentage >= 80:
    print("Special Note:Great job! You are performing very well.")
else:
    print("Special Note:Keep working hard to improve your performance.")
