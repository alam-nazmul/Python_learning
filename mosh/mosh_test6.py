number_of_guesses = 0
secret_number = 7

while number_of_guesses < 3:
    number_of_guesses = number_of_guesses +1
    user_input =  input("Please enter your secret: ")
    user_input = int(user_input)
    if user_input == secret_number:
        print(f'You Won ... Your guess number is {user_input}')
        break
else:
    print("Sorry, you failed")




# while number_of_guesses < 3:
#     number_of_guesses = number_of_guesses +1
#     user_input =  input("Please enter your secret: ")
#     user_input = int(user_input)
#     if user_input != secret_number:
#         print("Please try again")
#     else:
#         print(f'You Won ... Your guess number is {user_input}')