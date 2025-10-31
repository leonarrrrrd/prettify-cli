from core.cli import cli
from core._styling import rgb

import os

rows, cols = os.get_terminal_size()

cli._pos(int((rows-30)/2),3)

while True:
    cli._draw_canvas(30,10,['double',rgb(153, 222, 144)])
    cli._write_content(['option 1', 'option 2', 'option 3', 'option 4', 'option 5'], (6,2), True)