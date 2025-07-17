f = open('myfile.txt', 'r') # takes 2 arguments, file name and mode
# mode: r for reading, w for writing, a for appending (adding content at end of file)
# by default, mode is r
text = f.read()
f.close()
print(f)
print(text)
# In writing mode, if a file doesnot exist, it'll be created automatically
f2 = open('myfile2.txt', 'w')
f2.write("hi, habiba")
f2 = open('myfile2.txt', 'a') # append mode
f2.write(" how are you") # gets written after hi habiba
f2.close()

# modes: rt, reading a text file, by default
# rb: to read in form of binary

# to prevent the hustle we can also do this:
with open('myfile3.txt', 'w') as f3:
    f3.write("habiba, you look so happy")
# here we don't need to close the file