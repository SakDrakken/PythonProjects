file_object = open("C:/Users/Home/Desktop/input.txt", "r")
summary = 0
history = []
iterations = 0
first = 0

while first == 0:
    for lines in file_object.readlines():
        summary += int(lines)
        for x in history:
            if int(summary) == int(x):
                first = summary
                print first
        history.append(summary)
    iterations += 1
    print "Number of iterations: ", iterations
