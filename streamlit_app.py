import streamlit as st
import time
import psutil
import random
import os
import sys
from PIL import Image, ImageDraw, ImageOps
from PIL.Image import Resampling
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from os.path import exists
import telebot

# Set the desired width and height
width = 1000
height = 600

# Initialize your Telegram bot
bot = telebot.TeleBot("6148264758:AAHCAU_v3P9SAkCZLPuS6sStZ9Fhbjskp_w")

def get_driver():
    options = webdriver.ChromeOptions()
    
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')
    options.add_argument(f"--window-size={width}x{height}")
    
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    
    return webdriver.Chrome(service=service, options=options)

def get_screenshot(app_url):
    driver = get_driver()
    if app_url.endswith('streamlit.app'):
        driver.get(f"{app_url}/~/+/")
    else:
        driver.get(app_url)

#time.sleep(3)
    
    # Capture the screenshot
    screenshot_path = 'screenshot.png'
    driver.save_screenshot(screenshot_path)
    
    # Close the driver
    driver.quit()
    
    return screenshot_path

# Example usage
app_url = 'https://facebook.com'  # Set the URL you want to capture
print("Success")
screenshot_path = get_screenshot(app_url)

# Sending the screenshot to Telegram
@bot.message_handler(commands=['ss'])
def send_screenshot(message):
    chat_id = message.chat.id
    with open(screenshot_path, 'rb') as photo:
        bot.send_photo(chat_id, photo)

# Start the bot
bot.polling()

