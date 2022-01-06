from bs4 import BeautifulSoup
import requests

PRODUCT_URI=input("Enter product url: ")
price = 0

def get_product_price(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    available=soup.find("div",{"id":"availability"}).text
    if "Currently unavailable." in available:
        print("Product is currently unavailable.")
        return False
    price_parent = soup.find("span", {"class": "a-price a-text-price a-size-medium apexPriceToPay"}).text
    price = price_parent.split("₹")[1]
    print("Price: ₹", price)
    return True

get_product_price(PRODUCT_URI)