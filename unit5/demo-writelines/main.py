print("\nFILE WRITELINES DEMO")
print("----------------------")
dataToWrite = ["Python is Good", "Easy to Install", "Anybody can learn"]

#Opening file in write mode 
destination_file = open("destination.txt", "w")
print("File Opened for Writting")

#Writing in File
destination_file.writelines(dataToWrite)
print("Write Completed")

#Data written
print("Data Written:",dataToWrite)

#Closing File
destination_file.close()
print("File Closed")