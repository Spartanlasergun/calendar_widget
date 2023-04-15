import tkinter
import calendar
from tkinter import font
from datetime import date

# Main Class for Calendar Widget. All of its methods are encapsulated within this single class
class Calendar:

    # The init function parameters describe the information that dictates the size, position and styling associated with
    # the calendar object. Comments associated with the usage of each parameter is given within the __init__ function
    # where they are first defined and used.
    def __init__(self, window_name, pos_x=0, pos_y=0, size=300, style=None, command="no command",
                 background="white", calendar_relief="flat",
                 arrow_box_border="black", arrow_box_fill="white", arrow_box_width=1,
                 date_box_border="black", date_box_fill="white", date_box_width=2, date_boxes_outline="black",
                 arrow_outline="black", arrow_fill="white", arrow_thickness=1, arrow_active="orange",
                 weekday_border="gray50", weekday_fill="black", weekday_width=2, weekday_font_fill="white",
                 calendar_date_title="black", date_text_fill="black", trail_box_fill="gray83", trail_text_fill="black",
                 date_highlight="orange", text_highlight_fill="black", weekday_font_family="Algerian",
                 date_heading_font_family="Garamond", date_text_font_family="Arial CE", user_highlight_colour="gray75",
                 user_highlight_text="black"):

        self.command = command   # create global instance of user command for use within the click binding

        # styling options that need to be utilized outside of the init function are given global assignment in the block below
        self.calendar_date_title = calendar_date_title       # colour of the calendar title (ex: Aug 2020)
        self.date_text_fill = date_text_fill                 # colour of the text numbers associated with the month dates
        self.date_boxes_outline = date_boxes_outline         # colour of the box outline that make up the month grid
        self.trail_box_fill = trail_box_fill                 # colour of the background of the date boxes that trail into the previous and following months
        self.trail_text_fill = trail_text_fill               # colour of the text numbers associated with the trailing date boxes
        self.date_highlight = date_highlight                 # colour of the permanent date highlight associated with the current date retrieved from the OS
        self.text_highlight_fill = text_highlight_fill       # colour of the text associated with the permanent date highlight
        self.user_highlight_colour = user_highlight_colour   # colour of the highlight that is displayed when the user clicks on a month date
        self.user_highlight_text = user_highlight_text       # colour of the text associated with the user highlight


        # The following condition describes the preset styling options for the "Dark" style variation. Note: if the preset
        # is not specified, the calendar defaults to the options defined within the __init__ parameters. The default styling
        # is considered to be the "Light" preset. To manually style the calendar, the default arguments within the __init__
        # function are overridden by the options specified when and instance of the calendar object is created.
        if style == "Dark":
            background = "gray7"                     # colour of the calendar background
            calendar_relief = "flat"                 # relief style options associated with the canvas on which the calendar is created
            arrow_box_border = "gray25"              # colour of the box outline that contains the arrows for selecting previous and following months
            arrow_box_fill = "gray7"                 # colour inside the box that contains the arrows
            arrow_box_width = 1                      # width of the line used to create the box that contains the arrows
            date_box_border = "gray25"               # colour of the border associated with the monthly calendar grid
            date_box_fill = "gray7"                  # colour inside the boxes that make up the monthly calendar grid
            date_box_width = 2                       # width of the line used to create the grid for the monthly calendar
            self.date_boxes_outline = "gray50"       # colour of the box outline for the boxes that make up the monthly claendar grid
            arrow_outline = "gray25"                 # colour for the outline of the polygon (i.e - triangle) that represents the calendar arrows
            arrow_fill = "black"                     # colour of the calendar arrows
            arrow_thickness = 1                      # thickness of the calendar arrows
            arrow_active = "lime"                    # colour for the activefill associated with the calendar arrows
            weekday_border = "gray25"                # colour for the outline of the boxes that hold the weekday headings
            weekday_fill = "gray50"                  # colour for the background of the boxes that hold the weekday headings
            weekday_width = 2                        # width of the boxes that hold the weekday headings
            weekday_font_fill = "white"              # colour of the text associated with the weekday headings
            self.calendar_date_title = "white"
            self.date_text_fill = "white"
            self.trail_box_fill = "gray20"
            self.trail_text_fill = "gray60"
            self.date_highlight = "lime"
            self.text_highlight_fill = "black"


        # The minimum width of the calendar object is set at 300 pixels. The depth and the padding are both factors of
        # the width.
        if size < 300:
            size = 300
        size = size
        depth = (0.666 * size)
        depth = depth
        padding = int(size * 0.03333)
        padding = padding

        # create the tkinter canvas onto which the calendar will be created
        self.Calendar = tkinter.Canvas(window_name, width=size, height=depth,
                                       background=background, relief=calendar_relief)

        # position the calendar with the default "pack" option or according the user specified x and y coordinates
        if (pos_x == 0) and (pos_y == 0):
            self.Calendar.pack()
        else:
            self.Calendar.place(x=pos_x, y=pos_y)

        # Calendar Arrow Box
        arrow_box_margin = int(size * 0.25)
        self.Calendar.create_rectangle(arrow_box_margin, padding, (size - arrow_box_margin), (depth * 0.25),
                                  outline=arrow_box_border, fill=arrow_box_fill, width=arrow_box_width, tags="arrow_box")

        # Calendar Arrows
        # The polygons defined below contain the boundary wherein a user can click to access the previous or following
        # month grid.
        arrow_width = (size * 0.05)
        arrow_depth = ((depth * 0.25) * 0.15)
        self.Calendar.create_polygon((arrow_box_margin + padding), (0.5 * (padding + (depth * 0.25))),
                                (arrow_box_margin + padding + arrow_width), (arrow_depth + padding),
                                (arrow_box_margin + padding + arrow_width), ((depth * 0.25) - arrow_depth),
                                (arrow_box_margin + padding), (0.5 * (padding + (depth * 0.25))),
                                outline=arrow_outline, fill=arrow_fill, activefill=arrow_active, width=arrow_thickness,
                                tags="left_arrow")

        self.Calendar.create_polygon((size - (arrow_box_margin + padding)), (0.5 * (padding + (depth * 0.25))),
                                (size - (arrow_box_margin + padding + arrow_width)), (arrow_depth + padding),
                                (size - (arrow_box_margin + padding + arrow_width)), ((depth * 0.25) - arrow_depth),
                                (size - (arrow_box_margin + padding)), (0.5 * (padding + (depth * 0.25))),
                                outline=arrow_outline, fill=arrow_fill, activefill=arrow_active, width=arrow_thickness,
                                tags="right_arrow")


        # Calendar_Box Ratio Definitions
        # To ensure that the calendar remains scalable, the width and depth of the monthly grid boxes are defined as a
        # ratio of the size of the calendar itself.
        box_width = ((size - (padding * 2)) * 0.144)
        box_depth = ((depth - padding) - (padding + (depth * 0.25))) * 0.1666

        # Create Calendar_Weekday Headings
        heading_inc = 0
        weekday_top_y = (padding + (depth * 0.23))
        weekday_bot_y = weekday_top_y + box_depth

        # The boxes that hold the weekday headings are tagged with the items of the following array. These tags are used
        # to identify the boxes, define their local center and create the text associated with the corresponding weekday.
        weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

        while heading_inc != 7:
            self.Calendar.create_rectangle((padding + (box_width * heading_inc)),
                                           weekday_top_y,
                                           (padding + (box_width * (heading_inc + 1))),
                                           weekday_bot_y,
                                           outline=weekday_border,
                                           fill=weekday_fill,
                                           width=weekday_width,
                                           tags=weekdays[heading_inc])
            heading_inc = heading_inc + 1

        font_size = int((box_depth * 0.75) * 0.75)
        weekday_font = font.Font(family=weekday_font_family, size=font_size)
        for day in weekdays:
            weekday_coords = self.Calendar.coords(day)
            letter_x = (weekday_coords[0] + weekday_coords[2]) / 2
            letter_y = (weekday_coords[1] + weekday_coords[3]) / 2
            letter = day[0]
            self.Calendar.create_text(letter_x, letter_y, text=letter, anchor="center",
                                      font=weekday_font, fill=weekday_font_fill)


        # The month information is retrieved from the OS as an integer and defined as a string based on the
        # corresponding index within the following array. Since this information is used to create the calendar
        # heading for the month that the user selects, it has to be defined globally.
        self.months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

        # fetch basic date and time information from the OS
        today = date.today()
        self.year = today.year
        self.month = today.month
        self.date_today = self.months[(self.month - 1)] + " " + str(self.year)   # create the string that defines the current date
        const_month = today.month
        const_year = today.year
        const_day = today.day
        self.date_store = [const_year, const_month, const_day]   # this global array is used for creating a permanent date highlight for the current day

        # Initialize global date holder for selected days
        self.day_num = None

        # create calendar date heading (ex: Aug 2022)
        arrow_box_coords = self.Calendar.coords("arrow_box")
        self.arrow_date_x = (arrow_box_coords[0] + arrow_box_coords[2]) / 2
        self.arrow_date_y = (arrow_box_coords[1] + arrow_box_coords[3]) / 2
        font_size = int((self.arrow_date_y * 0.75) * 0.5)
        self.date_heading_font = font.Font(family=date_heading_font_family, size=font_size)
        self.Calendar.create_text(self.arrow_date_x, self.arrow_date_y, text=self.date_today, anchor="center",
                                  font=self.date_heading_font,
                                  fill=self.calendar_date_title, tags="arrow_box_date")

        # create date boxes for days of the month
        # The date boxes make up the monthly date grid into which the relevant dates are placed. The tags for the date
        # boxes are globally stored and are used to define the position of the text on the grid.
        box_width = ((size - (padding * 2)) * 0.144)
        box_depth = ((depth - padding) - (padding + (depth * 0.25))) * 0.1428
        box_y_start = (padding + (depth * 0.25)) + box_depth
        width_inc = 0
        depth_inc = 0
        box_count = 0
        self.date_box_font_size = int(((box_depth) * 0.75) * 0.6)
        self.date_text_font = font.Font(family=date_text_font_family, size=self.date_box_font_size)
        self.date_box_tags = []
        while box_count != 42:
            box_tag = "date_box_" + str(box_count)
            self.Calendar.create_rectangle((padding + (box_width * width_inc)),
                                           (box_y_start + (box_depth * depth_inc)),
                                           (padding + (box_width * (width_inc + 1))),
                                           (box_y_start + (box_depth * (depth_inc + 1))),
                                           outline=self.date_boxes_outline, tags=box_tag)
            self.date_box_tags.append(box_tag)
            width_inc = width_inc + 1
            box_count = box_count + 1
            if (box_count / 7).is_integer():
                width_inc = 0
                depth_inc = depth_inc + 1

        # The three two-dimensional arrays below hold major data relating to calendar dates and their corresponding
        # positon on the calendar grid. This data is used to perform active calendar operations including: creating
        # active date highlights, and returning date information to the user on-click.
        self.prev_tags = [[], []]
        self.foll_tags = [[], []]
        self.date_tags = [[], []]
        self.checkbox = []
        self.checkbox_tags = []

        # call first update to the calendar
        self.update()


        # The inner function below - switchboard - is linked to the click binding associated with the canvas on which
        # the calendar is created. It processes the click event data and handles the necessary update calls to the canvas
        # along with other functions associated with the user click.
        def switchboard(event):
            left_arrow = self.Calendar.coords("left_arrow")
            right_arrow = self.Calendar.coords("right_arrow")
            user_highlight = None
            self.day_num = None
            day_num = None
            for prev_coords in self.prev_tags[0]:
                event_coords = self.Calendar.coords(prev_coords)
                if (event.x > event_coords[0]) and (event.x < event_coords[2]) and (event.y > event_coords[1]) and (event.y < event_coords[3]):
                    event.x = left_arrow[0] + 1
                    event.y = left_arrow[3] + 1
                    index = self.prev_tags[0].index(prev_coords)
                    day_tag = self.prev_tags[1][index]
                    day_num = self.Calendar.itemcget(day_tag, 'text')

            for foll_coords in self.foll_tags[0]:
                event_coords = self.Calendar.coords(foll_coords)
                if (event.x > event_coords[0]) and (event.x < event_coords[2]) and (event.y > event_coords[1]) and (event.y < event_coords[3]):
                    event.x = right_arrow[0] - 1
                    event.y = right_arrow[3] + 1
                    index = self.foll_tags[0].index(foll_coords)
                    day_tag = self.foll_tags[1][index]
                    day_num = self.Calendar.itemcget(day_tag, 'text')

            for current_coords in self.date_tags[1]:
                if (event.x > current_coords[0]) and (event.x < current_coords[2]) and (event.y > current_coords[1]) and (event.y < current_coords[3]):
                    user_highlight = current_coords
                    index = self.date_tags[1].index(current_coords)
                    day_tag = self.date_tags[0][index]
                    day_num = self.Calendar.itemcget(day_tag, 'text')


            if (event.x > left_arrow[0]) and (event.x < left_arrow[2]) and (event.y > left_arrow[3]) and (event.y < left_arrow[5]):
                self.month = self.month - 1
                if self.month == 0:
                    self.month = 12
                    self.year = self.year - 1
                self.date_today = self.months[(self.month - 1)] + " " + str(self.year)
                self.update()
                if day_num != None:
                    user_highlight = self.date_tags[1][((int(day_num)) - 1)]
            elif (event.x < right_arrow[0]) and (event.x > right_arrow[2]) and (event.y > right_arrow[3]) and (event.y < right_arrow[5]):
                self.month = self.month + 1
                if self.month == 13:
                    self.month = 1
                    self.year = self.year + 1
                self.date_today = self.months[(self.month - 1)] + " " + str(self.year)
                self.update()
                if day_num != None:
                    user_highlight = self.date_tags[1][((int(day_num)) - 1)]

            # create selected date highlight
            # The user selected date highlight functionality is defined within the switchboard as it relies primarily on
            # the user click event to define the location of the highlight.
            self.Calendar.delete("user_highlight_box")
            self.Calendar.delete("user_highlight_text")
            if user_highlight != None:
                self.day_num = day_num
                user_highlight_x = (user_highlight[0] + user_highlight[2]) / 2
                user_highlight_y = (user_highlight[1] + user_highlight[3]) / 2
                oval_x1 = user_highlight_x - self.date_box_font_size
                oval_x2 = user_highlight_x + self.date_box_font_size
                oval_y1 = user_highlight_y - self.date_box_font_size
                oval_y2 = user_highlight_y + self.date_box_font_size
                self.Calendar.create_oval(oval_x1, oval_y1, oval_x2, oval_y2, fill=self.user_highlight_colour,
                                          tags="user_highlight_box")

                self.Calendar.create_text(user_highlight_x, user_highlight_y, text=day_num,
                                          anchor="center", fill=self.user_highlight_text,
                                          font=self.date_text_font, tags="user_highlight_text")

            # The condition below allows the user to define a command to be triggered by the calendar on click
            if self.command != "no command":
                self.command()


        self.Calendar.bind('<Button>', switchboard)

    # To avoid redundant blocks of code, all of the updates to the calendar are defined within one function - update.
    def update(self):
        # create calendar date heading
        self.Calendar.delete("arrow_box_date")
        self.Calendar.create_text(self.arrow_date_x, self.arrow_date_y, text=self.date_today, anchor="center",
                                  font=self.date_heading_font, fill=self.calendar_date_title, tags="arrow_box_date")


        # create date text on the calendar
        if len(self.date_tags[0]) > 0:
            for date in self.date_tags[0]:
                self.Calendar.delete(date)
            if (self.date_store[0] != self.year) or (self.date_store[1] != self.month):
                self.Calendar.delete("date_highlight")
                self.Calendar.delete("date_highlight_text")
        day_count = 1
        self.date_tags = [[], []]
        monthrange = calendar.monthrange(self.year, self.month)
        month_length = monthrange[1]
        start_box = (calendar.weekday(self.year, self.month, 1)) + 1
        self.prev_box = start_box - 1
        self.foll_box = start_box + int(month_length)
        while month_length != 0:
            date_tag = "day_" + str(day_count)
            date_box_coords = self.Calendar.coords(self.date_box_tags[start_box])
            x_coords = (date_box_coords[0] + date_box_coords[2]) / 2
            y_coords = (date_box_coords[1] + date_box_coords[3]) / 2
            self.Calendar.create_text(x_coords, y_coords, text=str(day_count), anchor="center",
                                      font=self.date_text_font, fill=self.date_text_fill, activefill=self.date_highlight,
                                      tags=date_tag)
            self.date_tags[0].append(date_tag)
            self.date_tags[1].append(date_box_coords)
            day_count = day_count + 1
            start_box = start_box + 1
            month_length = month_length - 1

        # create trailing month dates
        def trail_boxes(previous=False, following=False):
            if previous:
                month = self.month - 1
                year = self.year
                if month < 1:
                    month = 12
                    year = self.year - 1
                trail_monthrange = calendar.monthrange(year, month)
                trail_monthlength = trail_monthrange[1]
                trail_start = trail_monthlength
                stopping_point = -1
                counter = self.prev_box
            elif following:
                stopping_point = 42
                counter = self.foll_box
                trail_start = 1
            else:
                counter = 0
                stopping_point = 42
                trail_start = 0

            while counter != stopping_point:
                trail_text = str(trail_start)
                trail_box_tag = "trail_box_" + str(counter)
                trail_text_tag = "trail_text_" + trail_text
                trail_box_coords = self.Calendar.coords(self.date_box_tags[counter])
                # create trail_box background
                self.Calendar.create_rectangle(trail_box_coords[0], trail_box_coords[1],
                                               trail_box_coords[2], trail_box_coords[3],
                                               fill=self.trail_box_fill, outline=self.date_boxes_outline, tags=trail_box_tag)
                #create trail_box dates
                trail_x = (trail_box_coords[0] + trail_box_coords[2]) / 2
                trail_y = (trail_box_coords[1] + trail_box_coords[3]) / 2
                self.Calendar.create_text(trail_x, trail_y, text=trail_text, anchor="center",
                                          font=self.date_text_font, fill=self.trail_text_fill,
                                          activefill=self.date_highlight, tags=trail_text_tag)

                if previous:
                    self.prev_tags[0].append(trail_box_tag)
                    self.prev_tags[1].append(trail_text_tag)
                    counter = counter - 1
                    trail_start = trail_start - 1
                elif following:
                    self.foll_tags[0].append(trail_box_tag)
                    self.foll_tags[1].append(trail_text_tag)
                    counter = counter + 1
                    trail_start = trail_start + 1


        if len(self.prev_tags[0]) > 0:
            for trail_box in self.prev_tags[0]:
                self.Calendar.delete(trail_box)
            for trail_text in self.prev_tags[1]:
                self.Calendar.delete(trail_text)
            self.prev_tags = [[], []]

        if len(self.foll_tags[0]) > 0:
            for trail_box in self.foll_tags[0]:
                self.Calendar.delete(trail_box)
            for trail_text in self.foll_tags[1]:
                self.Calendar.delete(trail_text)
            self.foll_tags = [[], []]

        trail_boxes(previous=True)
        trail_boxes(following=True)

        # create date highlight
        if (self.date_store[0] == self.year) and (self.date_store[1] == self.month):
            highlight_coords = self.Calendar.coords("day_" + str(self.date_store[2]))
            hx_1 = highlight_coords[0] - self.date_box_font_size
            hy_1 = highlight_coords[1] - self.date_box_font_size
            hx_2 = highlight_coords[0] + self.date_box_font_size
            hy_2 = highlight_coords[1] + self.date_box_font_size
            self.Calendar.create_oval(hx_1, hy_1, hx_2, hy_2, fill=self.date_highlight, outline=self.date_highlight,
                                      tags="date_highlight")
            self.Calendar.create_text(highlight_coords[0], highlight_coords[1], text=str(self.date_store[2]),
                                      anchor="center", font=self.date_text_font, fill=self.text_highlight_fill,
                                      tags="date_highlight_text")

        # delete checkboxes if they exist
        if len(self.checkbox_tags) != 0:
            for cbox in self.checkbox_tags:
                self.Calendar.delete(cbox)

        # create checkboxes
        checkbox_count = 1
        if len(self.checkbox) > 0:
            for checkbox in self.checkbox:
                checkbox_tag = "checkbox_" + str(checkbox_count)
                status_tag = "status_" + str(checkbox_count)
                # checkboxes for current month
                if (int(self.month) == int(checkbox[0][1])) and (int(self.year) == int(checkbox[0][2])):
                    # create checkboxes
                    check_coords = self.date_tags[1][(int(checkbox[0][0]) - 1)]
                    box_length = ((check_coords[2] - check_coords[0]) * 0.2)
                    corner_x = check_coords[0]
                    corner_y = check_coords[1]
                    bot_x = corner_x + box_length
                    bot_y = corner_y + box_length
                    self.Calendar.create_rectangle(corner_x, corner_y, bot_x, bot_y, tags=checkbox_tag)
                    if checkbox[1]:
                        self.Calendar.create_line(corner_x, (corner_y + ((bot_y - corner_y) / 2)),
                                                  (corner_x + ((bot_x - corner_x) / 3)), bot_y,
                                                  bot_x, corner_y, width=3, fill="green", tags=status_tag)
                    else:
                        self.Calendar.create_line(corner_x, corner_y, bot_x, bot_y, width=2, fill="red", tags=status_tag)
                        self.Calendar.create_line(corner_x, bot_y, bot_x, corner_y, width=2, fill="red", tags=status_tag)
                    self.checkbox_tags.append(checkbox_tag)
                    self.checkbox_tags.append(status_tag)

                # checkboxes for previous month trail boxes
                prev_month = self.month - 1
                if prev_month < 1:
                    prev_month = 12
                    prev_year = self.year - 1
                else:
                    prev_year = self.year

                if (int(prev_month) == int(checkbox[0][1])) and (int(prev_year) == int(checkbox[0][2])):
                    for text_tag in self.prev_tags[1]:
                        day_num = self.Calendar.itemcget(text_tag, 'text')
                        if str(day_num) == str(checkbox[0][0]):
                            prev_box_index = self.prev_tags[1].index(text_tag)
                            prev_box = self.prev_tags[0][prev_box_index]
                            prev_box_coords = self.Calendar.coords(prev_box)
                            box_length = ((prev_box_coords[2] - prev_box_coords[0]) * 0.2)
                            corner_x = prev_box_coords[0]
                            corner_y = prev_box_coords[1]
                            bot_x = corner_x + box_length
                            bot_y = corner_y + box_length
                            self.Calendar.create_rectangle(corner_x, corner_y, bot_x, bot_y, tags=checkbox_tag)
                            if checkbox[1]:
                                self.Calendar.create_line(corner_x, (corner_y + ((bot_y - corner_y) / 2)),
                                                          (corner_x + ((bot_x - corner_x) / 3)), bot_y,
                                                          bot_x, corner_y, width=3, fill="green", tags=status_tag)
                            else:
                                self.Calendar.create_line(corner_x, corner_y, bot_x, bot_y, width=2, fill="red",
                                                          tags=status_tag)
                                self.Calendar.create_line(corner_x, bot_y, bot_x, corner_y, width=2, fill="red",
                                                          tags=status_tag)
                            self.checkbox_tags.append(status_tag)
                            self.checkbox_tags.append(checkbox_tag)

                # checkboxes for following month trail boxes
                foll_month = self.month + 1
                if foll_month > 12:
                    foll_month = 1
                    foll_year = self.year + 1
                else:
                    foll_year = self.year

                if (int(foll_month) == int(checkbox[0][1])) and (int(foll_year) == int(checkbox[0][2])):
                    for text_tag in self.foll_tags[1]:
                        day_num = self.Calendar.itemcget(text_tag, 'text')
                        if str(day_num) == str(checkbox[0][0]):
                            foll_box_index = self.foll_tags[1].index(text_tag)
                            foll_box = self.foll_tags[0][foll_box_index]
                            foll_box_coords = self.Calendar.coords(foll_box)
                            box_length = ((foll_box_coords[2] - foll_box_coords[0]) * 0.2)
                            corner_x = foll_box_coords[0]
                            corner_y = foll_box_coords[1]
                            bot_x = corner_x + box_length
                            bot_y = corner_y + box_length
                            self.Calendar.create_rectangle(corner_x, corner_y, bot_x, bot_y, tags=checkbox_tag)
                            if checkbox[1]:
                                self.Calendar.create_line(corner_x, (corner_y + ((bot_y - corner_y) / 2)),
                                                          (corner_x + ((bot_x - corner_x) / 3)), bot_y,
                                                          bot_x, corner_y, width=3, fill="green", tags=status_tag)
                            else:
                                self.Calendar.create_line(corner_x, corner_y, bot_x, bot_y, width=2, fill="red",
                                                          tags=status_tag)
                                self.Calendar.create_line(corner_x, bot_y, bot_x, corner_y, width=2, fill="red",
                                                          tags=status_tag)
                            self.checkbox_tags.append(status_tag)
                            self.checkbox_tags.append(checkbox_tag)


                checkbox_count = checkbox_count + 1


    def checkboxes(self, day, month, year, status=True, delete=False):
        if delete:
            # if the delete parameter is True, the checkbox is deleted from the list and the calendar is updated
            remove = [day, month, year]
            for item in self.checkbox:
                if item[0] == remove:
                    remove = item
                    delete = False
            if delete == False:
                self.checkbox.remove(remove)
                self.update()
        else:
            # check to ensure that the requested checkbox is not already created
            store = [[day, month, year], status]
            duplicate = False
            status_update = False
            remove = None
            for item in self.checkbox:
                if item[0] == store[0]:
                    duplicate = True
                    if duplicate:               # check if the status has changed
                        if item[1] != status:
                            status_update = True
                            remove = item

            if status_update:
                self.checkbox.remove(remove)     # remove the old entry
                duplicate = False

            # if the checkbox does not exist it will be added to the list and created
            if duplicate == False:
                self.checkbox.append(store)
                self.update()


    # the function below returns the date information to the user when a date selected
    def getdate(self):
        date = str(self.day_num) + "-" + str(self.month) + "-" + str(self.year)
        return date

    # destroy method for the Calendar Widget
    def destroy(self):
        self.Calendar.destroy()

