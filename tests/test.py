import sys
sys.path.append('C:/Users/bns36/Documents/calendar_widget/src/calendar_widget')

import tkinter
from Calendar_Widget import Calendar


root = tkinter.Tk()
root.geometry('600x600')

Calendar = Calendar(root)

root.mainloop()