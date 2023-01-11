"""
Simple IO and Control Structures

This program will explore the control flow concepts in Python through the questions provided in the homework assignment.

Question 1:
Using the formula for the area of a regular polygon, the program will take the length and sides of a polygon inputted by
the user. Using the input data, correctly output the total area to 4 decimal points.

Question 2:
Using the chart provided in the homework assignment, accurately create a program to replicate the
"Troubleshooting Chart for Diesel Engines."

The program will be able to restart continually until the user chooses to exit.


Author: Josh Reginaldo
GitHub: https://github.com/itmd-413-jreginaldo/Simple-IO-and-Control-Structures
"""

import math

def question_one():
    # Get user input and convert string input to appropriate data type
    polygon_sides = int(input("Enter the number of sides: "))
    polygon_side_length = float(input("Enter the length of a side: "))

    """
    Polygon Area Formula:
    
    Area = (polygon_sides * polygon_side_length^2) / (4 * tan(pi / polygon_sides))
    """
    polygon_area = (polygon_sides * math.pow(polygon_side_length, 2)) / (4 * (math.tan((math.pi / polygon_sides))))

    print(f"The area of the polygon is: {polygon_area:.4f}")


def question_two():
    # Loop control value
    user_program_choice = "Y"

    # Loop will start as "True" in order for the program to run on start
    while user_program_choice == "Y":
        print(f"\n=================================\n"
              f"DIESEL ENGINE TROUBLESHOOTING GUIDE"
              f"\n=================================\n")

        


        user_program_choice = input("Would you like to restart the guide? (Y/N)> ")

def main():
    # question_one()
    question_two()


if __name__ == '__main__':
    main()