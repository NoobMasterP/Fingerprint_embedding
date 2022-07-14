
with open("oroot.xyz") as inp:
    points = (list(zip(*(line.strip().split('\t') for line in inp))))

x = []
y = []
d = []
minutiae_type = []

for point in points[0]:
    
    # print(point)

    # x = point[(point.find("-> (") + 4):(point.find(","))]
    # y = point[(point.find(",") + 1):(point.find(")"))]
    # # print("(" + x + "," + y + ")")

    # d = point[point.find("Direction") + len("Diretion: ") + 1:point.find("\t")]
    # print(d)

    line = point.split()
    # print(str(line))

    x.append(int(line[2][1:line[2].find(",")]))
    y.append(int(line[2][line[2].find(",")+1:line[2].find(")")]))
    # print(y)

    d.append(int(line[4]))
    # print(d)

    minutiae = line[8]
    if (minutiae == "RIG"):
        minutiae_type.append(1)
    else: 
        minutiae_type.append(3)
    # print(minutiae_type)


# print(type(x[0]))

digitizedFormat = ""

for i in range(len(x)):

    digitizedFormat += bin(x[i]).replace("0b", "")
    digitizedFormat += bin(y[i]).replace("0b", "")
    digitizedFormat += bin(minutiae_type[i]).replace("0b", "")
    digitizedFormat += bin(d[i]).replace("0b", "")

print(digitizedFormat)

f = open("Digitized.sdc", "w")
f.write(digitizedFormat)
f.close()
