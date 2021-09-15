from get_urls import get_new_item_urls
from get_info import get_info
from send_tweet import send_tweet

new_urls = get_new_item_urls()
for url in new_urls:
    print(url)
    image, text = get_info(url)
    send_tweet(image, text)
