import os, colorama
from typing import overload
from ColorTER import *
import arabic_reshaper
from bidi.algorithm import get_display

__version__ = ['2.0.0']

pprint = '0'

# Colors Print
class Colors:
    """
    Colors Object
    Useage:
    
    ```python
    from Pprints import *
    from os import environ

    environ['print_access_request_library_PPrint'] = '1'

    colors = Colors()
    print = Pprint(Colors.RED).print
    input = Pprint(Colors.RED).input

    print(text=input('لطفا متن فارسی خود را وارد کنید : \n'))
    ```
    """
    RED            = colorama.Fore.RED
    GREEN            = colorama.Fore.GREEN
    RESET            = colorama.Fore.RESET
    BLUE            = colorama.Fore.BLUE
    YELLOW            = colorama.Fore.YELLOW
    CYAN            = colorama.Fore.CYAN
    MAGENTA            = colorama.Fore.MAGENTA
    BLACK            = colorama.Fore.BLACK
    WHITE            = colorama.Fore.WHITE

try:

    class _Fnc:
        def __init__(self, color) -> None:
            self.color = color
            global pprint
            if 'print_access_request_library_PPrint' not in os.environ:
                os.environ['print_access_request_library_PPrint'] = pprint
            if os.environ['print_access_request_library_Pprint'] == '0':
                Print.printY(f'You are using Pprint library :')
                Print.printM(f'\t version: {__version__[0]} (:')
            
        @overload
        def print(self, text: str) -> None: ...

        def print(self, text: str) -> None:
            reshaped_text = arabic_reshaper.reshape(u'{0}'.format(text))
            bidi_text = get_display(reshaped_text, upper_is_rtl=True, encoding='utf-8')
            print(self.color + bidi_text + Colors.RESET)
            
        @overload
        def input(self, text: str) -> None: ...

        def input(self, text: str) -> None:
            reshaped_text = arabic_reshaper.reshape(u'{0}'.format(text))
            bidi_text = get_display(reshaped_text, upper_is_rtl=True, encoding='utf-8')
            return input(self.color + bidi_text + Colors.RESET)

    class Pprint(_Fnc):
        def __init__(self, color: any = Colors.WHITE):
            self.color = color
            super().__init__(color)

        def print(self, text: str) -> None:
            translation_table = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")
            super().print(text.translate(translation_table))
            
        def input(self, text : str) -> str:
            translation_table = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")
            return super().input(text.translate(translation_table))
            
except Exception as e:
    
    Print.printY("Libray Pprint Error !")