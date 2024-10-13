# collect email from the user
# split the email using the @, the first part as the username, the second part is gonna be saved as domain
# split domain using .,


def main():
    print("Welcome to the Email Slicer")
    print("")

    email_input = input("Input the email address: ")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("Username : ", username)
    print("Domain : ",domain)
    print("Extension : ", extension)

while True:
    main()