print("\nFILE READ TELL")
print("------------------\n")

#Opening file in read mode 
source_file = open("source.txt", "r")
print("File Opened for Readeing")

print("File pointer current position:",source_file.tell())
#Reading from File
data = source_file.read()
print("File Read Completed")
print("File pointer current position:",source_file.tell())
print("\n.....DATA STARTS ......\n")
#Printing data
print(data)
print("\n.....DATA ENDS ......\n")

#Closing a file
source_file.close()
print("File Closed")