"""
This file is the core element of **prettifycli**. It includes
the core cli window and most of the settings. Functions can be
linked to selections through the `linker` in `funclinker.py`.
**prettifycli** is based on `msvcrt` and works exclusively on
the windows terminal. Versions including other operating 
systems will follow, starting with Linux.

Using prettifycli is very intuitive, the syntax is very easy 
to understand and use. 
"""
# ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
#    IMPORTS
# ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
import sys, os
sys.dont_write_bytecode = True

import msvcrt

from prettify_err import *
from _styling import (rgb, PRESETS)

# ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
#    DEFINITIONS
# ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
#: create custom types, formality - for the most part not exactly necessary
type KEY = bytes                                # -> indicating the type returned by key_listener()
type SEQ = list[str]                            # -> indicating the sequence of string returned by the window creator
type DEF = tuple[int,int] | tuple[str,str]      # -> indicating how certain arguments are to be defined
type FUN = function                             # -> defines a function
type FUL = list[function]                       # -> indicating a list of functions
type COO = tuple[int,int]                       # -> indicating a set of two-dimensional coordinates (x,y)

# ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
#    VARIABLES
# ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
HISTORY     = []                            # -> stores current menu pages for an eventual 'Return' option
ESC         = '\033['                       # -> PRESETS._reset
COLS, ROWS  = os.get_terminal_size()        # -> get the number of columns and rows of the currently active terminal

# ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
#    FUNCTIONS
# ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
def key_listener() -> KEY:
    """
    This is based on the `msvcrt.getch()` function which registers
    the keys a user is hitting on their keyboard. The `0x00` and 
    `0xe0` are bytes indicating that a special key was struck. 
    `msvcrt` then has to get the second byte using `msvcrt.getch()`
    again. Based on the mapping it will then return the corresponding
    string, based on the *arrow key* that was struck by the user.
    It shows the letters `H`, `P`, `K`, and `M` because when translated 
    to ASCII the byte codes `0x48`, `0x50`, `0x4B`, and `0x4D` 
    correspond to these letters. However, given that the `msvcrt.getch()`
    function has already registered that a key outside of the regular
    alphabet, the ASCII letters these codes correspond to do not 
    really matter (the byte sequence for the arrow keys would look as
    follows for the program `b'\\xe0' b'H'` (arrow UP), `b'\\xe0' b'P'`
     (arrow DOWN), `b'\\xe0' b'K'` (arrow LEFT), `b'\\xe0' b'M'` 
    (arrow RIGHT)).Furthermore, `key_listener()` registers the `ENTER` 
    (`\\r`) and `ESC` (`0x1b`) characters.\n
    If the user hits a key that's within the regular set of non-function
    keys, the byte code will be decoded using `ch.decode()`. The `str`
    element will then be returned, allowing the user to enter text
    normally.\n
    The `key_listener()` function *can* be disabled if the user wants
    to enter some form of text, allowing the use of the arrow keys.
    """
    #: get characters
    ch = msvcrt.getch()

    #: check if user hit  a key with a special function, map keys, return keys
    if ch in (b'\x00', b'\xe0'):
        ch2 = msvcrt.getch()            # -> a special key was detected, to register the correct byte code call getch() again   
        mapping = {
                b'H': 'UP',             # -> 0xe0 0x48
                b'P': 'DOWN',           # -> 0xe0 0x50      
                b'K': 'LEFT',           # -> 0xe0 0x4B
                b'M': 'RIGHT',          # -> 0xe0 0x4D
        }
        return mapping.get(ch2, '')     # -> return the character as a usable string
    
    #: ENTER or ESC byte codes
    elif ch == b'\r':   return 'ENTER'
    elif ch == b'\x1b': return 'ESC'

    #: no special functional key was hit, return regular ASCII letter
    else:
        try: return ch.decode()         # -> turn byte code to ASCII letter
        except UnicodeDecodeError: return ''
def clear() -> int:         os.system('cls' if os.name =='nt' else 'clear') # -> clear terminal
def move(y,x) -> str:       print(f"{ESC}{y};{x}H", end="")                 # -> move window frame in terminal
def color(code) -> str:     print(f"{code}", end="")                        # -> change color
def reset() -> str:         print(PRESETS._reset, end="")                   # -> reset escape sequence (use to go ack to default text after changing color etc...)
def w(cols, _str) -> int:   return int((cols - len(_str))//2)               # -> use to allign item (horizontal)
def h(rows, _opt) -> int:   return int((rows - len(_opt)+5)//4)             # -> use to allign item (vertical)
def print_at(y,x,text) -> str:
    """
    Use this to print a line at a specific location in the 
    terminal. Very useful to allign items within the frame.
    """
    lines = text.split('\n')                # -> turn text into a list
    #: iterate through list and move each item to the correct location
    for i, line in enumerate(lines):
        move(y + i, x)
        print(line, end="")

# ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
#    CLASSES
# ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
class _id:
    def __init__(self): ...
    def id_handler(self, id): ...

class cli:
    def __init__(self): ...

    def _draw_canvas(self, width, height, style, **kwargs) -> SEQ:
        """
        ```cli._draw_canvas(10,15,frame(<inpt>))```
        """
        if kwargs: _tmpkwarg = list(kwargs.keys())                  # -> FEATURES: check id styles


    def _pos(self, x, y, **kwargs) -> COO:
        if kwargs: _tmpkwarg = list(kwargs.keys())                  # -> FEATURES: move item with certain ID to the position

        if str(_tmpkwarg[0]).lower() == 'id': return move(y,x)                            # -> NOTE: to be edited once the IDs functionality is implemented

cli = cli()