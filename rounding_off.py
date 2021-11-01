#!/usr/bin/env python3

# Created by: Seti Ngabo
# Created on: Oct 2021
# This program rounds off to the nearest number
#   with user input


def round_off(final_sum, decimal_points):
    # This function rounds off the number
    first_sum = final_sum[0] * 10 ** decimal_points
    first_sum = int(first_sum + 0.5)
    first_sum = first_sum / (10 ** decimal_points)

    final_sum[0] = first_sum


def main():
    # This function accepts input
    final_sum = []

    try:
        # input
        user_input = input("Enter the number to round off: ")
        user_input = float(user_input)
        decimal_points = input("How many decimal places do you want to round off: ")
        decimal_points = int(decimal_points)

        final_sum.append(user_input)

        round_off(final_sum, decimal_points)

        # output
        print("The rounded number is {}".format(final_sum[0]))

    except (Exception):
        print("\nInvalid input, try again.")

    print("\nDone.")


if __name__ == "__main__":
    main()
