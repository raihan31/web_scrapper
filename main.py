import requests
from bs4 import BeautifulSoup
x = 0
# for x in range(844):
page = requests.get("https://medex.com.bd/brands?page=" + str(x + 1))
page_section = BeautifulSoup(page.content, 'html.parser')
main_section = page_section.find('section', class_='section')
container_div = list(main_section.children)
product_div_wrapper = list(container_div[1].children)
product_div = list(product_div_wrapper[3].children)
# print(container_div[0])
# print(container_div[2])
product_items = []
for x in product_div:
    if x != '\n':
        product_items.append(x)
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
print(product_items)