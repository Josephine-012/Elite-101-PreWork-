def greet_user(name):
    print(f"Hello, {name}!")
def ask_email(email):
    print(f"Your email is, {email}!")
def ask_plan(plan):
    print(f"I can help you with, {plan}!")

print("Welcome to the Edikted Help Chat")
name=input("Please enter your name: ")
greet_user(name)

email=input("Please enter what email your account is under: ")
ask_email(email)

plan=input("Are you planning on returning or exchanging an item today?: ")
ask_plan(plan)

ask=input("Has been less than 30 days since your purchase?: ")
if ask=='yes':
    tell=input("Okay please continue!")
    ask=input("What is the item's name?: ")
    choose=input("Check your email for the return label and check in at your local store or mail the package back! ")
if ask=='no':
    tell=input("Sorry, you are unable to return or exchange this item")