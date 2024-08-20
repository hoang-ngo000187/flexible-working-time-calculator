"""
    @brief: This file contains some configed variables.
"""
##################################################### SOFTWARE VERSION ##################################################
YEAR = 0x24
MONTH = 0x08
DAY = 0x17

######################################################## GUI CONFIG ####################################################
GUI_TITLE = "SAMSUNG - FLEXIBLE WORKING TIME CALCULATOR"
GUI_DIMENSIONS = "700x500" # (width x height)
GUI_BACKGROUND_COLOR = "#1C1C1C"#"#363636" ##707070
GUI_TOPMOST = True # always display on the top of other app.



######################################################## FONT TEXT & COLOR CONFIG ###############################################
JETBRAINS_MONO = "JetBrains Mono"
JETBRAINS_MONO_MEDIUM = "JetBrains Mono Medium"
CONSOLAS = "Consolas"
COOPER_BLACK= "Cooper Black"
IMPACT = "Impact"
COMIC_SANS_MS = "Comic Sans MS"
BERLIN_SANS_FB_DEMI = "Berlin Sans FB Demi"

FONT_NAME_TILE = BERLIN_SANS_FB_DEMI#JETBRAINS_MONO_MEDIUM
FONT_SIZE_TILE = 15
FONT_STYLE_TILE = "bold" # bold - italic - underline
FONT_TUPLE_TILE = (FONT_NAME_TILE, FONT_SIZE_TILE, FONT_STYLE_TILE)
COLOR_TITLE = "#FF6A6A"

FONT_NAME_CONTENT = COMIC_SANS_MS#CONSOLAS
FONT_SIZE_CONTENT = 10
FONT_STYLE_CONTENT = "" # bold - italic - underline
FONT_TUPLE_CONTENT = (FONT_NAME_CONTENT, FONT_SIZE_CONTENT, FONT_STYLE_CONTENT)
COLOR_CONTENT = "#00CC99"

FONT_NAME_BUTTON = COMIC_SANS_MS
FONT_SIZE_BUTTON = 13
FONT_STYLE_BUTTON = "bold" # bold - italic - underline
FONT_TUPLE_BUTTON = (FONT_NAME_BUTTON, FONT_SIZE_BUTTON, FONT_STYLE_BUTTON)

FONT_NAME_DATA = COMIC_SANS_MS#JETBRAINS_MONO_MEDIUM
FONT_SIZE_DATA = 13
FONT_STYLE_DATA = "bold" # bold - italic - underline
FONT_TUPLE_DATA = (FONT_NAME_DATA, FONT_SIZE_DATA, FONT_STYLE_DATA)

######################################################## CALCULATE CONFIG ###############################################
PLUS_TIME = True
MINUS_TIME = False

BIGGER_TIME = True
SMALLER_TIME = False

######################################################## TIME CONFIG ###############################################
OUT8H48 = "09:48"
OUT10H00 = "11:00"