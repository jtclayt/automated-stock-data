import os
from datetime import datetime as dt


class Logger:
    '''Logger for creating log files'''
    def __init__(self):
        self.logdir = './logs'

    def log(self, message: str):
        '''Method for logging a message, organized by date of log'''
        now = dt.now()
        filename = f'{now.day}.log'
        initial_dir = os.getcwd()

        self.__navigate_to_dir(now)

        with open(filename, 'a') as f:
            f.write(f'{now.strftime("%H:%M:%S")} - {message}\n')
            f.close()

        os.chdir(initial_dir)

    def __navigate_to_dir(self, now):
        '''Handle navigating to folder containing todays logs'''
        year = str(now.year)
        month = str(now.month)

        if not os.path.isdir(self.logdir):
            os.mkdir(self.logdir)
        os.chdir(self.logdir)

        if not os.path.isdir(year):
            os.mkdir(year)
        os.chdir(year)

        if not os.path.isdir(month):
            os.mkdir(month)
        os.chdir(month)
