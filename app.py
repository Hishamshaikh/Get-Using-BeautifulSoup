import requests
from bs4 import BeautifulSoup
request = requests.get("https://www.gasjeans.com/in_en/denim/man/jeans-slim.html")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"class": "regular-price"})
string_price = element.text.strip()
price_without_symbol = string_price[1:2]
price = float(price_without_symbol)
print(price)

if price < 10:
    print("You should buy the chair")
else:
    print("Do not buy, its too expensive")


