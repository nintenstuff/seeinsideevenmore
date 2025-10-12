# where the magic happens

import time
from colorama import Style

def die():
    time.sleep(4)
    print(Style.RESET_ALL)
    quit()