from selenium import webdriver
from pyrogram import Client, filters
from selenium.webdriver.firefox.options import Options


async def sel(bot, update):
    text = " ".join(update.text.split())
    op = Options()
    op.headless = True
    with webdriver.Firefox(options=op) as driver:
        driver.get(text)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        title = driver.find_element_by_xpath("//span[@id='folder_name']").text
        links = driver.find_elements_by_xpath("//a[@class='foldername']")
        for link in links:
            print(link.get_attribute("href"))


@Client.on_message(filters.command(["sel"]))
async def a(bot, update):
    await sel(bot, update)