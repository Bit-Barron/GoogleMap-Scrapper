# A simple Python library to make your terminal outputs colorful and attractive (:
# Github : https://github.com/aminrngbr1122
# TODO Name: ColorT

from colorama import Fore

__version__ = '1.0.0'

class Print:
    
    def printG(text: any) -> None:
        """
        Prints the text in green color.
        """
        print(Fore.GREEN + str(text) + Fore.RESET)

    def printB(text: any) -> None:
        """
        Prints the text in blue color.
        """
        print(Fore.BLUE + str(text) + Fore.RESET)

    def printM(text: any) -> None:
        """
        Prints the text in magenta color.
        """
        print(Fore.MAGENTA + str(text) + Fore.RESET)

    def printR(text: any) -> None:
        """
        Prints the text in red color.
        """
        print(Fore.RED + str(text) + Fore.RESET)

    def printY(text: any) -> None:
        """
        Prints the text in yellow color.
        """
        print(Fore.YELLOW + str(text) + Fore.RESET)
        
    def restoreT():
        print(Fore.RESET)
        
        
# =================================================================================================

class inputs:

    def inputG(text_Input: str, color_front = Fore.WHITE) -> str:
        """
        Displays the input prompt in green color and returns the user input as a string.
        """
        return input(Fore.GREEN + str(text_Input) + color_front)

    def inputB(text_Input: str, color_front = Fore.WHITE) -> str:
        """
        Displays the input prompt in blue color and returns the user input as a string.
        """
        return input(Fore.BLUE + str(text_Input) + color_front)

    def inputM(text_Input: str, color_front = Fore.WHITE) -> str:
        """
        Displays the input prompt in magenta color and returns the user input as a string.
        """
        return input(Fore.MAGENTA + str(text_Input) + color_front)

    def inputR(text_Input: str, color_front = Fore.WHITE) -> str:
        """
        Displays the input prompt in red color and returns the user input as a string.
        """
        return input(Fore.RED + str(text_Input) + color_front)

    def inputY(text_Input: str, color_front = Fore.WHITE) -> str:
        """
        Displays the input prompt in yellow color and returns the user input as a string.
        """
        return input(Fore.YELLOW + str(text_Input) + color_front)
    
# =====================================================================================================

def restoreT() -> None : ...