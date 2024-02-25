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

# Set the desired width and height
width = 1000
height = 600

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

# Example usage
app_url = 'https://facebook.com'  
print("success")
get_screenshot(app_url)
