from dotenv import load_dotenv
from src.data_bot import DataBot

if __name__ == '__main__':
    load_dotenv()
    bot = DataBot()
    tracked_symbols = [
        'AAPL', 'BNGO', 'CCL', 'COCP', 'DKNG', 'F', 'GE', 'HD', 'INTC', 'MSFT',
        'MVIS', 'NIO', 'PLUG', 'T', 'X'
    ]

    bot.track_day(tracked_symbols)
