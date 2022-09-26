import datetime
import random

# Create module
def createCredentials(usernameInput, pwdLength):
    src     = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*?~" #random strings for pwd generator
    rndmPwd = "".join(random.sample(src, pwdLength)) #randomize pwd process
    
    xDate   = datetime.datetime.now()

    msgShow = """Successfully generated your credentials!
    Here is your credentials:
    Username: {unameGenerated} | Password: {pwdGenerated}
    Do not share this to ANYONE! Remember, passwords are case sensitive.
    *Generated on {dateTime}"""

    f = open("generatedCredentials.txt", "w")
    f.write(msgShow.format(
        unameGenerated = usernameInput,
        pwdGenerated = rndmPwd,
        dateTime = xDate.strftime("%c")
    ))
    f.close()

    # f = open("generatedCredentials.txt", "r")
    # print(f.read())
    print("Password generated, please check your directory!")

# User manual input
unameInput  = input("Type username: ")
pwdInput    = int(input("Type password length: "))

# Run module
createCredentials(unameInput, pwdInput)
