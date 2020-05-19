import subprocess
from turtle import Shape, Turtle, mainloop, Vec2D as Vec

print("PACMAN")
print("Please type the following commands")
print("PLAY")
print("ABOUT")
print("EXIT")
option = input("Enter your choice: ").lower()
if option == "play":
    subprocess.call(['python', 'files/game.py'])
if option == "about":
    writer = Turtle()
    writer.ht()
    writer.pu()
    writer.goto(1,1.15)
    writer.write("\n\nThis game was made by hamza\n\nVISIT:\nFacebook: facebook.com/frndbros\nInstagaram: instagram.com/devoloper_of_insta\nWebsite: friendbros.blogspot.com",align="center",font=("Arial",30,("bold","italic")))
if option == "exit":
    input("press the close button to close")
input("press enter to exit")
