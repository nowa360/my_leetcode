
def doSth(file):
    f = open(file, "r+")

    print(f.readline())
    print(f.readline())
    print(f.readline())
    f.close()


def readAll(file):
    f = open(file, "r+")
    for line in f:
        print(line)

    f.close()


def readAll2(file):
    with open(file) as f:
        for line in f:
            for word in line.split(" "):
                print(word)
            #print(line)


#doSth("texty.txt")
readAll2("texty.txt")



#parse with regex?

