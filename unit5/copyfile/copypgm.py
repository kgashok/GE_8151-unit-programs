source = open("source.txt","r")
dest = open("dest.txt","w")

sourcedata = source.read();
print("source data readed...")
dest.write(sourcedata);
print("source data writed in destination...")

source.close()
dest.close()

# Get the source and destination path from user

# Exception handling
 #1.File Not Available
 #2.Problem with READ/WRITE Access
 #3.Usage of os module