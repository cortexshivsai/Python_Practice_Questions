# Use sys

# Import the sys module
import sys

# Display the Python version
print("Python version:", sys.version)

# Display the Python installation location
print("Python executable:", sys.executable)

# Display the platform name
print("Platform:", sys.platform)

# Display the command-line arguments
print("Command-line arguments:", sys.argv)

# Display the module search paths
print("Module search paths:", sys.path)



"""
Example output (details vary by computer and how the program is run):

Python version: 3.14...
Python executable: C:\...\python.exe
Platform: win32
Command-line arguments: ['main.py']
Module search paths: [...]
"""


"""
Important attributes:

Attribute                         Purpose

sys.version                 Python version information

sys.executable              Path to the Python executable

sys.platform                Identifies the operating system platform

sys.argv                    Command-line arguments

sys.path                    Locations Python searches for modules
"""