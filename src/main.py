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

For this question, I have opted for more of a "menu" style approach rather than purely user-input to further simplify
the process.


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
    user_program_choice = "y"

    # Loop will start as "True" in order for the program to run on start
    while user_program_choice == "y":
        print(f"\n=================================\n"
              f"DIESEL ENGINE TROUBLESHOOTING GUIDE"
              f"\n=================================\n")

        # Attempt to get status light value
        status_light = 0
        while status_light != 1 and status_light != 2 and status_light != 3:
            status_light = int(input(
                "What color is the status light?"
                "\n1: Green"
                "\n2: Red"
                "\n3: Amber"
                "\nEnter corresponding number > "
            ))

        # Red light status troubleshooting tree
        def switch_red_status_light():
            print("\nShut off all input lines.")
            meter_three_value = input("\nWhat is the value displayed on 'Meter 3?' > ")

            # Check if user input is NOT an integer value
            # Will NOT work for decimal values
            while not meter_three_value.isdigit():
                print("\nUnknown value(s) detected, numeric values only.")
                meter_three_value = input("\nWhat is the value displayed on 'Meter 3?' > ")

            # Cast meter_three_value to int before conditional statements
            int(meter_three_value)

            # Troubleshooting tree if value is < 50
            if meter_three_value < 50:
                print("\nCheck main line for test pressure.")
                test_pressure_value = 0
                while test_pressure_value != 1 and test_pressure_value != 2:
                    test_pressure_value = int(input(
                        "\nWhat is the test pressure value?"
                        "\n1: Normal"
                        "\n2: High"
                        "\n3: Low"
                        "\nEnter corresponding number > "
                    ))

                match test_pressure_value:
                    case 1:
                        print("\nRefer to motor service manual")
                    case 2:
                        print("\nRefer to main line manual")
                    case 3:
                        print("\nRefer to main line manual")

            # Troubleshooting tree if value is >= 50
            else:
                print("\nMeasure flow velocity at inlet 2-B.")
                flow_velocity = 0
                while flow_velocity != 1 and flow_velocity != 2:
                    flow_velocity = int(input(
                        "\nWhat is the flow velocity value at 'Inlet 2-B?'"
                        "\n1: Normal"
                        "\n2: High"
                        "\n3: Low"
                        "\nEnter corresponding number > "
                    ))

                match flow_velocity:
                    case 1:
                        print("\nRefer to inlet service manual")
                    case 2:
                        print("\nRefer unit for factory service")
                    case 3:
                        print("\nRefer unit for factory service")

        # Using status_light, switch to appropriate result
        match status_light:
            case 1:
                print("\nDo restart procedure")
            case 2:
                switch_red_status_light()
            case 3:
                print("\nCheck fuel line service routine")


        # Automatically set user input to lowercase to handle capital inputs
        user_program_choice = str.lower(input(
            "\n================================"
            "\nTo restart the guide, enter 'Y': "
            "\n================================"
        ))


def main():
    # question_one()
    question_two()


if __name__ == '__main__':
    main()