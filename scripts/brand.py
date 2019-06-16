import requests
from bs4 import BeautifulSoup
class Brand(object):
    url = ''
    pages = 0
    element = ''
    selector = ''
    def __init__(self, url, page_limit, el, sl):
        self.url = url
        self.pages = page_limit
        self.element = el
        self.selector = sl
    def get_page(self):
        return requests.get(self.url)
    def get_beautified_page(self, raw_page):
        return BeautifulSoup(raw_page.content, 'html.parser')
    def get_page_section_by_selector(self, beautified_page):
        return beautified_page.find(self.element, class_=self.selector)
    def find_section_children(self, index, page_section):
        return list(page_section[index].children) if index else list(page_section.children)
    def get_brands(self, raw_brand_list):
        brands = []
        for brand in raw_brand_list:
            if brand != '\n':
                brands.append(brand)
        return brands
    def brand_scrapper(self):
        for page_number in range(self.pages):
            self.url = self.url + '?page=' + str(page_number + 1)
            page = self.get_page()
            beautified_page = self.get_beautified_page(page)
            section_div = self.get_page_section_by_selector(beautified_page)
            container_div = self.find_section_children(None, section_div)
            product_div_wrapper = self.find_section_children(1, container_div)
            product_div = self.find_section_children(3, product_div_wrapper)
            brands = self.get_brands(product_div)
            print(brands)