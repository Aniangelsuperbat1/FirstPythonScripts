# want code to have user input to guess the password
# only want the user to guess three times
# after 3 gusses tyep "try again in 10 years"

secret_password = "python"
count = 0
guess_taken = 3
correct_guess = False

while count < guess_taken:
    user_input = input("what is the password:")
    count = count + 1
    if user_input != secret_password:
        print("invaild password, please try again")
    elif user_input == secret_password:
        correct_guess = True
        break
if correct_guess == False:
    print("try again in 10 years")
