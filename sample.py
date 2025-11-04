# ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
#    IMPORTS
# ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
from prettifycli import prettify, rgb
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
prettify.position(15,5)
prettify.iterable_window(True)

prettify.text_padding(10,3)
prettify.window_header(rgb(255,0,0) + PRESETS.bold + 'test '+rgb(100,255,0)+'header' + PRESETS._reset)
prettify.window_bottom(rgb(122, 122, 122) + "Press 'q' to exit!" + PRESETS._reset)

prettify.add_functions(prettify_functions)

# ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
#    RUN CLI
# ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
while True:
    prettify.create_window(40, 20, 'double', rgb(153, 222, 144))
    prettify.add_content(prettify_content)