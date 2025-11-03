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

from core.prettify_err import (DATATYPE_ERROR, COORDINATE_ERROR)
from core._styling import (rgb, PRESETS)

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
type ITR = list[SEQ]                            # -> indicating an iterable object (options in frame)
type CMD = str | bytes                          # -> indicating a terminal command executed in os.system()

# ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
#    VARIABLES
# ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
HISTORY     = []                            # -> stores current menu pages for an eventual 'Return' option
ESC         = '\033['                       # -> PRESETS._reset
COLS, ROWS  = os.get_terminal_size()        # -> get the number of columns and rows of the currently active terminal
STYLES      = ['default', 'double', 'smooth']
TXT_TYPE    = ['default','header','bottom']

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
def reset() -> str:         print(PRESETS._reset, end="")                   # -> reset escape sequence (use to go ack to default text after changing color etc...)
def w(cols, _str) -> int:   return int((cols - len(_str))//2)               # -> use to allign item (horizontal)
def h(rows, _opt) -> int:   return int((rows - len(_opt)+5)//4)             # -> use to allign item (vertical) 
def center(chars) -> int:   return int((ROWS - len(chars))/2)

def _color(code) -> str:     print(f"{code}", end="")                        # -> change color
def _print_at(y,x,text) -> str:
    """
    Use this to print a line at a specific location in the 
    terminal. Very useful to allign items within the frame.
    `print_at(y,x,<text>)`
    """
    lines = text.split('\n')                # -> turn text into a list
    #: iterate through list and move each item to the correct location
    for i, line in enumerate(lines):
        move(y + i, x)
        print(line, end="")
def _styles(_mode) -> list:
    #:                              0    1    2    3    4    5
    if _mode == 'default': return ['│', '─', '┌', '└', '┐', '┘']
    if _mode == 'double':  return ['║', '═', '╔', '╚', '╗', '╝']
    if _mode == 'smooth':  return ['│', '─', '╭', '╰', '╮', '╯']
    if _mode != 'default' or _mode != 'double' or _mode != 'smooth': return [_mode for i in range(6)]
def _NoneType() -> None: return None                                        # -> use in selection menu when option isn't linked

# ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
#    CLASSES
# ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
class _id:
    def __init__(self): ...
    def id_handler(self, id): ...

class cli:
    POS = tuple             # -> self.POS = (y,x)
    TXT = str | list

    LEN_FRAME = int
    HI_FRAME  = int

    index = 0               # -> current index for iterable objects

    def __init__(self): ...
    #: for the love of god and everything holy, do NOT use these functions!
    # ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
    #    PRIVATE CLI FUNCTIONS
    # ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
    def __new_terminal(self) -> CMD: os.system('wt new-tab -p "Command Prompt" -d "%cd%" cmd')
    def __terminal_size(self, cols, rows) -> CMD: os.system('mode con cols='+str(cols)+' lines='+str(rows))
    def __text(self, content_list:list[tuple]) -> SEQ: return content_list[0], content_list[1], content_list[2]
    def __call(self, __index, __options, __dict) -> callable:
        if __options[__index] in __dict: __dict[__options[__index]]()
        else: ...
    def __enum(self, text, pos) -> SEQ:
        #: list items in frame
        for i, _opts in enumerate(text):
            if len(pos) == 2: move(self.POS[0]+i+1+pos[1],self.POS[1]+1+pos[0])     # -> place text into frame
            else: move(self.POS[0]+i+1,self.POS[1]+1)
            if i == self.index:                                                     # -> iterate through options by increasing index
                _color(rgb(137, 222, 144) + "> " + PRESETS._reset)
                print(_opts)
                reset()
            else:
                print(_opts)    

    def __get_key(self, text, options) -> KEY | None | FUN:
        #: engage key listener
        key = key_listener()

            #: listen to key hits
        if key == 'UP': self.index = (self.index - 1) % len(text)
        elif key == 'DOWN': self.index = (self.index + 1) % len(text)
        elif key in ('ENTER', '\n'):
            #: allow to return functions when text is a dictionary
            if type(text) == dict: self.__call(self.index, options, text)
            #: return content elements regardless of type
        elif key.lower() == 'q': exit()
    def __place_decorators(self, header, regular, bottom, pos) -> SEQ:
        frame_pad = (self.LEN_FRAME - 2 - len(header[0])) // 2          # -> get padding of frame (distance from frame elements on x-axis)
        #: place header
        move(self.POS[0] + 1, self.POS[1] + 1)
        print(f"{(' ' * frame_pad)+' '}{header[0]}{' ' * (self.LEN_FRAME - 2 - len(header[0]) - frame_pad)}")
        #: place subtext
        move(self.POS[0] + self.HI_FRAME + 2, self.POS[1] + 1)
        print(bottom[0])

        if type(regular[0]) == list:
            self.__enum(regular[0], pos)
            self.__get_key(regular[0], '')
            # if regular[0][self.index] in regular[0]: regular[0][self.index]

        if type(regular[0]) == dict:
            self.__enum(list(regular[0].keys()), pos)
            self.__get_key(regular[0], list(regular[0].keys()))

    #: position frame in terminal
    def _pos(self, x, y, **kwargs) -> COO | Exception:
        """
        This might be unnecessary in the future? Determine position
        of frame and position it accordingly. 
        """
        if kwargs: 
            _tmpkwarg = list(kwargs.keys())                             # -> FEATURES: move item with certain ID to the position
            if str(_tmpkwarg[0]).lower() == 'id': return move(y,x)      # -> NOTE: to be edited once the IDs functionality is implemented
        if type(x) != int or type(y) != int: raise DATATYPE_ERROR('prettify expected type<int> but got '+str(type(x))+' at _pos(x,y)! Maybe you used the wrong type?')
        else:
            if x > COLS or y > ROWS: raise COORDINATE_ERROR('Coordinates in _pos(x,y,**kwargs) exceed terminal size.')
            else: self.POS = (y,x)
    #: print frame at position in terminal
    def _draw_canvas(self, width, height, style, **kwargs) -> SEQ:
        """
        ```cli._draw_canvas(10,15,frame(<inpt>))```
        """
        self.LEN_FRAME = width
        self.HI_FRAME  = height

        if kwargs: _tmpkwarg = list(kwargs.keys())                  # -> FEATURES: check id styles
        frame_elements = _styles(style[0])                           # -> get frame elements
        frame_color    = style[1]                                   # -> get frame colors
        if frame_color == 'default' or frame_color == 'd' or frame_color == None: 
            frame_color = PRESETS._reset
        for i in frame_elements: 
            frame_elements[frame_elements.index(i)] = frame_color + i + PRESETS._reset

        clear()    
        #: print at the user position
        #: left part of frame including corners 
        _print_at(self.POS[0],self.POS[1],
                 (frame_elements[2]+'\n')+
                 str((frame_elements[0]+'\n')*int(height))+
                 (frame_elements[3]+'\n'))
        #: top part of frame, excluding corners
        _print_at(self.POS[0],int(self.POS[1])+1,
                 str((frame_elements[1])*int(width)))
        #: right part of frame, including corners
        _print_at(self.POS[0],int(self.POS[1])+1+int(width),
                 (frame_elements[4]+'\n')+
                 str((frame_elements[0]+'\n')*int(height))+
                 (frame_elements[5]+'\n'))
        #: bottom part of frame, excluding corners
        _print_at(self.POS[0]+1+int(height), self.POS[1]+1,
                 str((frame_elements[1])*int(width)))
    #: print text in the frame at certain position
    def _write_content(self, text:dict|list|list[tuple], pos:tuple, is_iterable:bool) -> SEQ | ITR:
        #: iterable items
        if is_iterable == True:                             # -> print all other options
            if type(text) == dict: 
                options = list(text.keys())
                self.__enum(options, pos)
                return self.__get_key(text, options)

            elif type(text) == list:                    # -> check for text definitions
                for i in range(len(text)):
                    if type(text[i]) == tuple:
                        header, regular, bottom = self.__text(text)          # -> define text types
                        return self.__place_decorators(header, regular, bottom, pos)
                    else:
                        self.__enum(text, pos)
                        return self.__get_key(text, '')
            
            else: raise DATATYPE_ERROR('prettify expected type<dict> or type<list> for cli._write_content(text) but received '+str(type(text))+'!')

        elif is_iterable == False: ...

cli = cli()