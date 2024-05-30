x = int(input("X: "))
y = int(input("Y: "))
action = input("what do you want to do?(+, -, *, /): ")

if(action == "+"):
    answer = x + y
elif(action == "-"):
    answer = x - y
elif(action == "*"):
    answer = x * y
elif(action == "/"):
    answer = x / y

print(f"Answer: {answer}")

