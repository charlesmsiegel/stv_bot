from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json


def get_url(url):
    try:
        fireFoxOptions = Options()
        fireFoxOptions.headless = True
        brower = webdriver.Firefox(options=fireFoxOptions)

        brower.get(url)
        html = brower.page_source
    finally:
        try:
            brower.close()
        except:
            pass
    return html

html = get_url('http://www.storytellersvault.com')
soup = BeautifulSoup(html, 'html.parser')

all_links = soup.find_all('a', href=True)
all_links = list(all_links)
new_products = [
    x for x in all_links if "?src=newest_community" in x.get('href')][::2]

urls = [x.get('href') for x in new_products]
urls = [x.split("?")[0] for x in urls]

with open('tmp.json', 'r') as f:
    most_recent = json.load(f)['most_recent']
new_items = urls[:urls.index(most_recent)]
for item in new_items:
    print(item)

# TODO: Get information from new_item urls
# TODO: Update most_recent
# TODO: Handle if nothing more recent
# TODO: Send to twitter
