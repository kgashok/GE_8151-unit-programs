source_file = open("source.txt", "r")
destination_file = open("destination.txt", "w")

sourcedata = source_file.read()
print("source data readed...")
destination_file.write(sourcedata)
print("source data writed in destination...")

source_file.close()
destination_file.close()

# Get the source and destination path from user

# Exception handling
# 1.File Not Available
# 2.Problem with READ/WRITE Access
# 3.Usage of os module
