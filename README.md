# Calendar Widget for use with python tkinter

<img align="left" src="https://github.com/Spartanlasergun/calendar_widget/blob/main/README_info/Calendar%20-%20Light%20Theme.png?raw=true">
<img align="right" src="https://github.com/Spartanlasergun/calendar_widget/blob/main/README_info/Calendar%20-%20Dark%20Theme.png?raw=true">

------

------

------

------

------

------

------

------

------

------

# INSTALLATION

##### Install the calendar widget using the following commands
```python
pip install calendar_widget
```

# USAGE

#### First, Import the calendar widget along with tkinter
```python
import tkinter
from calendar_widget import Calendar
```

##### Define the tkinter window into which the widget will be placed. EXAMPLE:
```python
root = tkinter.Tk()
root.geometry('600x600')
```

##### The Calendar Widget can then be created as follows:
```python
Calendar = Calendar(root)
```

##### To pass a command to the Calendar, specify the command option when it is created
```python
Calendar = Calendar(root, command=user_command, ...)
```

##### To retrieve a selected date on the calendar, use the get_date command:
```python
Calender.get_date()
```

##### To create a checkbox on the calendar, the command is as follows:
```python
checkbox = Calendar.checkboxes(10, 10, 2022, status=True, ...)

#to remove a chcekbox that has already been created specify the delete option as follows:

Calendar.checkboxes(10, 10, 2022, delete=True)
```

##### To destroy the calendar widget, call the destroy method:
```python
Calendar.destroy()
```

## Example 1 - Basic Setup

-----
<img align="right" src="https://github.com/Spartanlasergun/calendar_widget/blob/main/README_info/example_one.png?raw=true">

```python
# import tkinter and the calendar widget
import tkinter
from calendar_widget import Calendar

# define the main window into which the widget will be placed
root = tkinter.Tk()
root.geometry('600x600')  # the geometry function defines the size of the tkinter window
                          # - in this case, we are using a window that is 600px by 600px

# create the calendar widget
Calendar = Calendar(root, # specify the tkinter window into which the widget will be placed
	size = 250, # set the size of the calendar widget to 250px
	pos_x = 0, # set the x position of the calendar widget within the tkinter window
	pos_y = 0, # set the y position of the calendar widget within the tkinter window
	background = 'lightblue', # set the background of the calendar to light blue
	)

# Note: images of the type 'png', 'gif', 'ppm', and 'pgm' can be set as the background.
# However, these images will not scale with the size of the calendar.

# remember to call your mainloop function so that the tkinter window is persistent
root.mainloop()
```

Note: if no 'pos_x' or 'pos_y' parameters are given, the Calendar widget will default to using the standard pack function.

-----

## Example 2 - Binding a command to the calendar

-----

```python
# the 'Calendar_Click' function retrives the date selected on the Calendar by the user, and prints the date to the console
def Calendar_Click():
	print(Calendar.getdate())

# create the calendar widget
Calendar = Calendar(root,
	size = 250,
	pos_x = 0,
	pos_y = 0, 
	background = 'lightblue', 
	command = Calendar_Click  # link the 'Calendar_Click' function to the widget
	)
```

Note: Only a single command can be linked to the calendar widget.

-----

# Widget Parameters - functionality and styling

The table below specifies opitons availiable for styling and other operations associated with the calendar widget

| options | description |
| ------- | ----------- |
| size= | Sets the width of the widget in pixels. The default width is 300px. |
| pos_x= | Sets the x coordinate position of the widget within the window. Note: In tkinter, this is always the top left corner. |
| pos_y= | Sets the y coordinate position of the widget within the window. Note: In tkinter, this is always the top left corner. |
| style= | Set the style="Dark" for the dark theme. If no styling is specified the Calendar will inherit its default white theme. |
| command= | A function to be called when the widget is clicked. |
| background= | Sets the background of the Calendar to a valid tkinter colour or image (png, gif, ppm, pgm). Example: background="blue" or background='sky.png' |
| img_pos_x= | Set the x coordinate of the background image if specified (by default, this is the top left corner) |
| img_pos_y= | Set the y coordinate of the background image if specified (by default, this is the top left corner) |
| img_anchor= | Set the anchor of the background image if specified (by default, this is set to 'nw' - the top left corner) |
| arrow_box_border= | Sets the border colour of the box containing the arrows for selecting previous and following months. |
| arrow_box_fill= | Sets the background of the box containing the arrows for selecting previous and following months |
| arrow_box_width= | Sets the line width of the box containing the arrows for selecting previous and following months |
| date_box_fill= | Sets the colour inside of the boxes that make up the monthly calendar grid. |
| date_box_width= | Sets the width of the line used to create the grid for the monthly calendar. |
| date_boxes_outline= | Sets the colour of the box outline for the boxes that make up the monthly claendar grid. |
| arrow_outline= | Sets the colour for the outline of the polygon (i.e - triangle) that represents the calendar arrows. |
| arrow_fill= | Sets the colour of the calendar arrows. |
| arrow_thickness= | Sets the thickness of the calendar arrows. |
| arrow_active= | Sets the colour for the active highlight when the mouse hovers over the calendar arrows. |
| weekday_border= | Sets the colour for the outline of the boxes that hold the weekday headings. |
| weekday_fill= | Sets the colour for the background of the boxes that hold the weekday headings. |
| weekday_width= | Sets the width of the boxes that hold the weekday headings. |
| weekday_font_fill= | Sets the colour of the text associated with the weekday headings. |
| weekday_font_family= | Sets the type of font used to create the weekday headings. (Accepts any of the valid native tkinter fonts) |
| weekday_font_weight= | Sets the weight of the font used to create the weekday headings. Valid options are 'normal' or 'bold' |
| weekday_font_slant= | Sets the slant of the font used to create the weekday headings. Valid options are 'roman' or 'italic' |
| weekday_font_underline= | Sets the underline of the font used to creates the weekday heading. Valid options are True or False |
| calendar_date_title= | Sets the colour of the text associated with the calendar title (ex: Aug 2020) |
| date_heading_font_family= | Sets the font type for the Calendar date heading. (Accepts any of the valid native tkinter fonts) |
| date_heading_font_weight= | Sets the weight of the font used to create the Calendar date heading. Valid options are 'normal' or 'bold' |
| date_heading_font_slant= | Sets the slant of the font used to create the Calendar date heading. Valid options are 'roman' or 'italic' |
| date_heading_font_underline= | Sets the underline of the font used to create the Calendar date heading. Valid options are True or False |
| date_text_fill= | Sets the colour of the text numbers associated with the month dates. |
| date_text_font_family= | Sets the font type used to create the month dates. (Accepts any of the valid native tkinter fonts) |
| date_text_font_weight= | Sets the weight of the font used to create the month dates. Valid options are 'normal' or 'bold' |
| date_text_font_slant= | Sets the slant of the font used to create the month dates. Valid options are 'roman' or 'italic' |
| date_text_font_underline= | Sets the underline of the font used to create the month dates. Valid options are True or False |
| trail_box_fill= | Sets the colour of the background of the date boxes that trail into the previous and following months. |
| trail_text_fill= | Sets the colour of the text numbers associated with the trailing date boxes. |
| date_highlight= | Sets the colour of the permanent date highlight associated with the current date retrieved from the OS. |
| text_highlight_fill= | Sets the colour of the text associated with the permanent date highlight. |
| user_highlight_colour= | Sets the colour of the highlight that is created when the user clicks on a month date. |
| user_highlight_text= | Sets the colour of the text associated with the user highlight. |

