import sys
sys.path.append('C:/Users/bns36/Documents/calendar_widget/src/calendar_widget')

import tkinter
from Calendar_Widget import Calendar


root = tkinter.Tk()
root.geometry('600x600')

def Calendar_Click():
	print(Calendar.getdate())


Calendar = Calendar(root)

Calendar.checkboxes(8, 4, 2023, status=True)
Calendar.checkboxes(31, 3, 2023, status=False)

root.mainloop()