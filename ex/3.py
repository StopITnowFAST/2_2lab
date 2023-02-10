try:
    fileptr = open("file.txt")
    # perform file operations
finally:
    fileptr.close()
