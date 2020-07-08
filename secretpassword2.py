# want code to have user input to guess the password
# only want the user to guess three times
# after 3 gusses tyep "try again in 10 years"

secret_password = "python"
guess_taken = 3
guess_taken = guess_taken + 1
print("what is the password:")

while guess_taken != secret_password:
    input()
    if guess_taken != secret_password:
        print("invaild password, please try again")
    elif guess_taken == secret_password:
        break
    else:
        print("try again in 10 years")
