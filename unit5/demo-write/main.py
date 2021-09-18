print("\nFILE WRITE DEMO")
print("-----------------")
dataToWrite = "Python is Good"

# Opening file in write mode
destination_file = open("destination.txt", "w")
print("File Opened for Writting")

#Writing in File
destination_file.write(dataToWrite)
print("Write Completed")

# Data written
print("Data Written:", dataToWrite)

# Closing File
destination_file.close()
print("File Closed")
