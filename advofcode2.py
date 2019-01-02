file_object = open("C:/Users/Home/Desktop/input2.txt", "r")
history2 = []
history3 = []
ascii_lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
                   "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def checkalphabet(line):
    counter2 = 0
    counter3 = 0
    for x in ascii_lowercase:
        if line.count(x) == 2:
            counter2 += 1
        if line.count(x) == 3:
            counter3 += 1
    if 0 < counter2 < 2:
        history2.append(line)
    if 0 < counter3 < 2:
        history3.append(line)


for lines in file_object.readlines():
    checkalphabet(lines)
print str(history2.__len__()) + " " + str(history3.__len__())
print history2.__len__() * history3.__len__()

