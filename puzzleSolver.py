import sys
import Piece
import math

def CheckSolutionString(pieces, solutionSring, size):
    solution = solutionSring.replace(" ","").split(";")
    for val in solution:
        tmp = val.split(",")
        index = int(tmp[0])
        rotateNum = int(tmp[1])
        pieces[index].RotateCount(rotateNum)

    for idx, val in enumerate(solution):
        tmp = val.split(",")
        index = int(tmp[0])
        curP = pieces[index]

        if idx < (len(solution) - 1):
            if not (idx % size) == (size - 1):
                nextVal = solution[idx + 1]
                nextTmp = nextVal.split(",")
                nextIndex = int(nextTmp[0])
                nextP = pieces[nextIndex]
                if curP.right != nextP.left:
                    print(curP)
                    print(nextP)
                    print("right")
                    return False
            if idx < size*(size - 1):
                nextVal = solution[idx + size]
                nextTmp = nextVal.split(",")
                nextIndex = int(nextTmp[0])
                nextP = pieces[nextIndex]
                if curP.bottom != nextP.top:
                    print(curP)
                    print(nextP)
                    print("bottom")
                    return False
    return True

def ParseData(file):
    piecesList = []
    file = open(file,"r")
    data = file.read()
    data = data.replace(" ","")
    cubes = data.split(";")
    for cube in cubes:
        id = cube.split(",[")[0]
        slices = cube[cube.find("[")+1:cube.find("]")]
        [top,right,bottom,left] = slices.split(",")
        p = Piece.Piece(top,right,bottom,left,id)
        piecesList.append(p)
    return piecesList

def GetTopLeftCorner():
    for p in pieces:
        if p.IsCorner() == True:
            while not (p.left == "0" and p.top == "0"):
                p.Rotate()
            return p

def NextMatch():
    for p in pieces:
        if p.inUse == False:
            if p.IsContain(solution[-1].right) == True:
                while p.left != solution[-1].right:
                    p.Rotate()
                solution.append(p)
                if (len(solution) == puzzleSize):
                    return True
                return NextMatch()


def FindSolution():
    p = GetTopLeftCorner()
    p.inUse = True
    solution.append(p)
    NextMatch()


"""
main
"""
solution = []
pieces = ParseData(sys.argv[1])
puzzleSize = len(pieces)
rowSize = int(math.sqrt(puzzleSize))
"""
p1 = Piece.Piece("1","2","3","4","5")
p2 = Piece.Piece("1","2","3","4","6")
al=[]
al.append(p1)
al.append(p2)
for a in al:
    print(a)
p1.top = "14"
for a in al:
    print(a)
"""
solutionSring = FindSolution()
#solutionSring = "2,2; 1,0; 6,0; 4,2; 3,0; 0,1; 8,2; 7,2; 5,3"
#res = CheckSolutionString(pieces, solutionSring, size = 3)
#print(res)