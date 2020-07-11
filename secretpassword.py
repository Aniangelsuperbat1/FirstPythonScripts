# want the user to guess the secret password
# only allowed three guesses

Secret_Password = ("Python!")
correct_guess = False

for _ in range(3):
    user_input = input("what is the password:")
    if user_input != Secret_Password:
        print("invaild password, please try again")
    elif user_input == Secret_Password:
        print("Valid password, congratulations. You are not the weakest link you may enter")
        correct_guess = True
        break
    print("")
if correct_guess == False:
    print("try again in 10 years")

# Want this code to execute ONLY after the user has tried three times
#print("you have tried too many times, wait 10 years before you can try again")
