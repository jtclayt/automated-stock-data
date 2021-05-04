import csv
from datetime import datetime as dt
import os


class CsvWriter:
    '''Class for appending to csv data file'''
    def __init__(self):
        self.datadir = './data'

    def write(self, symbol: str, row):
        '''Method for appending a new row to csv file'''
        now = dt.now()
        row.append(now.time())
        filename = f'{now.day}.csv'
        initial_dir = os.getcwd()

        self.__navigate_to_dir(symbol, now)

        with open(filename, 'a') as f:
            cw = csv.writer(f)
            cw.writerow(row)
            f.close()

        os.chdir(initial_dir)


    def __navigate_to_dir(self, symbol: str, now: dt):
        '''Handle navigating to folder containing todays logs'''
        year = str(now.year)
        month = str(now.month)

        if not os.path.isdir(self.datadir):
            os.mkdir(self.datadir)
        os.chdir(self.datadir)

        if not os.path.isdir(symbol):
            os.mkdir(symbol)
        os.chdir(symbol)

        if not os.path.isdir(year):
            os.mkdir(year)
        os.chdir(year)

        if not os.path.isdir(month):
            os.mkdir(month)
        os.chdir(month)
