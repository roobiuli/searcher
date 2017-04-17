#!/usr/bin/python
import os
import sys
from subprocess import Popen, PIPE
import re
import argparse
#----- Take every file in a location and gather all the defined variables and 
#----- Take the list and loop it and compare each element if it`s found, return it , also if not found gather it in another list and return it as well
#----- Create report for each file found with the variables found and not found 


par = argparse.ArgumentParser(description="Little PRG")
par.add_argument("-F", required=False, dest="< File With variables to load >")
par.add_argument("-p", required=True, dest="p", help="Path to files containing variables")
args = par.parse_args()



def bash(x):
    """
    Bash Function to move arround
    """
    proc = Popen(x, shell=True, stdout=PIPE, stderr=PIPE)
    out, err = proc.communicate()
    return out.strip(), err, proc.returncode


def looper_constructer(path):
    found = {}
    if  os.path.isdir(path):
        files = bash(["ls", path])[0].split('\n')
        for file in files:
            try:
                with open(path + "/" + file, "r") as f:
                    lines = f.read()
                    match = re.findall("(\%\(\w+\S\)+s)", \
                                                                     lines)
                    if len(match) != 0:
                        found[file] = match
                    f.close()
            except IOError:
                print "Could not open file {}/{}".format(path, file)
                sys.exit(1)
        return found


#looper_constructer(".")
def main():
    files = looper_constructer(args.p)
    print files

main()
