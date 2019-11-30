# This script can launch either both, or a single script of
# the Python assignment. Just follow the prompts.

import subprocess
import os
import stat
import sys
import time


class color:
    BOLD = '\033[1m'
    RED = '\033[91m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'


def ExecutePyBankProgram():
    bankScriptLoc = os.path.join("PyBank", "main.py")
    subprocess.call(['python', bankScriptLoc])


def ExecutePyPollProgram():
    pollScriptLoc = os.path.join("PyPoll", "main.py")
    subprocess.call(['python', pollScriptLoc])


asciiBarf = '''
 ___       _ _                                    _
| . \ _ _ | | | ___ ._ _ _  ___  _ _ _  ___  _ _ | |__
|  _/| | ||   |/ . \| ' ' |/ ._>| | | |/ . \| '_>| / /
|_|  `_. ||_|_|\___/|_|_|_|\___.|__/_/ \___/|_|  |_\_|
     <___|                                                '''

##################################################################
print(asciiBarf)
print("                                                Spaar")
print(
    f"\n{color.BOLD}Choices of Execution:{color.END}\nPyBank {color.RED}[1]{color.END}\nPyPoll {color.RED}[2]{color.END}\nBoth   {color.RED}[3]{color.END}\n-----------------------")

ans = int(input(f"{color.BOLD}Enter your selection:{color.END} "))

if ans == 1:
    print(f"\n{color.UNDERLINE}Loading PyBank..{color.END}")
    time.sleep(1)
    print(f"----------------------------------------------\n**********************************************\n----------------------------------------------")
    ExecutePyBankProgram()
elif ans == 2:
    print(f"\n{color.UNDERLINE}Loading PyPoll..{color.END}")
    time.sleep(1)
    print(f"----------------------------------------------\n**********************************************\n----------------------------------------------")
    ExecutePyPollProgram()
elif ans == 3:
    print(f"\n{color.UNDERLINE}Loading PyBank..{color.END}")
    time.sleep(1)
    print(f"----------------------------------------------\n**********************************************\n----------------------------------------------")
    ExecutePyBankProgram()
    print(f"\n{color.UNDERLINE}Loading PyPoll..{color.END}")
    time.sleep(1)
    print(f"----------------------------------------------\n**********************************************\n----------------------------------------------")
    ExecutePyPollProgram()
else:
    sys.exit("You must input a valid option (1, 2, or 3)")
