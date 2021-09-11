from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

try:
    fireFoxOptions = Options()
    fireFoxOptions.headless = True
    brower = webdriver.Firefox(options=fireFoxOptions)

    brower.get('http://www.storytellersvault.com')
    # print(brower.page_source)
    html = brower.page_source
finally:
    try:
        brower.close()
    except:
        pass


soup = BeautifulSoup(html, 'html.parser')

print("Black Aegis Bundle" in soup.prettify())
# print(soup.prettify())
