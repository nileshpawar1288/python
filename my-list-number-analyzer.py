#Concepts used:

#slicing

#reversing

#indexing


from matplotlib.pylab import number


numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("numbers:", numbers)
print("First Number:", numbers[0])
print("Last Number:", numbers[-1])
print("Sliced List (2 to 5):", numbers[2:6])
print("Reversed List:", numbers[::-1])
print("Even Indexed Numbers:", numbers[::2])
print("Odd Indexed Numbers:", numbers[1::2])
print("Sum of Numbers:", sum(numbers))
print("Average of Numbers:", sum(numbers) / len(numbers))
print("Maximum Number:", max(numbers))
print("Minimum Number:", min(numbers))
print("First three Numbers>:", numbers[:3])
print("last three Numbers:", numbers[-3:])
