# use OS

# Import the os module
import os

# Display the current working directory
print("Current directory:", os.getcwd())

# Display the files and folders in the current directory
print("Files and folders:", os.listdir())

# Create a new folder if it does not already exist
folder_name = "Python_Practice"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("Folder created successfully")
else:
    print("Folder already exists")

# Check whether a particular file exists
file_name = "data.txt"

if os.path.exists(file_name):
    print("data.txt exists")
else:
    print("data.txt does not exist")




"""
os.getcwd() → gets the current working directory.

os.listdir() → lists files and folders.

os.mkdir() → creates a folder.

os.path.exists() → checks whether a file or folder exists.

The folder is created in the current working directory. Running this program again will not create the same folder a second time.
"""    