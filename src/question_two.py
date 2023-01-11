def switch_red_status_light():
    print("\nShut off all input lines.")
    meter_three_value = 0

    # Input validation
    meter_three_value_is_num = False
    meter_three_value_is_float = False
    while not meter_three_value_is_num and not meter_three_value_is_float:
        meter_three_value = input("\nWhat is the value displayed on 'Meter 3?' > ")

        # Check if user input is an integer value
        if not meter_three_value.isdigit():
            meter_three_value_is_num = False
        else:
            meter_three_value_is_num = True

        # Check if user input is a decimal value
        try:
            float(meter_three_value)
            meter_three_value_is_float = True
        except ValueError:
            print("Unknown value(s) detected, numeric values only")
            meter_three_value_is_float = False

    # Troubleshooting tree if value is < 50
    if float(meter_three_value) < 50.00:
        print("\nCheck main line for test pressure.")
        test_pressure_value = "0"
        while test_pressure_value != "1" and test_pressure_value != "2" and test_pressure_value != "3":
            test_pressure_value = input(
                "\nWhat is the test pressure value?"
                "\n1: Normal"
                "\n2: High"
                "\n3: Low"
                "\nEnter corresponding number > "
            )

        match test_pressure_value:
            case "1":
                print("\nRefer to motor service manual")
            case "2":
                print("\nRefer to main line manual")
            case "3":
                print("\nRefer to main line manual")

    # Troubleshooting tree if value is >= 50
    else:
        print("\nMeasure flow velocity at inlet 2-B.")
        flow_velocity = "0"
        while flow_velocity != "1" and flow_velocity != "2" and flow_velocity != "3":
            flow_velocity = input(
                "\nWhat is the flow velocity value at 'Inlet 2-B?'"
                "\n1: Normal"
                "\n2: High"
                "\n3: Low"
                "\nEnter corresponding number > "
            )

        match flow_velocity:
            case "1":
                print("\nRefer to inlet service manual")
            case "2":
                print("\nRefer unit for factory service")
            case "3":
                print("\nRefer unit for factory service")

def troubleshoot_diesel_engine():
    # Loop control value
    user_program_choice = "y"

    # Loop will start as "True" in order for the program to run on start
    while user_program_choice == "y":
        print(f"\n=================================\n"
              f"DIESEL ENGINE TROUBLESHOOTING GUIDE"
              f"\n=================================\n")

        # Attempt to get status light value
        status_light = "0"
        while status_light != "1" and status_light != "2" and status_light != "3":
            status_light = input(
                "What color is the status light?"
                "\n1: Green"
                "\n2: Red"
                "\n3: Amber"
                "\nEnter corresponding number > "
            )

        # Using status_light, switch to appropriate result
        match status_light:
            case "1":
                print("\nDo restart procedure")
            case "2":
                switch_red_status_light()
            case "3":
                print("\nCheck fuel line service routine")


        # Automatically set user input to lowercase to handle capital inputs
        user_program_choice = str.lower(input(
            "\n================================="
            "\nTo restart the guide, enter 'Y' > "
        ))