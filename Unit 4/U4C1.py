# Write data to a file
file = open("sample.txt", "w")   # Open file in write mode
file.write("Hello, this is the first line.\n")
file.write("This file is created using Python.\n")
file.close()   # Close the file

# Read data from the file
file = open("sample.txt", "r")   # Open file in read mode
content = file.read()
print("File Content after writing:")
print(content)
file.close()

# Append more data to the file
file = open("sample.txt", "a")   # Open file in append mode
file.write("This line is added later.\n")
file.close()

# Read updated content
file = open("sample.txt", "r")
updated_content = file.read()
print("File Content after appending:")
print(updated_content)
file.close()
