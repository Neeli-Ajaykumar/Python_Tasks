""" Decorator-based Access Control 
Scenario: 
Restrict access to certain functions. 
Task: 
● Create a decorator to check user role 
● Use condition inside decorator 
● Apply decorator to multiple functions 
● Store roles in a dictionary """

users = {"Ajay": "admin", "Bubby": "user", "Naresh": "guest"}

def check_role(required_role):
    def decorator(func):
        def wrapper(username):
            
            if users.get(username) == required_role:
                return func(username)
            else:
                print("Access Denied for", username)

        return wrapper
    return decorator

@check_role("admin")
def delete_data(username):
    print(username, "deleted data")

@check_role("user")
def view_data(username):
    print(username, "viewed data")
delete_data("Ajay")
delete_data("Bubby")

view_data("Bubby")
view_data("Naresh")
