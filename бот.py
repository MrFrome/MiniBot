# -*- coding: utf-8 -*-
# скрипт был создан автором канала IT THINGS:https://yotube.com/c/ITTHINGS
import vk_api
import time


token = "b9d2723129a01c8c1fa5d0389151c422b1fd615e3e431978c8b9006503c36fdfea13af6b9dea63fd1d4ca"

vk = vk_api.VkApi(token=token)

vk._auth_token()

while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if body.lower() == "привет":
                vk.method("messages.send", {"peer_id": id, "message": "Привет! \nНапиши Help чтобы узнать мои команды", "random_id": 0})
            elif body.lower() == "help":
                vk.method("messages.send", {"peer_id": id, "message": "BAT", "random_id": 0})
            elif body.lower() == "bat":
                vk.method("messages.send", {"peer_id": id, "message": "https://psfx.ru/d/v/mass_explorer/ Открывает 2000 эксплореров(отличный стресс тест для вашего пк) \n", "random_id": 0})
            elif body.lower() == "о/":
                vk.method("messages.send", {"peer_id": id, "message": "о/", "random_id": 0})
            elif body.lower() == "\о":
                vk.method("messages.send", {"peer_id": id, "message": "\о", "random_id": 0})
            else:
                vk.method("messages.send", {"peer_id": id, "message": "    ", "random_id": 0})# в кавычках текст для неверной команды
    except Exception as E:
        time.sleep(1)