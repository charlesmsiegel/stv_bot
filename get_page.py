from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def get_page(url):
    try:
        firefox_options = Options()
        firefox_options.headless = True
        brower = webdriver.Firefox(options=firefox_options)

        brower.get(url)
        html = brower.page_source
    finally:
        try:
            brower.close()
        except:
            pass
    return html
