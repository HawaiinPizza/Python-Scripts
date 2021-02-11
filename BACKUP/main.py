#!/bin/python
import configparser
import re
import lib

def __main__():
    config = configparser.ConfigParser()
    config.read("/home/zaki/Projects/Programm/bookmarks/config.ini")


    def convertFiles(abbr, path, command, _funcs):
        lists = []

        for func in _funcs:
            lists.append(func(abbr, path, command, config))
        return lists
    funcs = [lib.zsh, lib.dmenufm, lib.emacs]


    exports = {}
    with open(config["DEFAULT"]["book"],"r") as f:
        for line in f:
            line=line[:-1]
            if "#" in line or re.match("^\s*$", line):
                continue

            (abbr, path) = (re.split(r'\s+', line, 1))
            (command, path)= (path.split("/",1 ))
            path = "/"+path
            tmp = convertFiles(abbr, path, command, funcs)
            for (path, alias) in tmp:
                if(path not in exports):
                    exports[path]=[alias]
                else:
                    exports[path].append(alias)

                    
    for path in exports:
        with open(path, "w") as fileWrite:
            fileWrite.write('\n'.join(dict(dict.fromkeys(exports[path]))))

