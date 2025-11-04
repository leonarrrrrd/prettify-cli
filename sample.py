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

header1 = rgb(255,0,0) + PRESETS.bold + 'test '+rgb(100,255,0)+'header' + PRESETS._reset
header2 = 'test header'
header3 = '123456789012345678901234567890123'

content = {
    'option 1': a,
    'option 2': b,
    'option 3': _NoneType,
    'option 4': d,
    'option 5': e
}
_content = [(header1, 'header'), 
           (content, 'regular'),
           (rgb(122, 122, 122) + "Press 'q' to exit!" + PRESETS._reset, 'bottom')]

__content = [('test header', 'header'), 
           (['option 1','option 2','option 3','option 4','option 5'], 'regular'),
           ("Press 'q' to exit!", 'bottom')]

___content = ['option 1','option 2','option 3','option 4','option 5']


cols, rows = os.get_terminal_size()
cli._pos(int((cols-30)/2),1)

while True:
    cli._draw_canvas(30,10,['smooth',rgb(153, 222, 144)])
    # cli._write_content(content, (15,3), True)
    cli._write_content(_content, (10,3), True)