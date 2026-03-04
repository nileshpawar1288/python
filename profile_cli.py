print("========profile creator======== ")
name = input("Enter your name: ")
age = input("Enter your age: ")
height = input("Enter your height: ")       
city = input("Enter your city: ")

is_adult = int(age) >= 18

print("\n========profile summary======== ")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"City: {city}")
print(f"Is Adult: {is_adult}")