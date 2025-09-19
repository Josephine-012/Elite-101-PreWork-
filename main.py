def greet_user(name):
    print(f"Hello, {name}!")
def ask_age(age):
    print(f"You're, {age}!")
def ask_help(help):
    print(f"I can help you with, {help}!")
def choose_option(option):
    print(f"I can help you contiue this conversation by, {option}!")

print("Welcome to the Elite 101 Chatbot")
name=input("Please enter your name: ")
age=input("Please enter your age: ")
ask=input("What can I help you with: ")
choose=input("Choose from this option menu: Placeholder1, Placeholder 2, Placeholder 3: ")


greet_user(name)
ask_age(age)
ask_help(ask)
choose_option(choose)