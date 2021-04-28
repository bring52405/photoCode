#! /usr/bin/python5

import os
import calendar

def y_dir():
    """ Create a list with the number of years which will be basis for 
    Directories"""
    path = '/media/bring/extStor'
    years = list(range(1990, 2022))
    months = [m for m in calendar.month_name if m]
    for y in years:
        for m in months:
            if os.path.exists(os.path.join(path, str(y), m)):
                continue
            else:
                os.makedirs(os.path.join(path, str(y), m))

def main():
    y_dir() 

if __name__ == "__main__":
    main()
