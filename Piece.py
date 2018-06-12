class Piece:
    def __init__(self,top,right,bottom,left,id):
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left
        self.id = id
        self.inUse = False

    def RotateCount(self, count):
        for i in range(count):
            self.Rotate()

    def Rotate(self):
        tmp = self.top
        self.top = self.left
        self.left = self.bottom
        self.bottom = self.right
        self.right = tmp

    def IsContain(self, num):
        if self.top == num:
            return True
        elif self.right == num:
            return True
        elif self.bottom == num:
            return True
        elif self.left == num:
            return True
        return False

    def IsCorner(self):
        if (self.top == "0" and self.right == "0") or \
            (self.right == "0" and self.bottom == "0") or \
            (self.bottom == "0" and self.left == "0") or \
            (self.left == "0" and self.top == "0"):
            return True
        return False

    def __str__(self):
        return self.id + ":" + " top:" + self.top + " right:" + self.right + " bottom:" + self.bottom + " left:" + self.left