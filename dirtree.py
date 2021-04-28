#! /usr/bin/python5

import os
import calendar

def y_dir():
    """ Create a list with the number of years which will be basis for 
    Directories"""
    path = '/media/bring/extStor'
    years = list(range(1990, 2022))
    for y in years:
        if not os.path.exists(os.path.join(path, str(y))):
            os.mkdir(str(y))

def m_dir():
    """create months dirs in each year dir"""
    path = '/media/bring/extStor'
    months = [m for m in calendar.month_name if m]
    exclude = path
    for root, dirs, files in os.walk(path, topdown=True):
#       dirs[:] = [d for d in dirs if d not in exclude]
        for dir in dirs:
#           print(os.path.join(root, dir))
            for m in months:
                if os.path.exists(os.path.join(root, m)):
                    continue
                elif os.path.exists(os.path.join(root, dir, m)):
                    continue
                else:
                    os.mkdir(os.path.join(root, dir, m))
#                   print(os.path.join(root, dir, m))

def main():
    y_dir() 
#   m_dir()

if __name__ == "__main__":
    main()
