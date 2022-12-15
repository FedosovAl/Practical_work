from loader import bot
import handlers
from utils.set_bot_commands import set_default_commands
from config_data.config import get_all_commands

import requests
import json

if __name__ == '__main__':
    # set_default_commands(bot)
    url = "https://hotels4.p.rapidapi.com/locations/v3/search"

    querystring = {"q": "prague"}

    headers = {
        "X-RapidAPI-Key": "9d54a2ed5emshcdbb7885d393718p19f2a6jsn81ad9223bc38",
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
    with open('hotel.json', 'w') as file:
        json.dump(data, file, indent=4)

    print(response.text)
    bot.infinity_polling()
