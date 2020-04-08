with open("overall.csv") as f:
    for line in map(lambda x: x.strip().split(","), f.readlines()):
        print (line[0], float(line[1])/float(line[2]))