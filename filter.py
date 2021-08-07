import glob, re
import sys, os, shutil, getopt

filetype = "pdf"

# In case no argument provided
if len(sys.argv) == 1:
    filetype = input("Insert the file type: ")
    source = input("Insert the source or reference file: ")

## Taking option from Command-Line Input
try:
    opts, args = getopt.getopt(sys.argv[1:], "hr:f:", [])
except getopt.GetoptError:
    print('ERROR!! Wrong Argument\n')
    print('HOW TO USE??\n$ python filter.py -r <reference file> -f <filetype-format>')
    exit()

for option, argument in opts:
    if option in ("-h"):
        print('HOW TO USE??\n$ python filter.py -r <reference file> -f <filetype-format>')
        exit()
    elif option in ("-f"):
        filetype = argument
    elif option in ("-r"):
        source = argument

lists = glob.glob(f"*.{filetype}")
fillist = []
for filelist in lists:
    filelist = filelist[:filelist.find(f".{filetype}")].lower()
    fillist.append(filelist)

if len(fillist) == 0:
    print("Maybe wrong format?")
    exit()

try:
    datahand = open(source, "r")
except:
    print("ERROR: Could not open", source)
    exit()

reference = datahand.read().strip().split("\n")

newpath = os.path.join("filtered")
if not os.path.exists(newpath):
    os.makedirs(newpath)
else:
    shutil.rmtree(newpath)
    os.makedirs(newpath)

for name in fillist:
    if name in reference:
        try:
            __src = name + f".{filetype}"
            dest = os.path.join(newpath, __src)
            shutil.copy(__src, dest)
        except:
            namecap = name.capitalize()
            if namecap in lists:
                __src = namecap + f".{filetype}"
                dest = os.path.join(newpath, __src)
                shutil.copy(__src, dest)
            else:
                __src = name.upper() + f".{filetype}"
                dest = os.path.join(newpath, __src)
                shutil.copy(__src, dest)
