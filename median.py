"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
import math

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        sortedList = numbers.sort()
        listLength = len(numbers)
        index = math.floor(listLength/2)

        if(listLength%2>0):
            print(numbers[index])
        else:
            print((numbers[index-1] + numbers[index])/2)

    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
