"""
This code represents to check the items of a dictionary within the items of a larger dictionary
Bu kod, bir sözlüğün maddelerini daha büyük bir sözlüğün maddeleri içinde arar
"""

# Username and password items
users={"Ali":"Ali1", "Veli":"Veli1", "Hasan":"Hasan1"}

user_mail=input("Username: ")
user_psw=input("Password: ")

# Define the inputs into a tuple object
user_input={user_mail:user_psw}

# Check whether input items exist in user items
if all(item in users.items() for item in user_input.items()):
    print("Correct")
else:
    print("Mistake")

