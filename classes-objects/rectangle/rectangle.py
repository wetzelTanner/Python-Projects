class Rectangle:
    """ 
    A class to manufacture rectangle objects
    
    ...

    Attributes
    ----------
    vertice_bl : Point type
        The bottom left vertex of the Rectangle object
    vertice_tr : Point type
        The top right vertex of the Rectangle object

    Methods
    -------
    __str__():
        A helper method to print a Rectangle object in
        the customized format
    
    area():
        Returns the area of the Rectangle object
    
    perimeter():
        Returns the perimeter of the Rectangle object

    is_origin_centered():
        Finds the center of the Rectangle object,
        and checks if the center is on origin (0, 0).
    """

    def __init__(self, point_bottom_left, point_top_right):
        """ Initialize rectangle """
        self.vertex_bl = point_bottom_left
        self.vertex_tr = point_top_right

    def __str__(self):
        """
        Print a Rectangle object in the format of 
            Bottom left: (x1, y1), top right: (x2, y2)
        """
        return 'Rectangle Location: Bottom Left: ' + str(self.vertex_bl) + ', ' + 'Top Right: ' + str(self.vertex_tr)


    def area(self):
        """ Returns the area of the Rectangle object """
        return ((abs(self.vertex_tr[0] - self.vertex_bl[0])) * abs(self.vertex_tr[1] - self.vertex_bl[1]))

    
    def perimeter(self):
        """ Returns the perimeter of the Rectangle object """
        return abs(self.vertex_bl[0] - self.vertex_tr[0]) * 2 + abs(self.vertex_bl[1] - self.vertex_tr[1]) * 2


    def is_origin_centered(self):
        """
        Finds the center of the Rectangle object,
        and checks if the center is on origin (0,0).
        If yes, returns True; if no, returns False
        """
        x = (self.vertex_bl[0] + self.vertex_tr[0]) / 2
        y = (self.vertex_bl[1] + self.vertex_tr[1]) / 2
        if x == 0 and y == 0:
            return True
        else:
            return False
    