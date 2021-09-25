import json
import requests


def get_product(product_id):
    with open('data.json', 'r') as f:
        data = json.load(f)

    query = data["query_product"].replace("PRODUCTID", f"{product_id}")
    response = requests.get(query)
    product = json.loads(response.text)['data']

    title = product['attributes']['description']['name']
    authors = product['attributes']['authors']
    if len(authors) == 1:
        verb = "has"
    else:
        verb = "have"
    price = float(product['attributes']['price'])
    authors = ", ".join(authors)

    url = "https://www.storytellersvault.com/product/" + product_id + "/"

    if authors == "":
        return f"{title} has been released at ${price:.02f}! {url}"
    return f"{authors} {verb} released {title} at ${price:.02f}! {url}"
