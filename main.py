import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import os
def send_alert(curr_price , limit_price):    
    msg = f'the price of the tracked product has reached {curr_price} which is in the range of the lowest price of {limit_price} in the past!!, hurry up go and purchase'
    my_password = os.environ['MY_PASS']
    my_email = os.environ['MY_EMAIL']

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(my_email, my_password)
    s.sendmail(my_email, my_email ,msg)
    s.quit()



product_url = '''https://www.amazon.com/Lenovo-V15-Hexa-core-Processor-i7-1065G7/
dp/B0CK9FQXWR/ref=sr_1_6?crid=17UJDNKPRGEZ3&keywords=LAPTOP&qid=1702478458&sprefix=laptop%2Caps%2C303&sr=8-6&th=1'''

my_header = {
    'Accept-Language':'en-GB,en-US;q=0.9,en;q=0.8',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}

response = requests.get(url=product_url,headers= my_header)
data = response.text
soup = BeautifulSoup(data , 'lxml')
object_price = soup.find(name='span' , id='price_inside_buybox')

curr_price = object_price.get_text()
curr_price = float(curr_price.replace('$',''))

min_price_in_past = 487.95
#if the price drops in range of five percent of the min price than we will buy it
max_accepted_price = min_price_in_past + (0.05 * min_price_in_past)

if curr_price <= max_accepted_price:
    send_alert(curr_price , max_accepted_price)




