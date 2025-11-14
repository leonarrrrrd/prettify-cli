# ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
#    IMPORTS
# ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
from prettifycli import prettify, rgb
from prettifycli import prettify_print as pprint

from core._styling import PRESETS

# ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
#    FUNCTIONS
# ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
def function_a(): print('SUCCESS!')
def function_b(): print('SUCCESS!')
def function_c(): print('SUCCESS!')
def function_d(): print('SUCCESS!')
def function_e(): print('SUCCESS!')

# ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
#    PRETTIFY CONTENT
# ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
prettify_content   = [
    'option-1',
    'option-2',
    'option-3',
    'option-4',
    'option-5'
]
prettify_functions = [
    function_a,
    function_b,
    function_c,
    function_d,
    function_e
]

# ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
#    PRETTIFY INITIALIZATION
# ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
prettify.position(3,2)
prettify.iterable_window(False)

prettify.text_padding(13,3)
prettify.window_header(rgb(255,0,0) + PRESETS.bold + 'test '+rgb(100,255,0)+'header' + PRESETS._reset)
prettify.window_bottom(rgb(122, 122, 122) + "Press 'q' to exit!" + PRESETS._reset)

#prettify.add_functions(prettify_functions)

# ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
#    RUN CLI
# ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
while True:
    prettify.create_window(30, 41, 'double', rgb(153, 222, 144))
    pprint.at(37,3,
              f"""{rgb(51,212,134)}Lorem ipsum dolor sit amet, consetetur sadipscing elitr,
sed diam nonumy eirmod tempor invidunt ut labore et dolor
magna aliquyam erat, sed diam voluptua. At vero eos et
accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren,
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem
ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy
eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed
diam voluptua. At vero eos et accusam et justo duo dolores et ea
rebum. Stet clita kasd gubergren, no sea takimata sanctus est
Lorem ipsum dolor sit amet.{PRESETS._reset}""")
    prettify.add_content(prettify_content)