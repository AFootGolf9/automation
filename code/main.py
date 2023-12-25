import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


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
