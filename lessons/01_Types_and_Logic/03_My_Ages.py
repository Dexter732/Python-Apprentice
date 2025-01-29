
"""
Am I Big Yet?

Ask the user's age then use an if-elif-else statement to 
tell the user what age groups the user is in. The groups are:

0-2: Baby
3-5: Toddler
6-12: Child
13-19: Teen
20-64: Adult
65+: Senior

Except, if the user is the same age as you, print "You are pretty awesome!"


Here is how you ask the user's age in integer format.  The first argument is 
the title of the window, the second is the message to the user.

age = simpledialog.askinteger("Your Age", "How old are you?") 

Or, you could ask the user for a float with simpledialog.askfloat() 

age =  simpledialog.askfloat("Your Age", "How old are you?")


Here is how you show the user a message window. The first parameter is the title of the window, 
the second is the message to show the user.

messagebox.showinfo('What you are', "You are a baby.")

"""

from tkinter import messagebox, simpledialog, Tk # import required modules
print("Hello World")

window = Tk()     # Create a window object
window.withdraw() # Hide the window; we just want to see pop ups

# Ask the user's age
age =  simpledialog.askfloat("Your Age", "How old are you?")
# Use if statements to determine the age group
if age >= 0 and age <= 2:
    messagebox.showinfo('You are a', "big baby")
if age >= 3 and age <= 5:
    messagebox.showinfo('You are a', 'toddler')
if age >= 6 and age <= 12:
    messagebox.showinfo('You are a', 'child')
if age >= 13 and age <= 19:
    messagebox.showinfo('You are a', 'Teen you are cool')
if age >= 20 and age <= 64:
    messagebox.showinfo('You are a', 'adult')
if age >= 65:
    messagebox.showinfo('You are a', 'old guy')
# and create a message

# Show the message to the user



window.mainloop()  # Keeps the window open


# TODO: 
# Try to write your program so you only need to use one messagebox.showinfo() function.
