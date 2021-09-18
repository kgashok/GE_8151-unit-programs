print("\nFILE READ TELL")
print("------------------\n")

# Opening file in read mode
source_file = open("source.txt", "r")
print("File Opened for Readeing")

print("File pointer current position:", source_file.tell())
# Seek position 5 [moves file pointer current_poisition + offset]

sno = source_file.read(3)
print("File pointer current position:", source_file.tell())
name = source_file.read(20)
print("File pointer current position:", source_file.tell())
mobileno = source_file.read(10)
print("File pointer current position:", source_file.tell())

print("sno:", sno.strip())
print("name:", name.strip())
print("mobileno:", mobileno.strip())


# Closing a file
source_file.close()
print("File Closed")
