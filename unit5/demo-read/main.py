print("\nFILE APPEND DEMO")
print("------------------")

#Opening file in read mode 
source_file = open("source.txt", "r")
print("File Opened for Readeing")

#Reading from File
data = source_file.read()
print("File Read Completed")

#Printing data
print(data)

#Closing a file
source_file.close()
print("File Closed")