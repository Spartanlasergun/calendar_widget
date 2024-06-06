import tkinter
from calendar_widget import Calendar

# define the main window into which the widget will be placed
root = tkinter.Tk()
root.geometry('600x600')  # the geometry function defines the size of the tkinter window
                          # - in this case, we are using a window that is 600px by 600px

# the 'Calendar_Click' function retrives the date selected on the Calendar by the user, and prints the date to the console
def Calendar_Click():
	print(Calendar.getdate())

# create the calendar widget
Calendar = Calendar(root, # specify the tkinter window into which the widget will be placed
	pos_x = 0, # set the x position of the calendar widget within the tkinter window
	pos_y = 0, # set the y position of the calendar widget within the tkinter window
	background = 'lightblue', # set the background of the calendar to light blue
	command = Calendar_Click  # link the 'Calendar_Click' function to the widget
	)

# Note: images of the type 'png', 'gif', 'ppm', and 'pgm' can be set as the background.
# However, these images will not scale with the size of the calendar.

# remember to call your mainloop function so that the tkinter window is persistent

current_date = Calendar.getdate_today()
print(current_date)

root.mainloop()
