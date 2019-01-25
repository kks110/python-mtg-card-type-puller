#Used for processing JSONS files
import json
#Used to get the URL
import requests
#Used to export the data to a CSV
import csv


#This writes the file.
def write_file(creature_input, card_data, set_count, first_row = False):
    with open('mtg_' + creature_input + '.csv', 'a', newline='', encoding='utf8') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        if first_row:
            writer.writerow(["Card Name", "Card colour", "Rarity", "Set Name", "Set Date"])
        for x in range(set_count):
            #Prints the data out on screen and also puts it in to the CSV file
            card_name = card_data['data'][x]['name']
            card_colour = card_data['data'][x]['color_identity']
            rarity = card_data['data'][x]['rarity']
            set_name = card_data['data'][x]['set_name']
            set_code = card_data['data'][x]['set']
            set_api = "https://api.scryfall.com/sets/" + set_code
            set_response = requests.get(set_api)
            set_json = set_response.json()
            set_date = set_json['released_at']
            writer.writerow([card_name, card_colour, rarity, set_name, set_date])

def pullList():
    card_counter = 0
    card_input = input("What type of card are you looking for? - ")
    #API call to get the JSON file
    api = "https://api.scryfall.com/cards/search?q=t:" + card_input
    response = requests.get(api)
    card_data = response.json()
    total_cards = card_data['total_cards']
    #Counts the amount of cards in the set
    set_count = len(card_data['data'])
    write_file(card_input, card_data, set_count, True)
    card_counter += set_count
    #If there are more than 175 cards, code to get the second half. The JSONs only contain info for the first 175 cards
    while card_counter < total_cards:
        continued = card_data['next_page']
        response_cont = requests.get(continued)
        card_data = response_cont.json()
        set_count = (len(card_data['data']))
        write_file(card_input, card_data, set_count)
        card_counter += set_count

def main():
    pullList()


#This starts my program!
if __name__ == "__main__":
    main()
