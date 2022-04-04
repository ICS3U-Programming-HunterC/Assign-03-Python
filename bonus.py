#!/usr/bin/env python3
# Created by: Hunter Connolly
# Created on: March 31, 2022
# This program determines if a number is positive
# negative or zero


import random
import math


def main():
    # get the number from the user
    years_worked = float(input("How many years have you been working for?: "))

    # check if number is positive negative or zero
    if years_worked >= 5:
        print("CONGRATULATIONS! You are eligible for a bonus this year")
    elif years_worked == 4:
        print("Unfortunately you are not eligible for a bonus this year. Next year you will be eligible!")
    elif years_worked == 3:
        print("Unfortunately you are not eligible for a bonus this year. In two years you will be eligible")
    elif years_worked == 2:
        print("Unfortunately you are not eligible for a bonus this year. In three years you will be eligible")
    elif years_worked < 5:
        print("Unfortunately you are not eligible for a bonus this year")
    else: 
        print("No idea!")


if __name__ == "__main__":
    main()