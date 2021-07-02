import os
from dotenv import load_dotenv
from selenium import webdriver
from pyrogram import Client, filters


async def sel(bot, update):
    text = " ".join(update.text.split())
    ops = webdriver.ChromeOptions()
    load_dotenv()
    ops.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    ops.add_argument("--headless")
    ops.add_argument("--no-sandbox")
    ops.add_argument("--disable-dev-shm-usage")
    with webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=ops) as driver:
        driver.get(text.strip())
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        title = driver.find_element_by_xpath("//span[@id='folder_name']").text
        links = driver.find_elements_by_xpath("//a[@class='foldername']")
        for link in links:
            print(link.get_attribute("href"))


@Client.on_message(filters.command(["sel"]))
async def a(bot, update):
    await sel(bot, update)
