# Set access to False by default
access = False

# Store approved users and their credentials
approved_users = {
    "Bob": "company1",
    "Sarah": "company2"
}

# Set the maximum number of attempts
max_attempts = 3

# Start the attempt counter
attempt = 1


# Repeat the login process while attempts remain
while attempt <= max_attempts:

    # Ask for username
    username = input("Enter your username: ")

    # Check if username is approved
    if username in approved_users:

        # YES PATH: username is approved
        password = input("Enter your password: ")

        # Look up the approved credential
        approved_users[username]

        # Check if password is correct
        if password == approved_users[username]:
            print("Welcome back! You're logged in.")
            access = True
            break

        # NO PATH: password is incorrect
        else:
            # Use an f-string to insert the current attempt values into the message
            print(f"Access denied. Attempt {attempt} of {max_attempts}")
            access = False
            attempt += 1

            # Check whether maximum attempts have been exceeded
            if attempt > max_attempts:
                print("Maximum login attempts reached. Your account is locked.")
                break

    # NO PATH: username is not approved
    else:
        # Use an f-string to insert the current attempt values into the message
        print(f"Access denied. Attempt {attempt} of {max_attempts}")
        access = False
        attempt += 1

        # Check whether maximum attempts have been exceeded
        if attempt > max_attempts:
            print("Maximum login attempts reached. Your account is locked.")
            break
