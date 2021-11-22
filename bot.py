import os
import requests
import mebots
import yaledining
import datetime


with open('token.txt', 'r') as f:
    BOT_TOKEN = f.read().strip()
bot = mebots.Bot('chickentenders', BOT_TOKEN)
dining = yaledining.API()


def serving_tenders():
    for hall in dining.halls():
        for meal in hall.meals(date=datetime.date.today()):
            for item in meal.items:
                if 'chicken tenders' in item.name.lower():
                    return True
    return False


def send(text, bot_id):
    url  = 'https://api.groupme.com/v3/bots/post'

    message = {
        'bot_id': bot_id,
        'text': text,
    }
    r = requests.post(url, json=message)


if not serving_tenders():
    bot_ids = [instance.id for instance in bot.instances()]
    for bot_id in bot_ids:
        send('It is chicken tenders day today.', bot_id)
