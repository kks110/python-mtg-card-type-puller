#Used for processing JSONS files
import json
#Used to get the URL
import requests
#Used to modify a file
import fileinput
#Used to download the images
import urllib.request
#Used to interact with the OS file system
import os
#Used to export the data to a CSV
import csv


def pullList():
    creatureInput = input("What type of creatures are you looking for? - ")
    #API call to get the JSON file
    API = "https://api.scryfall.com/cards/search?q=t:" + creatureInput
    response = requests.get(API)
    JSON = response.json()
    #Creates the CSV file
    with open('mtg_' + creatureInput + '.csv', 'w', newline='', encoding='utf8') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        #Counts the amount of cards in the set
        cardCountStage = JSON['data']
        setCount = len(cardCountStage)
        for Counter in range(setCount):
            #Prints the data out on screen and also puts it in to the CSV file
            CardName = JSON['data'][Counter]['name']
            cardColour = JSON['data'][Counter]['color_identity']
            rarity = JSON['data'][Counter]['rarity']
            setName = JSON['data'][Counter]['set_name']
            setCode = JSON['data'][Counter]['set']
            setAPI = "https://api.scryfall.com/sets/" + setCode
            setResponse = requests.get(setAPI)
            setJSON = setResponse.json()
            setDate = setJSON['released_at']
            writer.writerow([CardName, cardColour, rarity, setName, setDate])

def main():
    pullList()


#This starts my program!
if __name__ == "__main__":
    main()
