import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def get_free_game():
    # Make a request to the Epic Games API to get the free game information
    response = requests.get("https://store-site-backend-static-ipv4.ak.epicgames.com/freeGamesPromotions")

    # Check the response status code to determine if the request was successful
    if response.status_code == 200:
        game_info = response.json()
        game_name= game_info['data']['Catalog']['searchStore']['elements'][0]['productSlug']
        return game_name
    else:
        print("Failed to retrieve the free game information.")

freeGame = get_free_game()

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Navigate to the Epic Games Store
driver.get("https://www.epicgames.com/store/en-US/")

# Log in to your account
# Note: You'll need to handle the login process here

# Navigate to the game page
driver.get("https://www.epicgames.com/store/en-US/p/" + freeGame)  # replace 'game-name' with the actual game name
#time.sleep(200)

time.sleep(10)
while True:
    try:
        driver.refresh()
        time.sleep(5)
        driver.find_element("challenge-stage").click()
        print("Captcha found")
    except:
        time.sleep(5)
        print("No captcha") 
        break    

# Click on the 'Buy' button
buy_button = driver.find_element("button.buy-button")
buy_button.click()

# Handle the checkout process
# Note: You'll need to handle the checkout process here

# Confirm the purchase
# Note: You'll need to handle the purchase confirmation here

# Close the browser
driver.quit()