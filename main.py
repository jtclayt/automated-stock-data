from dotenv import load_dotenv
from src.data_bot import DataBot

if __name__ == '__main__':
    load_dotenv()
    bot = DataBot()
    bot.get_quotes(['AAPL', 'AMZN', 'FAKEDAS', 'MSFT', 'T'])
