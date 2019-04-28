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
    def get_page():
        return requests.get(url)
    def get_beautified_page(raw_page):
        return BeautifulSoup(raw_page.content, 'html.parser')
    def get_page_section_by_selector(beautified_page):
        return beautified_page.find(element, class_=selector)
    def find_section_children(index, page_section):
        return list(page_section[index].children) if index else list(page_section.children)
    def get_brands(raw_brand_list):
        brands = []
        for brand in raw_brand_list:
            if brand != '\n':
                brands.append(brand)
        return brands
    def brand_scrapper():
        for page_number in range(pages):
            url = url + '?page=' + str(page_number + 1)
            page = get_page()
            beautified_page = get_beautified_page(page)
            container_div = find_section_children(None, beautified_page)
            product_div_wrapper = find_section_children(1, container_div)
            product_div = find_section_children(3, product_div_wrapper)
            brands = get_brands(product_div)
            print('page: ' + str(page_number + 1))
            print(brands)