"""
"""

# ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
#    IMPORTS
# ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
import sys, os
sys.dont_write_bytecode = True

# ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
#    MAIN
# ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
def rgb(r,g,b,bg=False):
    """
    Can set text to any color on the rgb spectrum. Works
    on the windows terminal exclusively. Does not work in
    combination with the `curses` library as escape
    sequences are blocked by the library. It does however,
    work without any external library or the `mscvrt`
    library that prettifygui is based on. The `rgb`
    function can be used in normal print statements and
    CLI designs.\n
    **USAGE**: `print("Hello" + rgb(255, 128, 0) + "World!")`
    """
    return '\033[{};2;{};{};{}m'.format(48 if bg else 38,r,g,b)

# ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
#    CLASSES
# ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
class PRESETS:
    """
    Preset color templates and more.
    """
    on        = rgb(0, 204, 0)
    off       = rgb(255, 0, 0)
    _reset     = '\033[0m'
    err       = '│ ' + rgb(153, 0, 0) + 'ERROR' + _reset + ': '
    suc       = rgb(0, 179, 0)
    info      = '│ ' + rgb(230, 230, 0) + 'INFO' + _reset + ': '
    warn      = '│ ' + rgb(255, 117, 26) + 'WARN' + _reset + ': '
    success   = '│ ' + rgb(51, 204, 51) + 'SUCCESS' + _reset + ': '
    line      = rgb(179, 204, 255)
    highlight = rgb(102, 0, 102)
    prefix    = rgb(89, 89, 89)
    gs        = rgb(128, 128, 255)
    file_high = rgb(0, 179, 179)
    bold      = '\x1b[1m'

    def __init__(self): ...