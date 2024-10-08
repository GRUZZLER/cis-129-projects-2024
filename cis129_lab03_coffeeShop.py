# Christian Griessel
# Coffee and Muffin program for CIS 129
# Calculates the price of various items and accounts for sales tax

TAX_RATE = 0.06
TOTAL_VALUE_PLUS_TAX_RATE = 1 + TAX_RATE
COFFEE_COST = 5
MUFFIN_COST = 4
HUMAN_FINGERS_COST = 3
URANIUM_COST = 69.19


def main():
    coffee_muffin_values = coffee_muffin_counter()
    printer(coffee_muffin_values[0], coffee_muffin_values[1], coffee_muffin_values[2], coffee_muffin_values[3])


def coffee_muffin_counter():
    """This function grabs the number of coffees and muffins while making sure that the numbers are ints and are
    realistic"""
    while True:
        # Prompt for muffins, sets value to None so if a string is typed it won't reset the loop back to muffins once
        # muffins has a value
        number_of_muffins = None
        while number_of_muffins is None:
            try:
                number_of_muffins = int(
                    input("HOW MANY MUFFINS IN THIS PURCHASE?: "))  # Forces int and forces a realistic number
                if number_of_muffins < 0 or number_of_muffins > 50:
                    print("UNREALISTIC MUFFIN COUNT ENTER A NUMBER BETWEEN 0 AND 50 OR PREPARE TO BE DESTROYED")
                    number_of_muffins = None  # Reset for valid input before the loop starts again
            except ValueError:
                print("THIS IS NOT A NUMBER, PREPARE TO BE DISSOLVED")

        # Prompt for coffees only once we have a confirmed int locked in for muffins
        while True:
            try:
                number_of_coffees = int(
                    input("HOW MANY COFFEES IN THIS PURCHASE?: "))  # Forces int and forces a realistic number
                if number_of_coffees < 0 or number_of_coffees > 50:
                    print("UNREALISTIC COFFEE COUNT ENTER A NUMBER BETWEEN 0 AND 50 OR PREPARE TO BE DESTROYED")
                else:
                    break
            except ValueError:
                print("THIS IS NOT A NUMBER, PREPARE TO BE DISSOLVED")

        while True:
            try:
                number_of_human_fingers = int(
                    input("HOW MANY HUMAN FINGERS IN THIS PURCHASE?: "))  # Forces int and forces a realistic number
                if number_of_human_fingers < 0 or number_of_human_fingers > 50:
                    print("UNREALISTIC HUMAN FINGER COUNT ENTER A NUMBER BETWEEN 0 AND 50 OR PREPARE TO BE DESTROYED")
                else:
                    break
            except ValueError:
                print("THIS IS NOT A NUMBER, PREPARE TO BE DISSOLVED")

        while True:
            try:
                number_of_uranium = int(
                    input("HOW MANY POUNDS OF URANIUM IN THIS PURCHASE?: "))  # Forces int and forces a realistic number
                if number_of_uranium < 0 or number_of_uranium > 50:
                    print(
                        "UNREALISTIC POUNDS OF URANIUM COUNT ENTER A NUMBER BETWEEN 0 AND 50 OR PREPARE TO BE DESTROYED")
                else:
                    break
            except ValueError:
                print("THIS IS NOT A NUMBER, PREPARE TO BE DISSOLVED")

        # Return two valid values
        return number_of_muffins, number_of_coffees, number_of_human_fingers, number_of_uranium


def printer(coffee, muffins, human_fingers, uranium):
    """Prints out a mock receipt."""
    print("***************************************\n"
          "My Coffee and Muffin Shop\n"
          "Number of muffins bought?\n"
          f"{muffins}\n"
          "Number of coffees bought?\n"
          f"{coffee}\n"
          "Number of HUMAN FINGERS bought?\n"
          f"{human_fingers}\n"
          "Number of pounds of uranium bought?\n"
          f"{uranium} pounds\n"
          "***************************************\n\n"
          "***************************************\n"
          "My Coffee and Muffin Shop Receipt\n"
          f"{coffee} Coffee at $5 each: $ {float(coffee) * COFFEE_COST:.2f}\n"
          f"{muffins} Muffins at $4 each: $ {float(muffins) * MUFFIN_COST:.2f}\n"
          f"{human_fingers} HUMAN FINGERS at $3 each: $ {float(human_fingers) * HUMAN_FINGERS_COST:.2f}\n"
          f"{uranium} pounds of uranium at $69.19 each: $ {float(uranium) * URANIUM_COST:.2f}\n"
          f"6% tax: $ {((float(coffee) * COFFEE_COST + float(muffins) * MUFFIN_COST +
                         float(human_fingers) * HUMAN_FINGERS_COST + float(uranium) * URANIUM_COST) * TAX_RATE):.2f}\n"
          f"---------\n"
          f"Total: $ {((float(coffee) * COFFEE_COST + float(muffins) * MUFFIN_COST +
                        float(human_fingers) * HUMAN_FINGERS_COST +
                        float(uranium) * URANIUM_COST) * TOTAL_VALUE_PLUS_TAX_RATE):.2f}\n"
          "***************************************\n\n"
          "Thank you for your business please don't mention the fingers see you next time")


if __name__ == '__main__':
    main()
