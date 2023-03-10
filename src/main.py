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

For this question, I have opted for more of a "menu" style approach rather than utilizing purely user-input to further
simplify the validation process.


Author: Josh Reginaldo
GitHub: https://github.com/itmd-413-jreginaldo/Simple-IO-and-Control-Structures
"""

import question_one
import question_two

def main():
    question_one.find_polygon_area()
    question_two.troubleshoot_diesel_engine()

if __name__ == '__main__':
    main()