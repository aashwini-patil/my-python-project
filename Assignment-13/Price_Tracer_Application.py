import requests
from bs4 import BeautifulSoup

class PriceTracker:
    def __init__(self,url):
        self.url = url
        self.user_agent = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"}
        self.responce = requests.get(url=self.url, headers =self.user_agent).text
        self.soup= BeautifulSoup(self.responce, 'lxml')  #lxml parcer type

    def product_title(self):
        title = self.soup.find("span", {"id":"productTitle"})
        if title is not None:
            return title.text.strip()
        else:
            return "Tag not found"

    def product_price(self):
        price = self.soup.find("span", {"class":"a-price-whole"})
        if price is not None:
            return price.text.strip()
        else:
            return "Tag not found"

    def product_about(self):
        about = self.soup.find("ul", {"class":"a-unordered-list a-vertical a-spacing-mini"})
        if about is not None:
            return about.text.strip()
        else:
            return "Tag not found"


# obj = PriceTracker(url= "https://www.amazon.in/Redmi-Note-Neptune-Blue-Storage/dp/B07X1KT6LD/ref=pd_lpo_d_sccl_2/260-9212333-6687321?pd_rd_w=O09Pc&content-id=amzn1.sym.e0c8139c-1aa1-443c-af8a-145a0481f27c&pf_rd_p=e0c8139c-1aa1-443c-af8a-145a0481f27c&pf_rd_r=T8TRR4YDZ4CFXCQVTQVY&pd_rd_wg=lATwN&pd_rd_r=6b6b611e-ccd0-42bd-99e9-5bcaaf69b058&pd_rd_i=B07X1KT6LD&psc=1")
# print(obj.product_title())
# print(obj.product_price())

obj = PriceTracker(url= "https://www.amazon.in/iQOO-Dimensity-Processor-Military-Grade-Durability/dp/B0F2T674FJ/ref=pd_day0fbt_d_sccl_1/260-9212333-6687321?pd_rd_w=1wqZ6&content-id=amzn1.sym.49b8932b-8f39-4ca5-a10c-a436913a4b73&pf_rd_p=49b8932b-8f39-4ca5-a10c-a436913a4b73&pf_rd_r=JMFT7VBF4AEVWQ4RJW4R&pd_rd_wg=Ibv3W&pd_rd_r=916eadc2-08fe-45df-b434-6c26b934267a&pd_rd_i=B0F2T674FJ&th=1")
print(obj.product_title())
print(obj.product_price())
print(obj.product_about())