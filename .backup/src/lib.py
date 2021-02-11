
# Parsing functions
from os.path import basename, abspath
def zsh(abbr, path, command, config)->(str, str):
    # x=open
    # e=edit
    if(command == "x"):
        return  (config["DEFAULT"]["zsh"], f'alias -g "{abbr}= setsid $OPEN {path}  2>/dev/null 1>&2 "')
    if(command == "e"):
        return  (config["DEFAULT"]["zsh"], f'alias -g "{abbr}= $EDITOR {path}"')
    if(command == "xx"):
        return  (config["DEFAULT"]["zsh"], f'alias -g "{abbr}= devour $OPEN {path}  2>/dev/null 1>&2 "')
    elif(command == ""):
        return  (config["DEFAULT"]["zsh"], f'alias -g "{abbr}= {path}"')
    else:
        raise KeyError(f"Command {command} not listed for life {abbr} {command}{path}")


def dmenufm(abbr, path, command, config)->(str, str):
    path = abspath(path) 
    return   (config["DEFAULT"]["dmenufm"], f'{basename(path)} - {path}')

