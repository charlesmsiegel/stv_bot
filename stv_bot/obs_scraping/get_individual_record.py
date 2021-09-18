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
    price = float(product['attributes']['price'])
    # gamelines = None  # TODO: Extract gamelines info
    # editions = None  # TODO: Extract editions info
    # ranking = [product['attributes']['ranking'][x]['humanName']
    #            for x in product['attributes']['ranking'].keys()]
    authors = ", ".join(authors)

    # TODO: handle PWYW titles better

    if authors == "":
        return f"{title} has been released at ${price:.02f}! https://www.storytellersvault.com/product/{product_id}/"
    else:
        return f"{authors} have released {title} at ${price:.02f}! https://www.storytellersvault.com/product/{product_id}/"
