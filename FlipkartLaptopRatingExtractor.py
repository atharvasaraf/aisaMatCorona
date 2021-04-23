# Web Scraper tool to extract and store Laptop Names, Rating and Prices from Flipkart Page
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver


def main():
    driver = webdriver.Firefox()
    products = []
    prices = []
    ratings = []

    driver.get(
        "https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
    )

    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    for a in soup.find_all('div', attrs={'class': "_13oc-S"}):
        name = a.find('div', attrs={'class': '_4rR01T'})
        price = a.find('div', attrs={'class': '_30jeq3 _1_WHN1'})
        rating = a.find('div', attrs={'class': '_3LWZlK'})
        products.append(name.text)
        prices.append(price.text)
        ratings.append(rating.text)
    df = pd.DataFrame({'Product Name': products, 'Price': prices, 'Rating': ratings})
    df.to_csv('products.csv', index=False, encoding='utf-8')


if __name__ == "__main__":
    main()
