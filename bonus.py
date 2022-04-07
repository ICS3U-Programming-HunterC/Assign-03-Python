#!/usr/bin/env python3
# Created by: Hunter Connolly
# Created on: March 31, 2022
# This program asks the user or how many years they have worked
# and if they have worked more than 5 years, they get a 5% bonus


import random
import math


def main():
    # get the number from the user
    years_worked_string = (input("How many years have you been working for?: "))
    print("")

    # check if number is positive negative or zero
    try:
        years_worked_number = float(years_worked_string)
        if years_worked_number >= 5:
            print("CONGRATULATIONS! You are eligible for a bonus this year!!")
            salary = float(input("Enter your salary: "))
            print("")
            bonus = salary * 0.05
            print("Your bonus this year is: ${:.2f}" .format(bonus))
            net_bonus = salary + bonus
            print("Your total salary with the bonus this year is: ${:.2f}"
            .format(net_bonus))
        elif years_worked_number == 4:
            print("Unfortunately you are not eligible for a bonus this year. Next year you will be eligible!")
        elif years_worked_number == 3:
            print("Unfortunately you are not eligible for a bonus this year. In two years you will be eligible")
        elif years_worked_number == 2:
            print("Unfortunately you are not eligible for a bonus this year. In three years you will be eligible")
        else:
            print("Unfortunately you are not eligible for a bonus this year")
    except Exception:
        print("That is not a number")


if __name__ == "__main__":
    main()