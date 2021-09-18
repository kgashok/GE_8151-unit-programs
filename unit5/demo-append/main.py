print("\nFILE APPEND DEMO")
print("------------------")
dataToAppend = "Easy to Install"

# Opening file in write mode
destination_file = open("destination.txt", "a")
print("File Opened for Appending")

#Writing in File
destination_file.write(dataToAppend)
print("Append Completed")

# Data written
print("Data Appended:", dataToAppend)


# Closing File
destination_file.close()
print("File Closed")


# Points To Think
# 1. Can you read file after appending ?
# try destination_file.read() after line 12
