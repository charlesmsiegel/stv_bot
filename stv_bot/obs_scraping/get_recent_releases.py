import json
import requests


def get_recent_releases(safety_length=1):
    with open('data.json', 'r') as f:
        data = json.load(f)

    query = data["query_stv_list"].replace("PAGENUMBER", "1")
    response = requests.get(query)
    product = json.loads(response.text)['data']

    most_recent = data['most_recent']

    ids = [prod['attributes']['productId'] for prod in product]

    try:
        most_recent_index = ids.index(most_recent)
    except ValueError:
        most_recent_index = safety_length

    current_ids = ids[:most_recent_index]
    return current_ids
