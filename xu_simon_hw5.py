#10-1 learning python


filename = 'learning_python.txt'

with open(filename) as file_object:
    contents = file_object.read()
    print(contents * 3)


with open(filename, 'r') as file_object:
    for line in file_object:
        print(line, end='')


with open(filename, 'r') as file_object:
    lines = file_object.readlines()

#10-2 learning c
message = """In python you can create functions.
In python you can use conditionals such as if else statements.
In python you can create variables to store data.
In python you can write comments."""

replaced = message.replace('python', 'c')

print(replaced)


#10-3  guest

name = input('whats your name: ')

with open('guest.txt', 'w') as file_object:
    file_object.write(name)


#10-4 guest book

while True:
    name = input("what's your name? type 'quit' to quit: ")
        
    if name == 'quit':
            break
    else:
        with open('guest_book.txt', 'a') as file:
            file.write(name + '\n')
        print(f"greetings {name}")        
        
        

#10-5 programming poll

filename = 'programming_poll.txt'

response =[]
while True:
    poll = input("why do you like programming? type 'quit' to quit: ")
    response.append(poll)
    if poll == 'quit':
            break

with open(filename, 'w') as file:
    file.write(poll + '\n')


#10-6  addition

try:
    x = input("enter first number: ")
    x = int(x)

    y = input("enter second number: ")
    y = int(y)

except ValueError:
    print("only numbers please")

else:
    sum = x + y
    print("The sum of " + str(x) + " and " + str(y) + " is " + str(sum) + ".")

#10-7 addition calculator


print("type 'quit' to quit the program \n")
while True:
    try:
        x = input("Enter a number ")
        if x == 'quit':
            break

        x = int(x)

        y = input("Enter another number: ")
        if y == 'quit':
            break

        y = int(y)

    except ValueError:
        print("Only enter a number")

    else:
        sum = x + y
        print(f"{str(x)} + {str(y)} is equal to {str(sum)}")
