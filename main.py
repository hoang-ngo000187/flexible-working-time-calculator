"""
    @author: NGO KIEN HOANG (kienhoang.ng@samsung.com)
    @day: August 18
"""

#######################################################################################################################################
                                                        # IMPORT LIBRARY #
#######################################################################################################################################
from tkinter import*
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
name = Label(win,
             text ="Calculate Check-out time", 
             font = FONT_TUPLE_TILE,
             bg = GUI_BACKGROUND_COLOR,
             fg="#97FFFF")
name.place(x = 30, y = 30) #pixel x = truc ngang (width); y = truc doc (height)



# 02. Lable: Time-in
lable_TimeIn = Label(win,
             text ="⌨ Enter Check-in time:", 
             font = FONT_TUPLE_CONTENT,
             bg = GUI_BACKGROUND_COLOR,
             fg="#97FFFF")
lable_TimeIn.place(x = 30, y = 60)

# 03. Entry: Entry Time-in
entry_TimeIn = Entry(win,
                 width =7,
                 bg = "white", #Tan1
                 fg = "black",
                 font = FONT_TUPLE_TILE,
                 )
entry_TimeIn.place(x = 220, y = 60)



# 02. Lable: Exclude Time
lable_ExcludeTime = Label(win,
             text ="⌨ Enter Exclude time:", 
             font = FONT_TUPLE_CONTENT,
             bg = GUI_BACKGROUND_COLOR,
             fg="#97FFFF")
lable_ExcludeTime.place(x = 30, y = 90)

# 03. Entry: Entry Exclude time
entry_ExcludeTime = Entry(win,
                 width =7,
                 bg = "white", #Tan1
                 fg = "black",
                 font = FONT_TUPLE_TILE,
                 )
entry_ExcludeTime.place(x = 220, y = 90)



# 04. Lable: Time-out 8:48
lable_TimeOut8h48 = Label(win,
             text ="⏱ 8h48m-Check-out time:", 
             font = FONT_TUPLE_CONTENT,
             bg = GUI_BACKGROUND_COLOR,
             fg="#97FFFF")
lable_TimeOut8h48.place(x = 30, y = 120)

# 03. Entry: Time-out 8:48
entry_TimeOut8h48 = Entry(win,
                 width =7,
                 bg = "white", #Tan1
                 fg = "black",
                 font = FONT_TUPLE_TILE,
                 state = "disable"
                 )
entry_TimeOut8h48.place(x = 220, y = 120)



# 04. Lable: Time-out 10:00
lable_TimeIn = Label(win,
             text ="⏱ 10h00m-Check-out time:", 
             font = FONT_TUPLE_CONTENT,
             bg = GUI_BACKGROUND_COLOR,
             fg="#97FFFF")
lable_TimeIn.place(x = 30, y = 150)

# 03. Entry: Time-out 10:00
entry_TimeOut10h00 = Entry(win,
                 width =7,
                 bg = "white", #Tan1
                 fg = "black",
                 font = FONT_TUPLE_TILE,
                 state = "disable"
                 )
entry_TimeOut10h00.place(x = 220, y = 150)



# 03. Button: Calculate Time-out
def button_fcn_CalCheckOutTime():
    next = True
    IN = entry_TimeIn.get()
    EXCLUDE = entry_ExcludeTime.get()

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
    
    if (IN == "00:00" and EXCLUDE == "00:00"):
        next = False

    if (True == next):
        OUT8H48_TIME = calculate_time(IN, OUT8H48, PLUS_TIME)
        OUT8H48_TIME = calculate_time(str(OUT8H48_TIME)[11:16], EXCLUDE, PLUS_TIME)
        OUT10H00_TIME = calculate_time(IN, OUT10H00, PLUS_TIME)
        OUT10H00_TIME = calculate_time(str(OUT10H00_TIME)[11:16], EXCLUDE, PLUS_TIME)

        OUT8H48_STR = str(OUT8H48_TIME)[11:16]
        OUT10H00_STR = str(OUT10H00_TIME)[11:16]
    else:
        OUT8H48_STR = "ERROR!"
        OUT10H00_STR = "ERROR!"

    entry_TimeOut8h48.configure(state = "normal")
    entry_TimeOut8h48.delete(0, END)
    entry_TimeOut8h48.insert(0, OUT8H48_STR)
    entry_TimeOut8h48.configure(state = "disable")
    entry_TimeOut10h00.configure(state = "normal")
    entry_TimeOut10h00.delete(0, END)
    entry_TimeOut10h00.insert(0, OUT10H00_STR)
    entry_TimeOut10h00.configure(state = "disable")

button_CalCheckOutTime = Button(win,
                 text = "Calculate ▶",
                 width = 24,
                 height = 1,
                 bg = "#FFA54F", #Tan1
                 fg = "black",
                 font = FONT_TUPLE_BUTTON,
                 command = button_fcn_CalCheckOutTime,
                 )
button_CalCheckOutTime.place(x = 30, y = 190)

ico = Image.open('clock.png')
photo = ImageTk.PhotoImage(ico)
win.wm_iconphoto(False, photo)
win.mainloop()