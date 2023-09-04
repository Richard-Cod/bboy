from scrapy.selector import Selector
import os

# J'ai mis le contenu html dans un fichier nommé file.html 
# De ton coté tu n'as pas besoin de ça vu que la requete passe chez toi 
file_name = 'file.html'
file_path = os.path.join(os.path.dirname(__file__), file_name)
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()
    price_range = Selector(text=html_content).xpath('//div[@class="SrqKb"]/text()').get()
    print("result")
    print(price_range)