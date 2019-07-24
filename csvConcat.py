# dependencies
import pandas as pd         # for data frames
import os                   # for paths
import datetime             # for dates
import sys                  # for getting os type

# get current path/directory and make a list of all files in path/directory and make path
cwd = os.getcwd()

# lists of possible OS to work on
windows = ["win32", "cygwin", "msys"]
linux = ["linux", "linux2 (*)"]
macOS = ["darwin"]
slash = ""

# prompt user for  name of the directory to work in
date = input('Enter the date of CSV(s) to alter (YYYY-MM-DD) \nor type "today" to work on today\'s CSV(s) \n\t')

# get the date and add to path
if date.lower() == "today":
    date = str(datetime.date.today())       
    
if sys.platform in windows:
    path = cwd + "\\" + date
    slash = "\\"
elif sys.platform in linux or sys.platform in macOS:
    path = cwd + "/" + date
    slash = "/"

# make a list of files in directory, if file not found kill program
try:
    files = os.listdir(path)
except FileNotFoundError:
    print("Sorry, couldn't find that folder. Try again.")
    input("Press any key to exit.")
    sys.exit()

# update user
print(f"working on files in {path}\n")

# go through every file in directory, make a df and add to a list of df
frames = []

for file in files:
    temp_frame = pd.read_csv(path + slash + file)
    frames.append(temp_frame)

# concatenate all frames into a master df
master = pd.concat(frames, axis=0, sort=False)

# write to a csv file
master.to_csv(path + slash + date + "-master.csv", index=False)

# update user
print("Concatenation completed")
