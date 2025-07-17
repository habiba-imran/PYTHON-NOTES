# seek() and tell() functions
f = open('myfile.txt', 'r')
f.seek(5) # move file pointer at 10th character
print(f.tell()) # shows the location of file pointer
print(f.read(6)) # start reading from 5th ch and read only 6 characters
 # truncate() # works in write mode only, or append
f2 = open('myfile2.txt', 'w')
f2.write("hope you are doing well")
f2.truncate(10)
# keeps the first 10 characters and deletes the rest


