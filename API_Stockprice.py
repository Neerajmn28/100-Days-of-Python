import requests

STOCK_NAME = 'TSLA'
COMPANY_NAME = 'Tesla Inc'
STOCK_ENDPOINT = 'https://www.alphavantage.co/query'
NEWS_ENDPOINT = 'https://newsspi.org/v2/everything'
STOCK_API = 'QUVSA12ZFUQFBHOI'
NEWS_API = '2dda861956be4e42a1c46d8aadb1f10e'

stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'apikey': 'QUVSA12ZFUQFBHOI'
}

response = requests.get(STOCK_ENDPOINT, params = stock_params)
data = response.json()['Time Series (Daily)']
data_list = [value for(key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']
day_before_yesterday_data = yesterday_data[1]
print(yesterday_closing_price)


difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_data))
up_down = None
if difference > 0:
    up_dowm = '⬆️'
else:
    up_down = '⬇️'
        
    

diff_percent = round(difference / float(yesterday_closing_price))* 100


if diff_percent > 1:
    news_params = {
        'apikey' : NEWS_API,
        'qInTitle': COMPANY_NAME
    }
    
    news_response = requests.get(NEWS_ENDPOINT, params = news_params)
    articles = news_response.json()['articles']
    
    
    three_articles = articles[:3]
    print(three_articles)
    
    
    formated_article = [f'{S }Headline: {article['title']}. \nBrief: {article['desription']}' for article in three_articles]
    
    
    