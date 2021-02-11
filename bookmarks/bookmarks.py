#!/bin/python
import re
import lib
import json
import os

config = json.loads(open("./config.json").read())



def convertFiles(abbr, path, command, _funcs):
    lists = []

    for func in _funcs:
        lists.append(func(abbr, path, command, config))
    return lists

zsh = lib.zsh(config["output"]["zsh"])
dmenufm = lib.dmenufm(config["output"]["dmenufm"])
emacs = lib.emacs(config["output"]["emacs"])
dmenufmBook = lib.dmenufmBook(config["output"]["dmenu"])
fzf = lib.fzf(config["output"]["fzf"])
classes = [zsh, dmenufm, emacs, dmenufmBook,fzf ]
lines = [ ]
for file in config["input"]["files"]:
    if(os.path.exists(file)):
        lines=(open(file, "r").read().splitlines())
for dir_regex in config["input"]["dirs"]:
    dir,regex = list(dir_regex.items())[0]
    if(os.path.exists(dir)):
        files = (os.listdir(dir))
        regexTmp = re.compile(regex)
        for file in files:
            if(regexTmp.match(file)):
                lines+=(open(dir+""+file, "r").read().splitlines())
# lines = open(config["input"]["book"],"r").read().splitlines()
for clas in classes:
    clas.write(lines)
"""
"""
