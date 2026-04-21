"""2. Notes Reader Program 
A student stores daily notes in a file called notes.txt. Write a program that opens the 
file, reads all the contents, and displays them on the screen. """

with open("notes.txt", "r") as file:
    content = file.read()
    print("Notes:", "\n" ,content)
