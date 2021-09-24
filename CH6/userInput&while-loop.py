message = input("Tell me something, and I will repeat it back to you: ")
print(message)

##########################################################################

message = int(input("How old are you? "))
print(message > 18)  # True

current_num = 0
while current_num <= 5:
    print(current_num)
    current_num += 1

##########################################################################

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
message = ""

while message != "quit":
    message = input(prompt)
    if message != "quit":
        print(message)

##########################################################################

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

active = True

while active:
    message = input(prompt)
    if message == "quit":
        active = False
    else:
        print(message)

##########################################################################

# break & continue

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

active = True

while active:
    message = input(prompt)
    if message == "quit":
        break
    else:
        print(message)

##########################################################################

current = 0

while current <= 10:
    current += 1
    if current % 2 != 0:
        continue

    print(current)

##########################################################################

# 使用while循环处理列表和字典

unconfirmed_user = ['alice', 'brain', 'candace']
confirmed_user = []

while unconfirmed_user:
    current_user = unconfirmed_user.pop()

    print(f'Verifying user: {current_user.title()}')
    confirmed_user.append(current_user)

print('\nThe following users have been confirmed:')
for user in reversed(confirmed_user):
    print(user.title())

##########################################################################

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

##########################################################################

responses = {}

polling = True

while polling:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")


