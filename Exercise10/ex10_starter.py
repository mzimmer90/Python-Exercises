import sys
import glob
import os

# Get the directory name
if sys.platform == 'win32':
    #added extra path info as my home directory is c:/users/admin
    hdir = os.environ['HOMEPATH'] = 'C:/Users/Admin/Documents/QA evening learning/Chris Beagles/maxexercise10/exercise10/'
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir, '*')


# TODO: Use the glob.glob() function to obtain the list of filenames
print(glob.glob(hdir))

files = glob.glob(pattern)

print("\n", "******files within this folder****")
#use \n for new line and .join to present each element in list on new line
print("\n" .join(files))

# TODO: use os.path.getsize to find each file's size
# TODO: Add a test to only display files that do not have a size of zero
print("")
print("\n", "******size of each file****")
#glob.glob returns a list. getsize expects individual files. iterating over that list gives each individual filea and size.
for filename in glob.glob(pattern):
#add test to detect if a file size is 0. if it is. ignore it
    if os.path.getsize(filename) != 0:
        print(os.path.getsize(filename))

# TODO: Remove the leading directory name(s) from each filename before you print it -
# using os.path.basename()
print("\n", "******each file without it's path****")
#glob.glob returns a list. os.path.basenameindividual files. iterating over that list gives each individual file without the path
for filename in glob.glob(pattern):
    print(os.path.basename(filename))
#print(glob.glob(hdir))

#files = glob.glob(pattern)

#print("******files within this folder****")
#print(files)