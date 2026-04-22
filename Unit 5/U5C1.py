# Take filename from user
filename = input("Enter the filename: ")

try:
    file = open(filename, "r")   # Try to open file in read mode
    content = file.read()
    print("File opened successfully.\n")
    print("File Content:\n", content)
    file.close()

except FileNotFoundError:
    print("Error: The file does not exist.")

except PermissionError:
    print("Error: You do not have permission to read this file.")
