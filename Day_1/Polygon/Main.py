import math

class Polygon:
    list_of_points = []

    def __init__(self):
        self.list_of_points = []

    def addPoint(self, x, y):
        list_of_points = self.list_of_points.append([x,y])
        return self.list_of_points
        pointx.append(self.list_of_points)


    def dist(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def perimeter(self):
        list_of_points = self.list_of_points
        self.perimeter = 0
        #while sides < len(list_of_points):
            #sides += 1
        i = 0
        while i < len(list_of_points) - 1:
                #i += 1
            #for i in range(len(self.list_of_points)):
            x1 = self.list_of_points [i][0]
            x2 = self.list_of_points [i + 1][0]
            y1 = self.list_of_points [i][1]
            y2 = self.list_of_points [i + 1][1]
            self.perimeter = self.perimeter + ((x2 - x1) ** 2 + (y2 - y1) ** 2)**(.5)
            i += 1
        x1 = self.list_of_points [0][0]
        x2 = self.list_of_points [-1][0]
        y1 = self.list_of_points [0][1]
        y2 = self.list_of_points [-1][1]
        self.perimeter = self.perimeter + ((x2 - x1) ** 2 + (y2 - y1) ** 2)**(.5)
                #total = total + (self.dist(self.list_of_points[0][0],
                #self.list_of_points[0][1], self.list_of_points[len(self.list_of_points)-1][0],
                #self.list_of_points[len(self.list_of_points)-1][1]))

        return self.perimeter

    def area(self):
        for i in range(len(self.list_of_points)):
            x1 = self.list_of_points [i],[0]
            x2 = self.list_of_points [i + 1],[0]
            y1 = self.list_of_points [i + 2],[1]
            y2 = self.list_of_points [i + 3],[1]
            self.area = self.area + dist(x1, y1, x2, y2)
        area = self.area
        return area

count = int(input("How many sides would you like?: "))
f = Polygon()
while count > 0:
    coordinate_x = eval(input("What x coordinates would you like?: "))
    coordinate_y = eval(input("What y coordinate would you like?: "))
    f.addPoint(coordinate_x, coordinate_y)
    print ("(" + str(coordinate_x) + "," +  str(coordinate_y) + ")")
    count -= 1
print (f.perimeter())
