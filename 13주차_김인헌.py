class Box :
    def __init__(self,width,length,height):
        self.width = width
        self.length = length
        self.height = height

    def setWidth(self,W):
        self.width = width    

    def setLength(self,L):
        self.length = length

    def setHeight(self,H):
        self.height = height

    def getVokume(self):
         return self.width * self.length * self.height
        
    def __str__ (self):
        return ("가로 = %d, 세로 = %d, 높이 = %d,"
                %(self.width, self.length, self.height))
      
box1=Box(10,10,10)
box2=Box(4,5,6)

print(box1)
print("box의 부피 =", box1.getVokume())
print(box2)
print("box의 부피 =", box2.getVokume())
