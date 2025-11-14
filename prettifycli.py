"""
**prettifycli** aims to make the creation of CLI interfaces
for the windows terminal as intuitive as possible. Using
prettifycli a complex CLI menu can be created within a few
lines. It combines all necessary utilities a user might 
need to create a CLI-based software. Relying on only 
This file links all functionalities of prettifycli into
more intuitive functions that can be called by the user.
"""
# ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
#    IMPORTS
# ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
import sys, os
sys.dont_write_bytecode = True

from core._styling      import rgb as _RGB
from core._styling      import PRESETS

from core.prettify_err  import DATATYPE_ERROR, WHATTHEFUCK

from core.cli           import cli as PCLI
from core.cli           import SEQ, CMD, FUL, ITR
from core.cli           import _NoneType, move, _print_at

# ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
#    PUBLIC FUNCTIONS
# ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
def rgb(r, g, b, background=False): return _RGB(r,g,b,background)

# ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
#    PRIVATE FUNCTIONS
# ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
def _typing(item, __type:object, __var) -> Exception | None:
    if type(item) == __type: ...
    else:
        try: item = __type(item)
        except Exception: return DATATYPE_ERROR(f'prettify expected {str(__type)} but got {str(type(item))} for {__var}! Maybe you have used the wrong type?')

# ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
#    CLASSES
# ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
class prettify_print:
    def __init__(self): ...

    def at(self, x:int, y:int, text:str) -> SEQ:
        _typing(x, int, 'x')
        _typing(y, int, 'y')
        _typing(text, str, 'text')
        _print_at(y, x, text)

class prettify:

    #: core window functions
    __is_iterable = False
    __show_cursor = True
    __pos         = tuple

    #: selection menu
    __functions   = []
    __MENU        = dict | list

    #: style elements
    __decorators  = list
    __header      = str
    __bottom      = str

    def __init__(self): ...

    def position(self, x:int, y:int) -> callable:
        _typing(x, int, 'x')
        _typing(y, int, 'y')
        PCLI._pos(x, y)
    def iterable_window(self, is_iterable:bool) -> bool:
        _typing(is_iterable, bool, 'is_iterable')
        self.__is_iterable = is_iterable
        if is_iterable == False: self.__show_cursor = False
    def add_functions(self, functions:list) -> FUL:
        self.__functions = functions
    def create_window(self, width:int, height:int, frame_style:str, frame_color:str|CMD) -> SEQ:
        if self.__show_cursor == False: print('\033[?25l', end="")
        else: ...
        _typing(width, int, 'width')
        _typing(height, int, 'height')
        _typing(frame_style, str, 'frame_style')
        PCLI._draw_canvas(width, height, [frame_style, frame_color])

    def text_padding(self, x:int, y:int) -> SEQ:
        _typing(x, int, 'x')
        _typing(y, int, 'y')
        self.__pos = (x, y)
    def window_header(self, text:str) -> SEQ:
        _typing(text, str, 'text')
        self.__header = text
    def window_bottom(self, text:str) -> SEQ:
        _typing(text, str, 'text')
        self.__bottom = text

    def add_content(self, text:list) -> ITR:
        _typing(text, list, 'text')
        if self.__is_iterable == True:
            if len(text) == len(self.__functions):
                self.__MENU = dict(zip(text, self.__functions))

            elif len(text) < len(self.__functions):
                for extra in range(len(self.__functions) - len(text)):
                    text.append('<empty'+str(extra)+'>')
                self.__MENU = dict(zip(text, self.__functions))

            elif len(text) > len(self.__functions):
                for extra in range(len(text) - len(self.__functions)):
                    self.__functions.append(_NoneType)
                self.__MENU = dict(zip(text, self.__functions))

            if len(list(self.__MENU.keys())) != 0 and (self.__header != '' or self.__bottom != ''): 
                PCLI._write_content(
                    [(self.__header, 'header'), (self.__MENU, 'regular'), (self.__bottom, 'bottom')], 
                    self.__pos, 
                    self.__is_iterable)
            elif len(list(self.__MENU.keys())) != 0:
                PCLI._write_content(self.__MENU, self.__pos, self.__is_iterable)
            else:
                PCLI._write_content(text, self.__pos, self.__is_iterable)

        if self.__is_iterable == False:
            if type(self.__header) != type or type(self.__bottom) != type:
                PCLI._write_content([(self.__header, 'header'), (text, 'regular'), (self.__bottom, 'bottom')], 
                                    self.__pos, 
                                    self.__is_iterable)
            else: return PCLI._write_content(text, self.__pos, self.__is_iterable)

prettify       = prettify()
prettify_print = prettify_print()