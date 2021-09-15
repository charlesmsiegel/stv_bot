from bs4 import BeautifulSoup
from get_page import get_page


def deduplicate(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]


def get_info(url):
    html = get_page(url)
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find('h1').get_text()
    # print(title)

    all_links = soup.find_all('a', href=True)
    all_links = list(all_links)
    authors = [x for x in all_links if "?author" in x.get('href')]
    authors = [x.get('href') for x in authors]
    authors = [x.split("?author=")[-1] for x in authors]

    authors = deduplicate(authors)

    author_join = ", ".join(authors)

    # print(", ".join(authors))

    txt = f"{author_join} released {title} {url}"
    return txt
