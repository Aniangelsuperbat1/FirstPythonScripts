# want the user to guess the secret password
# only allowed three guesses

Secret_Password = ("Python!")
print("what is the password:")

for Password in range(4):
    Password = input()
    if Password != Secret_Password:
        print("invaild password, please try again")
    elif Password == Secret_Password:
        print("Valid password, congratulations. You are not the weakest link you may enter")
        break


# Want this code to execute ONLY after the user has tried three times
#print("you have tried too many times, wait 10 years before you can try again")
