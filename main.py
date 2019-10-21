
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium import webdriver


# options = webdriver.FirefoxOptions()
# options.add_argument('headless')
# browser = Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe',options = options)
#
# browser.get('https://projectmooncircle.bandcamp.com/track/dim-lights-and-meteorites-featuring-sorrow')
# browser.find_element_by_class_name('playbutton').click()

# import requests
#
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
# bsObj = BeautifulSoup(html)
# for link in bsObj.findAll("a"):
#  print(link.attrss)
#  if 'href' in link.attrs:
#     print(link.attrs['href'])



from sqlalchemy import create_engine
from bs4 import BeautifulSoup
import requests
import re
import os


if os.path.exists("some.db"):
    os.remove("some.db")
e = create_engine("sqlite:///some.db")
e.execute("""
    create table ebay_notepads (
        notepad_id integer primary key,
        notepad_name varchar,
        notepad_subname varchar ,
        notepad_brand varchar,
        notepad_country varchar,
        notepad_praice float,
        notepad_shipping float,
        notepad_sail_value varchar   
    )
""")

iterator = 1
while True:


    source = requests.get('https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276?_pgn={}'.format(iterator))
    soup = BeautifulSoup(source.text, 'lxml')


    try:
        if "0 results found." in soup.find_all('span', class_='page-notice__content')[0].text:
            print("break")
            break
    except Exception:
            pass


    for items in soup.find_all('li', class_='s-item'):
        try:
            item_title = items.find('h3', class_='s-item__title').text
        except Exception:
            item_title = 'None'

        print(item_title)
        try:
            item_desc = items.find('div', class_='s-item__subtitle').text
        except Exception :
            item_desc = 'None'

        print(item_desc)
        try:
            item_brand = items.find('span', class_='s-item__dynamic s-item__dynamicAttributes1').text.split(' ')[1]
        except Exception :
            item_brand = 'None'

        print(item_brand)
        try:
            item_model = items.find('span', class_='s-item__dynamic s-item__dynamicAttributes2').text.split(' ')[1:]
            item_model = ' '.join(item_model)
        except Exception :
            item_model = 'None'
        print(item_model)
        try:
            item_features = items.find('span', class_='s-item__dynamic s-item__dynamicAttributes3').text.split(' ')[1]
        except Exception :
            item_features = 'None'
        print(item_features)
        try:
            item_origin = items.find('span', class_='s-item__location s-item__itemLocation').text
            item_origin = re.sub('From ', '', item_origin)
        except Exception :
            item_origin = 'None'
        print(item_origin)
        try:
            item_price = items.find('span', class_='s-item__price').text
        except Exception :
            item_price = 'None'
        print(item_price)
        try:
            item_shipping = items.find('span', class_='s-item__shipping s-item__logisticsCost').text
        except Exception :
            item_shipping = 'None'
        print(item_shipping)
        try:
            item_top_seller = items.find('span', class_='s-item__etrs-text').text
        except Exception :
            item_top_seller = 'None'
        print(item_top_seller)
        try:
            item_stars = items.find('span', class_='clipped').text.split(' ')[0]
        except Exception :
            item_stars = 'None'
        print(item_stars)
        try:
            item_link = items.find('a', class_='s-item__link')['href']
        except Exception :
            item_link = 'None'
        print(item_link)
        e.execute(
            "insert into ebay_notepads (notepad_name, notepad_subname, notepad_brand,notepad_country,notepad_praice,notepad_shipping,notepad_sail_value) values (:n,:sn,:b,:c,:p,:sh,:sv)",
            n = item_title,sn =item_desc, b =item_brand, c = item_model,p= item_origin,sh = item_price,sv = str(item_link),)

    iterator+=1
    # if  iterator>2:
    #     break

result = e.execute("select * from ebay_notepads")
for row in result:
    print(row)