print("\nFILE READ LINES")
print("------------------\n")

#Opening file in read mode 
source_file = open("source.txt", "r")
print("File Opened for Readeing")

#Reading from File [readlines - reads all the lines in files and returns list of strings]
data = source_file.readlines()
print("File Read Completed")
print("Type of Data:",type(data))

print("\n.....DATA STARTS ......\n")
#Printing data
print(data)
print("\n.....DATA ENDS ......\n")

#Closing a file
source_file.close()
print("File Closed")