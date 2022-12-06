import requests
import datetime as dt
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()
# Global Variables
STOCK = "TSLA"
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")

# Get The last two closing prices of the stock
# Create variables to look up data for those two dates
today_date = dt.datetime.now()
one_day_ago = today_date - dt.timedelta(days=1)
two_days_ago = today_date - dt.timedelta(days=2)
# Adjust days for the weekend
if one_day_ago.weekday() == 6:
    one_day_ago = one_day_ago - dt.timedelta(days=2)
elif one_day_ago.weekday() == 5:
    one_day_ago = one_day_ago - dt.timedelta(days=1)
if two_days_ago.weekday() == 6:
    two_days_ago = two_days_ago - dt.timedelta(days=3)
elif two_days_ago.weekday() == 5:
    two_days_ago = two_days_ago - dt.timedelta(days=2)

# Get stock Data
parameters = {
    "apikey": STOCK_API_KEY,
    "symbol": STOCK,
    "function": "TIME_SERIES_DAILY_ADJUSTED"
}
response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
response.raise_for_status()
data = response.json()

# Find the last two closing prices
one_day_ago_closing = data["Time Series (Daily)"][str(one_day_ago.date())]["4. close"]
two_days_ago_closing = data["Time Series (Daily)"][str(two_days_ago.date())]["4. close"]
difference = float(one_day_ago_closing) - float(two_days_ago_closing)
# Dynamically create text for SMS message
if difference > 0:
    stock_status = f"🔺 {round(abs(difference), 2)}%"
elif difference < 0:
    stock_status = f"🔻 {round(abs(difference), 2)}%"


def compare_closing_prices():
    """Compares the two last closing prices and gets news about company if difference is greater than 5."""
    if abs(difference) > 5:
        get_news()


def get_news():
    """Uses NewAPI to get news from the stock and sends latest three articles to the send sms function"""
    news_parameters = {
        "apiKey": NEWS_API_KEY,
        "q": STOCK,
        "sortBy": "publishedAt"
    }
    news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()
    top_3_articles = news_data["articles"][:3]
    # Call send text function with the three articles
    send_sms(top_3_articles)


# Send Text message showing latest three articles related to Stock
def send_sms(articles):
    """Sends SMS with the three latest articles"""
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    for article in articles:
        client.messages \
            .create(
            body=f"TSLA: {stock_status}\nHeadline: {article['title']}\n{article['description']}\n{article['url']}",
            from_="+16506634889",
            to="+18187416845"
        )


compare_closing_prices()
