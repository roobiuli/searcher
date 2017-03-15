#!/usr/bin/python
import os
import sys
from subprocess import Popen, PIPE
import re

#----- Take every file in a location and gather all the defined variables and 
#----- Take the list and loop it and compare each element if it`s found, return it , also if not found gather it in another list and return it as well
#----- Create report for each file found with the variables found and not found 

def bash(x):
    """
    Bash Function to move arround
    """
    proc = Popen(x, shell=True, stdout=PIPE, stderr=PIPE)
    out, err = proc.communicate()
    return out, err, proc.returncode

#def search(var):
#    re.search(^(\%\())

def looper_constructer(path):
    found_variables = []

    if  os.path.isdir(path):
        files = bash(["ls", path])[0].split('\n')
        for file in files:
            
            #filefull = path + "/" + file
            try:
                with open(path + "/" + file, "r") as f:
                    lines =f.read().splitlines()
                    print lines
                    f.close()
            except IOError:
                print "Could not open file {}/{}".format(path,file)
                sys.exit(1)
        


looper_constructer(".")

#def main():
#    return None
