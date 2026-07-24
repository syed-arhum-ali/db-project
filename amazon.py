from bs4 import BeautifulSoup
from openpyxl import Workbook
from curl_cffi import requests

URL = "https://www.amazon.com/s?k=gaming&_encoding=UTF8&content-id=amzn1.sym.bd749ccd-05a5-46df-9094-58bcc6398482&pd_rd_r=76fd352a-207d-46cf-b8ea-af06e9aafec9&pd_rd_w=jR96k&pd_rd_wg=Dss5S&pf_rd_p=bd749ccd-05a5-46df-9094-58bcc6398482&pf_rd_r=3VCWJC82N64CK2M4J462&ref=pd_hp_d_atf_unk"
# ye header ai hn
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Connection": "keep-alive"
}

print("Connecting to Amazon...")
response = requests.get(URL, headers=headers)
print(response)
#ye ai hn
if "captcha" in response.text.lower() or "api-services-support@amazon.com" in response.text:
    print("Warning: Amazon returned a bot-check/CAPTCHA page, not real results.")
    
try:
    soup = BeautifulSoup(response.text, "lxml")
except Exception:
    soup = BeautifulSoup(response.text, "html.parser")

products = soup.find_all("div", {"data-component-type": "s-search-result"})
print(f"Found {len(products)} product blocks")  

wb = Workbook()
ws = wb.active
ws.title = "Amazon Scraped Data"
ws.append(["Title", "Price", "delivery date", "sales"])

for i, items in enumerate(products, 1):
    try:
        title_element = items.find("h2")
        title = (
            title_element.text.strip()
            if title_element
            else "no title"
        )

        price_symbol = items.find("span", class_="a-price-symbol")
        price_whole = items.find("span", class_="a-price-whole")
        price_fraction = items.find("span", class_="a-price-fraction")
        if price_symbol and price_whole and price_fraction:
            price = f"{price_symbol.text.strip()}{price_whole.text.strip()}{price_fraction.text.strip()}"
        else:
            price = "N/A"

        delivery_el = items.find("span", {"data-a-color": "secondary"})
        delivery_date = (
            delivery_el.text.strip()
            if delivery_el and "delivery" in delivery_el.text.lower()
            else "N/A"
        )

        
        bought_element = items.find("span", string=lambda text: bool(text) and "bought in past month" in text)
        bought_volume = (bought_element.text.strip() if bought_element else "N/A")

        ws.append([title, price, delivery_date, bought_volume])

    except Exception as e:
        print(e)

wb.save("excel_file_values.xlsx")
print("Done! Spreadsheet file generated.")