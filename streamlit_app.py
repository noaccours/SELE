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
    
    # No need to specify chromedriver path
    driver = webdriver.Chrome(options=options)
    
    return driver

@bot.message_handler(commands=['ss'])
def send_screenshot(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Please send the URL for which you want to capture the screenshot.")

# Function to capture screenshot based on the URL provided
@bot.message_handler(func=lambda message: True)
def capture_screenshot(message):
    chat_id = message.chat.id
    app_url = message.text.strip()  # Get the URL from the message
    screenshot_path = get_screenshot(app_url)
    with open(screenshot_path, 'rb') as photo:
        bot.send_photo(chat_id, photo)

def get_screenshot(app_url):
    driver = get_driver()
    if app_url.endswith('streamlit.app'):
        driver.get(f"{app_url}/~/+/")
    else:
        driver.get(app_url)
    
    # Add a delay to ensure page loading
    time.sleep(3)
    
    # Capture the screenshot
    screenshot_path = 'screenshot.png'
    driver.save_screenshot(screenshot_path)
    
    # Close the driver
    driver.quit()
    
    return screenshot_path

# Start the bot
bot.polling()
