import cv2

# 以下两个值越小线越多
levelthreshold = 6
verticalthreshold = 10

# 这个值越小 线越多
error = 7

# 此文件试图给图片补上线
def judge(list, num):
    for item in list:
        if abs(num - item) <= error:
            return False
    return True


# 获取图片的横线
def getlevelline(img, row, col):
    lines = []
    for i in range(row):
        blackcount = 0
        for j in range(col):
            px = img[i, j]
            if px == 0:
                blackcount += 1
        if blackcount > int(9 * col / 10):
            lines.append(i)
    print("一共找到如下横线" + str(lines))
    return lines


def getverticalline(img, row, col):
    lines = []
    for i in range(col):
        count = 0
        for j in range(row):
            px = img[j, i]
            if px == 0:
                count += 1
        if count > int(9 * row / 10):
            lines.append(i)
    print("一共找到如下竖线" + str(lines))
    return lines


def getxbegin(img, col, lines):
    for i in range(col):
        if img[lines[0], i] == 0:
            xBegin = i
            break
    return xBegin


def getxend(img, col, lines):
    for i in range(col - 1, 0, -1):
        if img[lines[0], i] == 0:
            xEnd = i
            break
    return xEnd


'''返回列号
    Args:
        linesNum: 备选路径上黑点的最大个数
    '''


def getcandidatevertical(img, col, row,linesNum):
    myList = []
    for i in range(col):
        count = 0
        for j in range(row):
            px = img[j, i]
            if px == 0:
                count += 1
        if count <= linesNum:
            myList.append(i)
    return myList


def getcandidatelevel(img, row, col, linesNum=2):
    myList = []
    for i in range(row):
        count = 0
        for j in range(col):
            px = img[i, j]
            if px == 0:
                count += 1
        if count <= linesNum + 1:
            myList.append(i)
    return myList


def getdrawlevel(myList):
    newList = []
    i = 0
    while i < len(myList):
        temp = []
        for j in range(myList[i], myList[-1]):
            if j in myList:
                temp.append(j)
                i += 1
            else:
                i -= 1
                break
        i += 1
        newList.append(temp)
    print(newList)
    return newList


def draw(newlist, xbegin, xend, lines, img, myList):
    newlist.remove(newlist[0])
    newlist.remove(newlist[-1])
    cv2.line(img, (xbegin, lines[0]), (xbegin, lines[-1]), (0, 0, 0), 1)
    cv2.line(img, (xend, lines[0]), (xend, lines[-1]), (0, 0, 0), 1)

    for i in newlist:
        if len(i) > verticalthreshold:
            num = int((i[0] + i[-1]) / 2)
            if not judge(myList, num):
                continue
            cv2.line(img, (num, lines[0]), (num, lines[-1]), (0, 0, 0), 1)


def draw2(newlist, xbegin, xend, lines):
    for i in newlist:
        if len(i) > levelthreshold:
            num = int((i[0] + i[-1]) / 2)
            if not judge(lines, num):
                continue
            cv2.line(img, (xbegin, num), (xend, num), (0, 0, 0), 1)


def show(img):
    cv2.imshow('image', img)
    # cv2.imwrite("hhhh.png", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 0 黑色  255 白色
img = cv2.imread('2.png', 0)
ret, img = cv2.threshold(img, 180, 255, cv2.THRESH_BINARY)
shape = img.shape
print(shape)
row = shape[0]
col = shape[1]
count = 0

# 找横着的线
lines = getlevelline(img, row, col)
xbegin = getxbegin(img, col, lines)
xend = getxend(img, col, lines)
myList = getcandidatevertical(img, col, row, len(lines))

temp = getverticalline(img, row, col)

newList = getdrawlevel(myList)
draw(newList, xbegin, xend, lines, img, temp)


verticallines = getverticalline(img, row, col)
myList = getcandidatelevel(img, row, col, len(verticallines))

newList = getdrawlevel(myList)
draw2(newList, xbegin, xend, lines)

show(img)

cv2.imwrite("../pdfreader/22.png", img)