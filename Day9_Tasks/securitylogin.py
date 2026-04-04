"""Secure Login System (Decorators) 
A web application wants to ensure that users are authenticated before accessing 
sensitive functions. Create a decorator that checks whether the user is logged in before 
allowing access to a function."""

user = {"name": "Ajay", "logged_in": True}
def login_required(func):
    def wrapper(user):
        if user["logged_in"]:
            return func(user)
        else:
            return "Access denied user not logged in."
    return wrapper

@login_required
def view_data(user):
    return f"Welcome {user['name']}! Here is your data."

print(view_data(user))
