print("\nFILE READ WITH SIZE DEMO")
print("------------------\n")

#Opening file in read mode 
source_file = open("source.txt", "r")
print("File Opened for Readeing")

#Reading from File but only 3 charecters 
data = source_file.read(3)
print("File Read Completed")

print("\n.....DATA STARTS ......\n")
#Printing data
print(data)
print("\n.....DATA ENDS ......\n")

#Closing a file
source_file.close()
print("File Closed")