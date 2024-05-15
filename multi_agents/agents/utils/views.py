from colorama import Fore, Style
from enum import Enum

callbackfunc  = None

class AgentColor(Enum):
    RESEARCHER = Fore.LIGHTBLUE_EX
    EDITOR = Fore.YELLOW
    WRITER = Fore.LIGHTGREEN_EX
    PUBLISHER = Fore.MAGENTA
    REVIEWER = Fore.CYAN
    REVISOR = Fore.LIGHTWHITE_EX
    MASTER = Fore.LIGHTYELLOW_EX

def set_callback_func(func):
    global callbackfunc
    callbackfunc = func

def print_agent_output(output:str, agent: str="RESEARCHER"):
    if callbackfunc is None:
        print(f"{AgentColor[agent].value}{agent}: {output}{Style.RESET_ALL}")
    else:
        callbackfunc(agent, output)
