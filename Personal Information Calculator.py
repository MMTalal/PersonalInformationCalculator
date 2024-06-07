# Personal Information Calculator
# This program calculates personal information based on user input.
# Print the title of the program
print("Personal Information Calculator")
print("-" * 30)

# Prompt the user to enter their name
# Collect the user's first, middle, and last name, capitalizing and stripping whitespace
FirstName = input("What\'s your first name ?").capitalize().strip()
MiddleName = input("What\'s your middle name ?").capitalize().strip()
LastName = input("What\'s your lastname ?").capitalize().strip()
# Welcome the user and print their full name
print(f"Welcome {FirstName} {MiddleName:.1s}. {LastName} in your python world, here your Personal Information Calculator\n")

# Prompt the user to enter their E-mail
# Collect the user's email address and extract the username, website, and domain
Email = input("What\'s your E-mail ?").strip()
UserName = Email[0:Email.index("@")]
Website = Email[Email.index("@") + 1:]
Domain = Email[Email.index(".") + 1:]
# Print the user's username, website, and domain
print(f"Your User Name is {UserName}\nYour website is {Website}\nYour Domain is {Domain}\n")

# Prompt the user to enter their age
# Collect the user's age and calculate various time metrics
Age = int(input("How old are you ?").strip())
Months = Age * 12
Weeks = Age * 52
Days = Age * 365
Hours = Days * 24
Minutes = Hours * 60
Seconds = Minutes * 60
# Print the user's age and the various time metrics
print(f"Your Age is {Age} year, and You almost lived around for:-\n{Months} Months.\n{Weeks} Weeks.\n{Days} Day.\n{Hours} Hours.\n{Minutes} Minutes.\n{Seconds} Seconds.\nI wish you a long year of good health.\n")

# Thank the user for their experience
print(f"Thank you {FirstName} for your experience with me.")