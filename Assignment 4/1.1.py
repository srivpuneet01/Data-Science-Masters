# define the Triangle class -- base class
class Triangle():

    # initialize the sides in the contructor
    def __init__(self, side1, side2, side3):
        self.side1 = float(side1)
        self.side2 = float(side2)
        self.side3 = float(side3)
    
    # define the get function for the semiperimeter property
    def _get_semiperimeter(self):
        return (self.side1 + self.side2 + self.side3)/2
    
    # allocate the get function to the semiperimeter property
    semiperimeter = property(_get_semiperimeter)

# define the Area_Calculator class -- the sub class for area calculation
class Area_Calculator(Triangle):
    def calculate_area(self):
            print("Area of the triangle is %s" %(self.semiperimeter*(self.semiperimeter - self.side1)*(self.semiperimeter - self.side2)*(self.semiperimeter - self.side3))**0.5)

area_calculator = Area_Calculator(20, 30, 40)
area_calculator.calculate_area()


