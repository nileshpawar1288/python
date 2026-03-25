try:
    answer = input("what should i divide 10 by?")
    num = int(answer)
    print(10/num)
except ZeroDivisionError as e:
    print("You can't divide by zero")
except ValueError as e:
    print("You didnt give me a valid number")
    print(e)
finally:
    print("Finaly always run")             