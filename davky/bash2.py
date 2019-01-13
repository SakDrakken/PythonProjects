def batch2():
    f = open("input2.txt", "a+")
    content = f.readlines()

    for lines in content:
        a = lines.split(",")
        add = int(a[0]) + int(a[1])
        sub = int(a[0]) - int(a[1])
        mult = int(a[0]) * int(a[1])
        div = int(a[0]) / int(a[1])

        line = str("\nInput:" + lines + " Add: " + str(add) + " Subtract: " + str(sub) + " Multiply:" + str(mult)
                   + " Divide:" + str(div))
        f.write(line)


if __name__ == "__main__":
    batch2()
