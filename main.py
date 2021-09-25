import json
import stv_bot

current_ids = stv_bot.obs_scraping.get_recent_releases()[::-1]
with open("data.json", "r") as f:
    tmp_dict = json.load(f)

if len(current_ids) > 0:
    tmp_dict["most_recent"] = current_ids[-1]

with open("data.json", "w") as f:
    json.dump(tmp_dict, f, indent=4)

for identifier in current_ids:
    text = stv_bot.obs_scraping.get_product(identifier)
    stv_bot.social_media.send_tweet(text)
