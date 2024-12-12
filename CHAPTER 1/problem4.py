# Write a python program to print the contents of a directry using os module, Search online for the function which does that. 

import os

# Specify the directory path (you can modify this path)
directory_path = '/'  # Current directory (use an absolute path if needed)

try:
    # List all files and folders in the specified directory
    contents = os.listdir(directory_path)
    
    print(f"Contents of '{directory_path}' directory:")
    for item in contents:
        print(item)

except FileNotFoundError:
    print(f"Error: The directory '{directory_path}' was not found.")
except PermissionError:
    print(f"Error: You do not have permission to access '{directory_path}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
