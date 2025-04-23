import requests
import smtplib

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = ''

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = ""

GMAIL_EMAIL = "Bugs.Bunny@amcemail.com"
PASSWD_G = ""
HOTMAIL_EMAIL = "Bugs.Bunny@amcemail.com"
PASSWD_H = ""


api_perams = {
    'function': 'TIME_SERIES_DAILY',
    'symbol':  STOCK_NAME,
    'apikey': STOCK_API_KEY,
    'verify': False
}

response = requests.get(url=STOCK_ENDPOINT, params=api_perams)
# print(response.status_code)
response.raise_for_status()

# stock_data = response.json()
stock_data = response.json()['Time Series (Daily)']

data_list = [value for (key,value) in stock_data.items()]

# print(data_list)

yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']
# print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
# print(day_before_yesterday_closing_price)

neg_difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
pos_difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
# print(neg_difference)
# print(pos_difference)

diff_percent = (pos_difference / float(yesterday_closing_price)) * 100

# print(diff_percent)
formatted_articles = []

if diff_percent > 3:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    # print("Get News")
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()['articles']
    # print(articles)
    
    top_three_articles = articles[:3]
    # print(top_three_articles)

    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in top_three_articles]

    print(formatted_articles)
# print(formatted_articles[0])
# print(formatted_articles[1])
# print(formatted_articles[2])
# print(len(formatted_articles))
    # with smtplib.SMTP("smtp.gmail.com") as connection:
    #     connection.starttls()
    #     connection.login(GMAIL_EMAIL, PASSWD_G)
    #     connection.sendmail(from_addr=GMAIL_EMAIL, to_addrs=HOTMAIL_EMAIL,
    #                         msg=f"Subject:Company News\n\n {formatted_articles}") 

# for article in formatted_articles:
#     print(article)

    for article in formatted_articles:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(GMAIL_EMAIL, PASSWD_G)
            connection.sendmail(from_addr=GMAIL_EMAIL, to_addrs=HOTMAIL_EMAIL,
                                msg=f"Subject:Company News\n\n {article}")

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(GMAIL_EMAIL, PASSWD_G)
#     connection.sendmail(from_addr=GMAIL_EMAIL, to_addrs=HOTMAIL_EMAIL,
#                         msg=f"Subject:Company News\n\n {formatted_articles}")    

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(GMAIL_EMAIL, PASSWD_G)
#     connection.sendmail(from_addr=GMAIL_EMAIL, to_addrs=HOTMAIL_EMAIL,
#                         msg=f"Subject:Company News\n\n {formatted_articles[0]}\n{formatted_articles[1]}\n{formatted_articles[2]}")


# print(stock_data)
# print(stock_data.keys())
# print(stock_data['Time Series (Daily)'])
# print(stock_data['Time Series (Daily)']['2024-07-15'])
# print(f"2024-07-15: {stock_data['Time Series (Daily)']['2024-07-15']}")
# print(stock_data['Time Series (Daily)']['2024-07-16'])
# print(f"2024-07-16: {stock_data['Time Series (Daily)']['2024-07-16']}")

# for (key,value) in stock_data['Time Series (Daily)'].items():
#     if key == '2024-07-15' or key == '2024-07-16':
#         print(f"Date: {key}: Closing Value: {value['4. close']}")

# yesterdays_closing_num = [float(value['4. close']) 
#                           for (key,value) in stock_data['Time Series (Daily)'].items() 
#                           if key == '2024-07-16'
#                           ]
# print(yesterdays_closing_num[0])
# print(type(yesterdays_closing_num[0]))

# day_before_closing_num = [float(value['4. close']) 
#                           for (key,value) in stock_data['Time Series (Daily)'].items() 
#                           if key == '2024-07-15'
#                           ]
# print(day_before_closing_num[0])
# print(type(day_before_closing_num[0]))

# if yesterdays_closing_num > day_before_closing_num:
#     difference_between = float(yesterdays_closing_num) - float(day_before_closing_num)
# else:
#     difference_between = float(day_before_closing_num - yesterdays_closing_num)

# print(f"The difference is: {difference_between}")

# yesterdays_closing_num = {key:value for (key, value) in stock_data.items()}

# print(yesterdays_closing_num)
