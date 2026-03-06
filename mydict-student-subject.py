student = {
    "name": "John",
    "subjects": ["math", "physics", "chemistry"]
}

print("Student:", student["name"])

print("Subjects:")

for subject in student["subjects"]:
    print(subject)
    print("Subject length:", len(subject))
    print("Subject in uppercase:", subject.upper())
    print("Subject in lowercase:", subject.lower())
    print("Subject with first letter capitalized:", subject.capitalize())
    print("Subject with replaced 'a' with '@':", subject.replace("a", "@"))
    print("Subject with 's' replaced with 'z':", subject.replace("s", "z"))
    print("Subject with 'c' replaced with 'k':", subject.replace("c", "k"))
    print("Subject with 'h' replaced with 'H':", subject.replace("h", "H"))
    print("Subject with 'm' replaced with 'M':", subject.replace("m",   "M"))