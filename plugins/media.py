import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from pyrogram import Client, filters


async def scrap(bot, update):
    text = " ".join(update.text.split(" ")[1:])
    r = requests.get(text).content
    soup = BeautifulSoup(r, "html.parser")
    ht = re.findall(r'"https://[\s]{0,1000}[\S]{0,1000}"', str(r))
    regex = [i.replace('"', "") for i in ht]
    print(regex)
    a = soup.find_all("a")
    c = [b.get("href") for b in a]
    print(c)


@Client.on_message(filters.command(["scrap"]))
async def a(bot, update):
    await scrap(bot, update)

