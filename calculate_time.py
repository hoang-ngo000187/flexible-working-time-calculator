from datetime import datetime , timedelta
from config import*

def check_valid_time(time: str):
    ret = True
    list_time = time.split(":")
    if ( (int(list_time[0]) < 0) 
        or (int(list_time[0]) > 23) 
        or (int(list_time[1]) < 0) 
        or (int(list_time[1]) > 59) ):
        ret = False
    return ret


def calculate_time(timeA: str, timeB: str, type: bool):
    start = datetime.strptime(timeA, "%H:%M")

    difference = 0
    if (PLUS_TIME == type):
        end = timeB.split(":")
        difference = start + timedelta(hours = int(end[0]), minutes = int(end[1]))

    elif (MINUS_TIME == type):
        end = datetime.strptime(timeB, "%H:%M")
        difference = end - start

    return difference

def compare_two_time(timeBig: str, timeSmall: str):
    ret = BIGGER_TIME

    list_timeA = timeBig.split(":")
    list_timeB = timeSmall.split(":")

    if (int(list_timeA[0]) > int(list_timeB[0])):
        ret = BIGGER_TIME
    elif (int(list_timeA[0]) < int(list_timeB[0])):
        ret = SMALLER_TIME
    else:
        if (int(list_timeA[1]) > int(list_timeB[1])):
            ret = BIGGER_TIME
        elif (int(list_timeA[1]) < int(list_timeB[1])):
            ret = SMALLER_TIME
    return ret

def check_valid_syntax_hours(time: str):
    ret = True
    if (len(time) == 1 and time[0] != "0"): # a, ~, !, -
        ret = False
    elif (len(time) <= 5): # HH:MM
        # Fine ":"
        if (time.find(":") == -1): # 12345
            ret = False
        else:
            tmp = time.split(":")
            if (len(tmp) != 2): # 10:23:34:35
                ret = False
            else: # :12 --> ["", "12"]
                if (tmp[0] == "" or tmp[1] == ""):
                    ret = False
    elif (len(time) > 5): # 125:23, 123456
        ret = False
    return ret