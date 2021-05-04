import os
import requests

from .util.csv_writer import CsvWriter
from .util.logger import Logger

class DataBot:
    '''Class for handling automated data collection'''
    def __init__(self):
        self.api_url = 'https://api.tdameritrade.com/v1/marketdata'
        self.apikey = os.environ['TD_APIKEY']
        self.logger = Logger()
        self.csv_writer = CsvWriter()

    def get_quotes(self, symbol_list: list):
        '''Get current quotes for a list of symbols'''
        symbols = ','.join(symbol_list)
        url = f'{self.api_url}/quotes?symbol={symbols}'
        self.logger.log(f'Making GET request: {url}')
        r = requests.get(f'{url}&apikey={self.apikey}')
        self.logger.log(f'GET response code: {r.status_code}')

        for sym in symbol_list:
            row = self.__extract_data(sym, r.json())

            if len(row) > 0:
                self.csv_writer.write(sym, row)

    def __extract_data(self, sym: str, data: dict):
        '''Extract desired data from response'''
        if sym not in data:
            self.logger.log(f'{sym} - No data returned')
            return []

        self.logger.log(f'{sym} - Data returned')
        return [
            data[sym]['bidPrice'],
            data[sym]['bidSize'],
            data[sym]['askPrice'],
            data[sym]['askSize'],
            data[sym]['totalVolume'],
            data[sym]['volatility']
        ]

