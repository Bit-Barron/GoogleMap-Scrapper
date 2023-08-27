#  ____   ____         _         _     _      ___  ____     __   
# |  _ \ |  _ \  _ __ (_) _ __  | |_  | |    |_ _|| __ )   / / _ 
# | |_) || |_) || '__|| || '_ \ | __| | |     | | |  _ \  | | (_)
# |  __/ |  __/ | |   | || | | || |_  | |___  | | | |_) | S | |  _ 
# |_|    |_|    |_|   |_||_| |_| \__| |_____||___||____/  | | (_)
#                                                          \_\   

"""
Pprints Library
~~~~~~~~~~~~~~~~~~~~~

The PPrints library is an auxiliary library for printing in the terminal in Farsi language and Farsi color printing written with Python language for humans.
Basic usage:

```python
from Pprints import *
from os import environ

environ['print_access_request_library_PPrint'] = '1'

colors = Colors()
print = Pprint().print
input = Pprint().input

print(text=input('لطفا متن فارسی خود را وارد کنید : \n'))
```

:Library used in the code: arabic_reshaper, bidi
:Copyright: (c) 2023 Amin Rngbr.
:license: MIT
"""

import sys

sys.dont_write_bytecode = True

from .Ppr_class import *

this : dict = {}