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
            print(meal.id)


def process(message):
    bot_ids = [instance.id for instance in bot.instances()]



def send(text, group_id):
    url  = 'https://api.groupme.com/v3/bots/post'

    message = {
        'bot_id': bot.instance(group_id).id,
        'text': text,
    }
    r = requests.post(url, json=message)


print(serving_tenders())
