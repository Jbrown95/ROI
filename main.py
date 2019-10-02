#!/usr/local/bin/python3

#imports dictionaries
from dict import *
#imports get_info
from get_info import *
#imports calculations
from calculations import *
#main runs the scripts in order needed
def main():
    get_info(information,dividendValues)
    calculations(information,dividendValues)


if __name__ == "__main__":
    main()
