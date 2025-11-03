"""
NOTE: currently prettifycli.py isn't really implemented, 
making the usage only possible through the cli.py module.
"""
from core.cli import cli, _NoneType
from core._styling import rgb, PRESETS

import os

def a(): print('aaa')
def b(): print('bbb')
def c(): print('ccc')
def d(): print('ddd')
def e(): print('eee')

_content = {
    'option 1': a,
    'option 2': b,
    'option 3': _NoneType,
    'option 4': d,
    'option 5': e
}                           # -> KEY ERROR

# content = ['option 1', 'option 2', 'option 3', 'option 4', 'option 5']


cols, rows = os.get_terminal_size()
cli._pos(int((cols-30)/2),1)

content = [('test header', 'header'), 
           (_content, 'regular'),
           ("Press 'q' to exit!", 'bottom')]            # -> KEY ERROR

__content = [('test header', 'header'), 
           (['option 1','option 2','option 3','option 4','option 5'], 'regular'),
           ("Press 'q' to exit!", 'bottom')]                # -> WORKS

___content = ['option 1','option 2','option 3','option 4','option 5']           # -> WORKS

while True:
    cli._draw_canvas(30,10,['smooth',rgb(153, 222, 144)])
    # cli._write_content(content, (15,3), True)
    cli._write_content(___content, (10,3), True)