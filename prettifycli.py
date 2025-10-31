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

from core._styling      import *
from core.prettify_err  import *
from core.cli           import cli

# ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
#    FUNCTIONS
# ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
def __typing(item, __type:object, __var) -> Exception | None:
    if type(item) == __type: ...
    else:
        try: item = __type(item)
        except Exception: return DATATYPE_ERROR(f'prettify expected {str(__type)} but got {str(type(item))} for {__var}! Maybe you have used the wrong type?')

# ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
#    CLASSES
# ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
class prettify:
    def __init__(self): ...

    def draw_frame(self, width, height, frame_style, frame_col, _id) -> callable[list]:
        __typing(width,int,'prettify.draw_frame(width=<int>)')
        __typing(height,int,'prettify.draw_frame(height=<int>)')
        __typing(frame_style,str,'prettify.draw_frame(frame_style=<str>)')
        __typing(frame_col,str,'prettify.draw_frame(frame_col=<str>)')
        if _id: 
            __typing(_id,list,'prettify.draw_frame(id=<list>)')
            cli._draw_canvas('', '', '', _id)

        cli._draw_canvas(width, height, [frame_style, frame_col])
    
    def position(self, x, y) -> callable[tuple]:
        __typing(x,int,'prettify.position(x=<int>)')
        __typing(y,int,'prettify.position(y=<int>)')

        cli._pos(x, y)

    def content(self, text, is_iterable) -> list | dict: ...