import sys
sys.path.append('C:/Users/bns36/Documents/calendar_widget/src/calendar_widget')

import tkinter
from Calendar_Widget import Calendar


root = tkinter.Tk()
root.geometry('600x600')

def Calendar_Click():
	print(Calendar.getdate())

Calendar = Calendar(root,
	date_heading_font_weight='normal',
	date_text_font_weight='normal',
	weekday_font_weight='normal',
	date_heading_font_slant='roman',
	date_text_font_slant='roman',
	weekday_font_slant='roman',
	weekday_font_underline=False,
	date_heading_font_underline=False,
	date_text_font_underline=False,
	command=Calendar_Click)

root.mainloop()