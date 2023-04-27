import sys
sys.path.append('C:/Users/bns36/Documents/calendar_widget/src/calendar_widget')

import tkinter
from Calendar_Widget import Calendar


root = tkinter.Tk()
root.geometry('600x600')

def Calendar_Click():
	print(Calendar.getdate())

Calendar = Calendar(root,
	command = Calendar_Click,
	size=300,
	#current_date_highlight=False, # fixed issue #2 - permanent date highlight can be toggled on/off
	#weekday_font_size=15,         # fixed issue #8 - font size can now be specified and overidden
	#date_heading_font_size=15,
	#date_text_font_size=7,
	#trail_box_fill=None,          # fixed issue #14 - calendar grid can now be completely transparent
	#date_box_fill='white',
	#date_box_width=0,
	#date_boxes_outline='green'
	)

Calendar.checkboxes(8, 4, 2023, status=True)

root.mainloop()