from bs4 import BeautifulSoup

from selenium.webdriver import Firefox, PhantomJS

import re
from tkinter import *

def clicked_btn_search():


    number = first_param.get()
    browser = Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\geckodriver.exe')
    #browser = PhantomJS(executable_path=r'C:\Program Files\phantomjs-2.1.1-windows\bin\phantomjs.exe')

    browser.get('http://www.unda.com.ua/proverka-gosnomer-UA/')
    browser.find_element_by_class_name("input").send_keys(number)
    browser.find_element_by_xpath("//form[@class='search']/button").click()

    page = BeautifulSoup(browser.page_source, 'lxml')


    car_info = page.find("div",class_='alert alert-text').text


    #Модель:.{1,25}\s

    car_model = re.findall(r'Модель:[a-яА-Яa-zA-Z]{3,}\s[a-zA-Z0-9]{1,}', car_info)
    if car_model == []:
        car_model = re.findall(r'Модель:.{1,25}\s', car_info)[0][0:-4]


    car_year = re.findall(r'Год выпуска:\d{4}', car_info)
    try:
        car_current_price,car_smoler_price,car_biggest_price =re.findall(r"\d{1,}`\d{3}", car_info)
    except :
        car_current_price = re.findall(r'а\s\d{3}', car_info)[0][1::]
        car_smoler_price = re.findall(r'от\s\d{3}', car_info)[0][2::]
        try:
            car_biggest_price = re.findall(r"\s\d{3}", car_info)[0][2::]
            print("Try {}".fromat(car_biggest_price))
        except:
            car_biggest_price = re.findall(r"\d{1,}`\d{3}", car_info)[0]
            print(car_biggest_price)



    text.insert(1.0,
                "Номер {}\n{}\n"
                "{}\n\n"
                "Средняя стоимость {}$ \n\n"
                "Цены от {}$ до {}$\n\n".format(number, car_model,car_year, car_current_price,car_smoler_price,car_biggest_price)

                )


window = Tk()
window.title("Car Seacher")

window.geometry('500x500')  # размер окна
first_param= Entry(window,width=30)
first_param.place(x=100,y=0)

btn = Button(window, text="Search",command = clicked_btn_search)
btn.place(x=280,y=0)
text = Text()
text.place(x=10,y=100)




window.mainloop()


