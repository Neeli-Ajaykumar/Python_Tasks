"""Basic File Logger 
Scenario: 
A system logs user actions. 
Task: 
● Take user input 
● Store logs in a file 
● Use loop to allow multiple entries 
● Handle file errors using exception handling """

while True:
    try:
        user = input("Enter user action:")
        if user == "exit":
            print("logging stopped:")
            break

        file = open("log.txt", "a")
        file.write(user + "\n")
        file.close()
        print("Action logged successfully")

    except:
        print("Error while writing to file")
