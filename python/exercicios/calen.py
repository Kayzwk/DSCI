import calendar
import sys

def exibe (year, month):
    #year = 2023
    #month = 11
    for month in range (1,13):
        x = calendar.month(year,month)

        print(x)

if __name__ == '__main__':
    if len(sys.argv)==3:
        exibe(int(sys.argv[1]),int(sys.argv[2]))
        