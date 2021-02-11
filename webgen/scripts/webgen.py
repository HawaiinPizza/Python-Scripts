#!/bin/python
# https://docs.python.org/3/library/configparser.html for config
# TODO
"""come up with some way to have the path show"""
import configparser as CP
import os
import markdown
import regex

config =  CP.ConfigParser()
config.read("../config.ini")

def makepath(path):
    if (not os.access(path, os.R_OK)):
        os.makedirs(path)
makepath(config["def"]["build"])

os.chdir(config["def"]["path"])
# result = [os.path.join(dp, f) for dp, dn, filenames in os.walk(config["def"]["path"]) for f in filenames ]
result = [os.path.join(dp, f) for dp, dn, filenames in os.walk(config["def"]["path"]) for f in filenames ]
pages=[]
checkregex = regex.compile(config["def"]["keep"])
ignoreFiles  = config["def"]["ignore"].split(",")
for i in result:
    tmpfile=(i  [len(config["def"]["path"]):] )
    if(checkregex.match(os.path.basename(tmpfile)) and tmpfile not in ignoreFiles):
        pages.append(tmpfile.split("/",1)[1])


for i in pages:
    with open(i) as page:

        data=''.join(page.readlines())
        pagehtml=markdown.markdown(data)
        (path, filename) = os.path.split(i)
        head = ''.join(['../' for i in range(0, path.count("/"))])
        if(path!=""):
            head+="../"

        # Make tilebar 
        filehtml=""
        if(path):
            filehtml=( path + "/" )
        

        pagehtml="\n<ul id=nav-bar>\n"+''.join([f"<li> <a href=\"{head}{j[0:-3]}.html\"> {os.path.basename(j)[0:-3]} </a>  </li> \n" for j in pages])  +  "</li>\n\n" + pagehtml
        # pagehtml="\n<ul id=nav-bar>\n"+''.join([f"<li> {j} WOW  </li> \n" for j in pages])  +  "</li>\n\n" + pagehtml
        pagehtml=f"<head> <title> My shit templating engine </title> <link rel=\"stylesheet\" href=\"{head}styles.css\" </head>\n<body>\n" + pagehtml
        pagehtml+="\n</body>"





        filehtml =  config["def"]["build"] + "/" + filehtml + filename[0:-3]+".html" 
        print(filehtml)
        makepath(config["def"]["build"] + "/" + path ) 
        # config["def"]["buiod"]+
        open(filehtml, "w+").write(pagehtml)
open("build/WOW.html", "w").write("FUCK")


