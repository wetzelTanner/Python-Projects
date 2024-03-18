class Point:
    """ 
    A class to represent a point in a Cartesian coordinate system
    
    ...

    Attributes
    ----------
    x : float
        The x coordinate of a point
    y : float
        The y coordinate of a point

    Methods
    -------
    __str__():
        A helper method to print a Point object in customized format
    
    distance_x(p2):
        Measures the horizontal distance from the starting point to p2
    
    distance_y(p2):
        Measures the vertical distance from the starting point to p2

    distance(p2):
        Measures the Euclidean distance from the starting point to p2
    """

    def __init__(self, x = 0, y = 0):
        """ Create a new point at x, y. Defaults to 0, 0 """
        self.x = x
        self.y = y

    def __str__(self):
        """ Print a Point object in the format of (x, y) """
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def distance_x(self, p2):
        """
        Measures the horizontal distance from the 
        starting point self to Point p2
        """
        return abs(self.x - p2.x)

    def distance_y(self, p2):
        """
        Measures the vertical distance from the 
        starting point self to Point p2
        """
        return abs(self.y - p2.y)

    def distance(self, p2):
        """
        Measures the Euclidean distance from the 
        starting point self to Point p2
        """
        return ( self.distance_x(p2)**2 + \
            self.distance_y(p2)**2 ) ** 0.5

    def halfway(self, p2):
        """
        Takes two points and returns the midpoint
        """
        x1 = (self.x + p2.x) / 2
        y1 = (self.y + p2.y) / 2
        return '(' + str(x1) + ', ' + str(y1) + ')'