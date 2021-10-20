#!/usr/bin/env python3

# Created by: Seti Ngabo
# Created on: Oct 2021
# This program rounds off to the nearest number
#   with user input


def round_off(answer, point):
    # This function is about rounding number

    # process
    first_sum = answer * 10 ** point + 0.5
    second_sum = int(first_sum)
    final_sum = second_sum / 10 ** point

    return final_sum


def main():
    # This function just call other functions

    # input
    user1_str = input("Enter the number to round off: ")
    user2_str = input("How many decimals do you want to round off: ")
    print("")

    try:
        user1_int = float(user1_str)
        user2_int = float(user2_str)

        # call functions
        rounded_off = round_off(answer=user1_int, point=user2_int)

        # output
        print("The rounded number is {}".format(rounded_off))

    except Exception:
        # output
        print("Invalid input, try again.")

    print("\nDone.")


if __name__ == "__main__":
    main()
