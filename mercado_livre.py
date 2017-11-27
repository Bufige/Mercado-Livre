from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from enum import Enum

from bs4 import BeautifulSoup
import requests


class Browser_Type(Enum):
    CHROME = 1
    FIREFOX = 2


class Browser:
    def __init__(self, type):
        if type == Browser_Type.CHROME:
            chromeOptions = webdriver.ChromeOptions()
            prefs = {"profile.managed_default_content_settings.images": 2}
            chromeOptions.add_experimental_option("prefs", prefs)
            chromeOptions.add_argument('--headless')
            self.browser = webdriver.Chrome(chrome_options=chromeOptions)
        elif type == Browser_Type.FIREFOX:
            # possível adicionar o driver do firefox aqui e configurar.
            pass
        else:
            # adicionar outro tipo
            pass

    def close(self):
        # fechamos o drive
        self.browser.quit()

    def GoTo(self, url):
        # se o driver, vamos a url
        if self.browser:
            self.browser.get(url)

    def GetLinks(self):

        # driver não foi inicializado, logo paramos aqui.
        if not self.browser:
            return None

        # pegamos os links da página atual
        page_items = self.browser.find_elements_by_css_selector(
            "a[class='item__info-link item__js-link ']")
        # uma lista para salvar os items
        items = []
        # acessamos os links da página e adicionamos nela lista.
        for link in page_items:
            # get each link
            tmp = link.get_attribute('href')
            # append to the array
            items.append(tmp)
        # retornamos a lista
        return items

    def NextPage(self):
        # tentamos ver se é possível ir para a proxima página.
        try:
            pag_next = self.browser.find_element_by_css_selector(
                "li[class='pagination__next']").find_element_by_tag_name('a')
            pag_next.click()
        except:
            return False
        return True

    def GetData(self, url):
        # paracriamos um dictionary para salvar nossos dados importantes.
        data = {}
        req = requests.get(url)
        page = req.text
        soup = BeautifulSoup(page,'lxml')
        item_title = soup.find('h1', class_='item-title__primary ').get_text().strip()
        item_price = soup.find('span', class_='price-tag-fraction').get_text().strip().replace('.', '')
        data['item_title'] = item_title
        data['item_price'] = item_price
        return data
