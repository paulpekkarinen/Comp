# This program compiles all .cpp files in the current directory and
# places .o files in /obj subdirectory, then links a binary file.
# Use this program only if you understand what you just read.
# Tested in Fedora Linux 39.

# imports
import os
import sys

# variables, target is the executable name
target = "teemu"
comp_flags = "-g -Wall -std=c++17 -fexceptions"
linker_flags = "-lSDL2main -lSDL2"
current_path = os.getcwd()
obj_folder = "obj"

# check if /obj exists
if not os.path.isdir(obj_folder):
    # try to create /obj folder, this "should" work
    os.mkdir(obj_folder);

# read filenames to a list from the current directory
files = []
for file in os.listdir(current_path):
    # check only .cpp files
    if file.endswith('.cpp'):
        files.append(file)

# stop if no .cpp files in this directory
if not files:
    sys.exit("No .cpp files found in this folder.")

# compile .cpp files to .o files, performing a "full build"
obj_files = ""
for filename in files:
    # create .o filename with the obj folder
    obj_file=obj_folder+"/"+filename.replace(".cpp", ".o")
    
    # create the command line for compiling a .cpp file
    comp = "g++ "+comp_flags+" -c "+filename+" -o "+obj_file
    
    # append .o file to a continuous string for the linker
    obj_files+=obj_file+" "
    
    # show the command and call the compiler from python
    print(comp)
    os.system(comp)

# create linker command
link = "g++ -o "+target+" "+obj_files+linker_flags

# show the command and call the linker from python
print(link)
os.system(link)
 
print("Ready.")
