print("\nFILE READ DEMO")
print("------------------\n")

# Opening file in read mode
source_file = open("source.txt", "r")
print("File Opened for Readeing")

# Reading from File
data = source_file.read()
print("File Read Completed")

print("\n.....DATA STARTS ......\n")
# Printing data
print(data)
print("\n.....DATA ENDS ......\n")

# Closing a file
source_file.close()
print("File Closed")
