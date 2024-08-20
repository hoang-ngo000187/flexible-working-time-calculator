"""
    @author: NGO KIEN HOANG (kienhoang.ng@samsung.com)
    @day: August 18
"""

#######################################################################################################################################
                                                        # IMPORT LIBRARY #
#######################################################################################################################################
from tkinter import*
import tkinter.messagebox
from config import*
from calculate_time import*
from PIL import Image, ImageTk

#######################################################################################################################################
                                                        # CONFIG MAIN GUI #
#######################################################################################################################################
win = Tk()

# Setup tile of GUI
win.title(GUI_TITLE)
# Setup demension of GUI (width x height)
win.geometry(GUI_DIMENSIONS)
# Setup background color
win["bg"] = GUI_BACKGROUND_COLOR
# Setup Topmost
win.attributes("-topmost", GUI_TOPMOST)



#image = PhotoImage(file="gfg.png")

#######################################################################################################################################
                                                        # CALCULATE CHECK-OUT TIME #
#######################################################################################################################################
# 01. Tile: Calculate check-out time
lable_CO_TitleCheckOutTime = Label(win,
             text ="CALCULATE CHECK-OUT TIME", 
             font = FONT_TUPLE_TILE,
             bg = GUI_BACKGROUND_COLOR,
             fg= COLOR_TITLE)
lable_CO_TitleCheckOutTime.place(x = 30, y = 30) #pixel x = truc ngang (width); y = truc doc (height)


# 02. Lable: Time-in
lable_CO_TimeIn = Label(win,
             text ="⌨ Enter Check-in time:", 
             font = FONT_TUPLE_CONTENT,
             bg = GUI_BACKGROUND_COLOR,
             fg= COLOR_CONTENT)
lable_CO_TimeIn.place(x = 30, y = 70)

# 03. Entry: Entry Time-in
entry_CO_TimeIn = Entry(win,
                 width =7,
                 bg = "white", #Tan1
                 fg = "black",
                 font = FONT_TUPLE_DATA,
                 )
entry_CO_TimeIn.place(x = 220, y = 70)



# 02. Lable: Exclude Time
lable_CO_ExcludeTime = Label(win,
             text ="⌨ Enter Exclude time:", 
             font = FONT_TUPLE_CONTENT,
             bg = GUI_BACKGROUND_COLOR,
             fg= COLOR_CONTENT)
lable_CO_ExcludeTime.place(x = 30, y = 100)

# 03. Entry: Entry Exclude time
entry_CO_ExcludeTime = Entry(win,
                 width =7,
                 bg = "white", #Tan1
                 fg = "black",
                 font = FONT_TUPLE_DATA,
                 )
entry_CO_ExcludeTime.place(x = 220, y = 100)



# 04. Lable: Time-out 8:48
lable_CO_TimeOut8h48 = Label(win,
             text ="⏱ 8h48m-Check-out time:", 
             font = FONT_TUPLE_CONTENT,
             bg = GUI_BACKGROUND_COLOR,
             fg= COLOR_CONTENT)
lable_CO_TimeOut8h48.place(x = 30, y = 130)

# 03. Entry: Time-out 8:48
entry_CO_TimeOut8h48 = Entry(win,
                 width =7,
                 bg = "white", #Tan1
                 fg = "black",
                 font = FONT_TUPLE_DATA,
                 state = "disable"
                 )
entry_CO_TimeOut8h48.place(x = 220, y = 130)



# 04. Lable: Time-out 10:00
entry_CO_TimeOut10h00 = Label(win,
             text ="⏱ 10h00m-Check-out time:", 
             font = FONT_TUPLE_CONTENT,
             bg = GUI_BACKGROUND_COLOR,
             fg= COLOR_CONTENT)
entry_CO_TimeOut10h00.place(x = 30, y = 160)

# 03. Entry: Time-out 10:00
entry_CO_TimeOut10h00 = Entry(win,
                 width =7,
                 bg = "white", #Tan1
                 fg = "black",
                 font = FONT_TUPLE_DATA,
                 state = "disable"
                 )
entry_CO_TimeOut10h00.place(x = 220, y = 160)



# 03. Button: Calculate Time-out
def button_fcn_CO_CalCheckOutTime():
    next = True
    overange10H00 = False
    overange8H48 = False
    IN = entry_CO_TimeIn.get()
    EXCLUDE = entry_CO_ExcludeTime.get()

    if (EXCLUDE == "0" or EXCLUDE == ""):
        EXCLUDE = "00:00"
    if (IN == "0" or IN == ""):
        IN = "00:00"

    if ((check_valid_syntax_hours(IN) == True) and (check_valid_syntax_hours(EXCLUDE) == True)):
        if ((check_valid_time(IN) == True) and (check_valid_time(EXCLUDE) == True)):
            next = True
        else:
            next = False
    else:
        next = False

    # Check overange10H00
    if (True == next):
        EX_Ov = EXCLUDE.split(":")
        IN_Ov = IN.split(":")

        # Check overange8H48
        if (int(EX_Ov[0]) + int(IN_Ov[0]) > 14):
            overange8H48 = True
            overange10H00 = True
        elif (int(EX_Ov[0]) + int(IN_Ov[0]) == 14):
            if (int(EX_Ov[1]) + int(IN_Ov[1]) > 12):
                overange8H48 = True
                overange10H00 = True
        else:
            overange8H48 = False
            if (int(EX_Ov[0]) + int(IN_Ov[0]) == 13):
                if (int(EX_Ov[1]) + int(IN_Ov[1]) > 0):
                    overange10H00 = True
                else:
                    overange10H00 = False
                
    if (IN == "00:00" and EXCLUDE == "00:00"):
        next = False

    if (True == next):
        if (False == overange8H48):
            OUT8H48_TIME = calculate_time(IN, OUT8H48, PLUS_TIME)
            OUT8H48_TIME = calculate_time(str(OUT8H48_TIME)[11:16], EXCLUDE, PLUS_TIME)
            # Display
            OUT8H48_STR = str(OUT8H48_TIME)[11:16]
            if (False == overange10H00):
                OUT10H00_TIME = calculate_time(IN, OUT10H00, PLUS_TIME)
                OUT10H00_TIME = calculate_time(str(OUT10H00_TIME)[11:16], EXCLUDE, PLUS_TIME)
                # Display
                OUT10H00_STR = str(OUT10H00_TIME)[11:16]
            else:
                OUT10H00_STR = "OVER"
                tkinter.messagebox.showinfo("⚠ Warning!", "If you work for 10 hours, your check-out time will exceed 00:00!")
        else:
            OUT8H48_STR = "OVER"
            OUT10H00_STR = "OVER"
            tkinter.messagebox.showinfo("⚠ Warning!", "Your check-out time will exceed 00:00!")
    else:
        OUT8H48_STR = "ERROR"
        OUT10H00_STR = "ERROR"
        tkinter.messagebox.showinfo("❌ Error!", "Please enter the correct time format (HH:MM)! Example: 07:35")

    entry_CO_TimeOut8h48.configure(state = "normal")
    entry_CO_TimeOut8h48.delete(0, END)
    entry_CO_TimeOut8h48.insert(0, OUT8H48_STR)
    entry_CO_TimeOut8h48.configure(state = "disable")
    entry_CO_TimeOut10h00.configure(state = "normal")
    entry_CO_TimeOut10h00.delete(0, END)
    entry_CO_TimeOut10h00.insert(0, OUT10H00_STR)
    entry_CO_TimeOut10h00.configure(state = "disable")

IN = entry_CO_TimeIn.get()
EXCLUDE = entry_CO_ExcludeTime.get()

button_CO_CalCheckOutTime = Button(win,
                 text = "Calculate ▶",
                 width = 25,
                 height = 1,
                 bg = "#FFA54F", #Tan1
                 fg = "black",
                 font = FONT_TUPLE_BUTTON,
                 command = button_fcn_CO_CalCheckOutTime,
                 )
button_CO_CalCheckOutTime.place(x = 30, y = 200)



#######################################################################################################################################
                                                        # CALCULATE WORK HOURS #
#######################################################################################################################################
# 01. Tile: Calculate check-out time
lable_WH_TitleWorkHours = Label(win,
             text ="CALCULATE WORK HOURS", 
             font = FONT_TUPLE_TILE,
             bg = GUI_BACKGROUND_COLOR,
             fg= COLOR_TITLE)
lable_WH_TitleWorkHours.place(x = 30, y = 300) #pixel x = truc ngang (width); y = truc doc (height)


# 02. Lable: Time-in
lable_WH_TimeIn = Label(win,
             text ="⌨ Enter Check-in time:", 
             font = FONT_TUPLE_CONTENT,
             bg = GUI_BACKGROUND_COLOR,
             fg= COLOR_CONTENT)
lable_WH_TimeIn.place(x = 30, y = 340)

# 03. Entry: Entry Time-in
entry_WH_TimeIn = Entry(win,
                 width =7,
                 bg = "white", #Tan1
                 fg = "black",
                 font = FONT_TUPLE_DATA,
                 )
entry_WH_TimeIn.place(x = 220, y = 340)

# 04. Lable: Time-out
lable_WH_TimeOut = Label(win,
             text ="⌨ Enter Check-out time:", 
             font = FONT_TUPLE_CONTENT,
             bg = GUI_BACKGROUND_COLOR,
             fg= COLOR_CONTENT)
lable_WH_TimeOut.place(x = 30, y = 370)

# 05. Entry: Entry Time-out
entry_WH_TimeOut = Entry(win,
                 width =7,
                 bg = "white", #Tan1
                 fg = "black",
                 font = FONT_TUPLE_DATA,
                 )
entry_WH_TimeOut.place(x = 220, y = 370)

# 02. Lable: Exclude Time
lable_WH_ExcludeTime = Label(win,
             text ="⌨ Enter Exclude time:", 
             font = FONT_TUPLE_CONTENT,
             bg = GUI_BACKGROUND_COLOR,
             fg= COLOR_CONTENT)
lable_WH_ExcludeTime.place(x = 30, y = 400)

# 03. Entry: Entry Exclude time
entry_WH_ExcludeTime = Entry(win,
                 width =7,
                 bg = "white", #Tan1
                 fg = "black",
                 font = FONT_TUPLE_DATA,
                 )
entry_WH_ExcludeTime.place(x = 220, y = 400)

# 04. Lable: Work hours
lable_WH_WorkHours = Label(win,
             text ="⏱ Work hours of the day:", 
             font = FONT_TUPLE_CONTENT,
             bg = GUI_BACKGROUND_COLOR,
             fg= COLOR_CONTENT)
lable_WH_WorkHours.place(x = 30, y = 430)

# 03. Entry: Work hours
entry_WH_WorkHours = Entry(win,
                 width =7,
                 bg = "white", #Tan1
                 fg = "black",
                 font = FONT_TUPLE_DATA,
                 state = "disable"
                 )
entry_WH_WorkHours.place(x = 220, y = 430)

isLunchBreak = True

def button_fcn_WH_CalWorkHours():
    LUNCH_TIME = "01:00"
    WH_next = True
    WH_Error_InOut = False # In time is larger than Out time
    WH_IN = entry_WH_TimeIn.get()
    WH_OUT = entry_WH_TimeOut.get()
    WH_EXCLUDE = entry_WH_ExcludeTime.get()

    if (WH_IN == "0" or WH_IN == ""):
        WH_IN = "00:00"
    if (WH_OUT == "0" or WH_OUT == ""):
        WH_OUT = "00:00"
    if (WH_EXCLUDE == "0" or WH_EXCLUDE == ""):
        WH_EXCLUDE = "00:00"

    if ((check_valid_syntax_hours(WH_IN) == True) and (check_valid_syntax_hours(WH_EXCLUDE) == True) and (check_valid_syntax_hours(WH_OUT) == True)):
        if ((check_valid_time(WH_IN) == True) and (check_valid_time(WH_EXCLUDE) == True) and (check_valid_time(WH_OUT) == True)):
            WH_next = True
        else:
            WH_next = False
    else:
        WH_next = False
    
    WH_IN_str = WH_IN.split(":")
    WH_OUT_str = WH_OUT.split(":")
    if (int(WH_OUT_str[0]) < int(WH_IN_str[0])):
        WH_next = False
        WH_Error_InOut = True
    elif (int(WH_OUT_str[0]) == int(WH_IN_str[0])):
        if (int(WH_OUT_str[1]) < int(WH_IN_str[1])):
            WH_next = False
            WH_Error_InOut = True
    else:
        WH_Error_InOut = False
    
    if (True == WH_next):
        WORKHOURS = calculate_time(WH_IN, WH_OUT, MINUS_TIME)
        x = str(WORKHOURS)
        print(x)
        WORKHOURS = calculate_time(WH_EXCLUDE,str(WORKHOURS)[0:5], MINUS_TIME)
        if (True == isLunchBreak):
            WORKHOURS = calculate_time(LUNCH_TIME, str(WORKHOURS)[0:5], MINUS_TIME)
        WORKHOURS = str(WORKHOURS)[0:5]
    else:
        if (TRUE == WH_Error_InOut):
            tkinter.messagebox.showinfo("❌ Error!", "Check-in time must be earlier than check-out time!")
        WORKHOURS = "ERROR"

    entry_WH_WorkHours.configure(state = "normal")
    entry_WH_WorkHours.delete(0, END)
    entry_WH_WorkHours.insert(0, WORKHOURS)
    entry_WH_WorkHours.configure(state = "disable")


button_WH_CalWorkHours = Button(win,
                 text = "Calculate ▶",
                 width = 25,
                 height = 1,
                 bg = "#FFA54F", #Tan1
                 fg = "black",
                 font = FONT_TUPLE_BUTTON,
                 command = button_fcn_WH_CalWorkHours,
                 )
button_WH_CalWorkHours.place(x = 30, y = 470)

#######################################################################################################################################
                                                        # CLOCK ICON #
#######################################################################################################################################
ico = Image.open('clock.png')
photo = ImageTk.PhotoImage(ico)


win.wm_iconphoto(False, photo)
win.mainloop()