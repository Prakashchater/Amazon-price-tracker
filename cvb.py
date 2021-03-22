from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

email = "chaterprakash@gmail.com"
password = "pcchater@160997"

url = "https://www.amazon.in/Fossil-Touchscreen-Smartwatch-Smartphone-Notifications/dp/B07SRVV8V4/ref=sr_1_6?crid=1YN9U05X4YMXU&dchild=1&keywords=smart+watch+fossil&qid=1616389788&sprefix=smart+watch+foss%2Caps%2C299&sr=8-6"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
accept_lang = "en-GB,en-US;q=0.9,en;q=0.8"
header = {
    "User-Agent":user_agent,
    "Accept-Language":accept_lang,
}
proxy_dict = {
    "http":"http://www.amazon.in/Fossil-Touchscreen-Smartwatch-Smartphone-Notifications/dp/B07SRVV8V4/ref=sr_1_6?"
           "crid=1YN9U05X4YMXU&dchild=1&keywords=smart+watch+fossil&qid=1616389788&sprefix=smart+watch+foss%2Caps%2C299&sr=8-6",
    "https":"https://www.amazon.in/Fossil-Touchscreen-Smartwatch-Smartphone-Notifications/dp/B07SRVV8V4/ref=sr_1_6?crid=1YN9U05X4YMXU&dchild=1&keywords=smart+watch+fossil&qid=1616389788&sprefix=smart+watch+foss%2Caps%2C299&sr=8-6"
,

}
response = requests.get(url=url, headers=header,proxies=proxy_dict)
# website = response.text
# print(website)

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

prices = soup.find("span", id="priceblock_saleprice")
max_price = prices.getText().split()[1].replace(',',"").replace(".","").replace("00","")
price_int = int(max_price)

title = soup.find(id="productTitle").getText().strip()
print(title)

buy_price = 15000

if price_int < buy_price:
    message = f"{title} price is drooped and now in {price_int}."


    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email,
                            to_addrs=email,
                            msg=f"Subject: Amazon Price drop alert! \n\n{message}\n{url}")





