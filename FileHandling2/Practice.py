# readline method
f = open('myfile.txt', 'r')
while True:
    line = f.readline() # prints all lines from myfile.txt wihh a break line in bw
    # break line is added coz readlne() prints /n after every line
    if not line:
        break
    print(line)

# to print data while separating commas
f2 = open('myfile3.txt', 'r')
i = 1
while True:
    line = f2.readline()
    if not line:
        break
    m1 = int(line.split(',')[0])
    m2 = int(line.split(',')[1])
    m3 = int(line.split(',')[2]) # split splits the line whereever it sees a comma and forms a list
    print(f"Marks of student {i} in maths are: {m1}")
    print(f"Marks of student {i} in english are: {m2}")
    print(f"Marks of student {i} in urdu are: {m3}")
    i += 1

# writeline() method # writes a sequence of lines into a string
# we us eit in form of a list a follows:
f3 = open("myfile2.txt", 'w')
lines = ['hello ', 'habiba\n', 'how are you?']
f3.writelines(lines)
f3.close()


