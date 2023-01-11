import math

def find_polygon_area():
    # Get user input and convert string input to appropriate data type
    polygon_sides = int(input("Enter the number of sides: "))
    polygon_side_length = float(input("Enter the length of a side: "))

    """
    Polygon Area Formula:

    Area = (polygon_sides * polygon_side_length^2) / (4 * tan(pi / polygon_sides))
    """
    polygon_area = (polygon_sides * math.pow(polygon_side_length, 2)) / (4 * (math.tan((math.pi / polygon_sides))))

    print(f"The area of the polygon is: {polygon_area:.4f}")