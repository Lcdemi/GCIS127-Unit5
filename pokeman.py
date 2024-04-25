import csv
import random

def make_database(filename):
    pokemon_cards = [] #list to store all 102 pokemon cards
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for record in csv_reader:
            pokemon_card = (record[1], record[0], record[2])
            pokemon_cards.append(pokemon_card)
    return pokemon_cards

def make_pack(database):
    pack = set()
    while len(pack) < 10:
        pack.add(database[random.randrange(0, len(database))])
    return pack

def build_basic_collection(database):
    pack_counter = 0
    current_pokemon_cards = set()
    while len(current_pokemon_cards) < 102:
        pack = make_pack(database)
        pack_counter += 1
        for cards in pack:
            current_pokemon_cards.add(cards)
    return pack_counter

def build_counting_collection(database):
    collection = dict() #dictionary for all cards including duplicates
    card_counter = 0
    while len(collection) < len(database):
        new_pack = make_pack(database)
        for cards in new_pack:
            card_counter += 1
            if cards not in collection:
                collection[cards] = 1
            else:
                collection[cards] += 1

    sorted_collection = dict()
    counter = 1
    while len(sorted_collection) < len(collection): #sorts the collection by index value
        for key, value in collection.items():
            if int(key[0]) == counter:
                sorted_collection[key] = value
                counter += 1
                break

    return sorted_collection, card_counter

def find_most_card(collection):
    max = 0
    max_card = None
    for card in collection:
        if collection[card] > max:
            max = collection[card]
            max_card = card
    return max_card, max

def main():
    database = make_database("data/pokemon_cards.csv")
    print("Cards in database:", len(database)) #cards in database
    print("Cards in pack:") #cards in one pack
    pack = make_pack(database)
    for card in pack:
        print(card)
    #print(build_basic_collection(database))
    total_packs = 0
    for _ in range(0, 1000):
        total_packs += build_basic_collection(database)
    print("Average packs purchased to complete set:", total_packs / 1000) #average packs to complete set
    print("Cards purchased to complete set:") #all cards purchased
    sorted_collection, total_cards = build_counting_collection(database)
    for cards in sorted_collection:
        print(cards, ":", sorted_collection[cards])
    card_info, max_value = find_most_card(sorted_collection)
    print("Most:", card_info, "=", max_value) #most amount of a singular card bought
    print("Total:", total_cards) #prints total amount of cards purchased

if __name__ == "__main__":
    main()