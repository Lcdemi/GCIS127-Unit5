import random

def swap_sort(a_list):
    Swapped = True
    while Swapped == True:
        Swapped = False
        for i in range(1, len(a_list)):
            if a_list[i] < a_list[i-1]:
                temp = a_list[i]
                a_list[i] = a_list[i-1]
                a_list[i-1] = temp
                Swapped = True
    return a_list

def what_does_the_fox_say(a_func):
    sound = a_func()
    print("The Fox says " + sound)

def oof():
    return "oof"

def ouchie():
    return "ouchie"

def make_tuple(a, b, c):
    return (a, b, c)

def reverse_tuple(sequence):
    new_tuple = sequence[::-1]
    return new_tuple

def make_trading_card(name, mana_value, power, toughness):
    return (name, mana_value, power, toughness)

def trading_card_value(trading_card_tuple):
    return trading_card_tuple[2] + trading_card_tuple[3]

def trading_card_sort_key(trading_card_tuple):
    return trading_card_value(trading_card_tuple)

def make_list(a, b, c):
    return [a, b, c]

def nth_list(sequence, n):
    new_list = [sequence[i] for i in range(0, len(sequence), n)]
    return new_list

def odds_before_evens(a_list):
    odds_list = [a_list[i] for i in range(len(a_list)) if a_list[i] % 2 == 1]
    #print(odds_list)
    evens_list = [a_list[i] for i in range(len(a_list)) if a_list[i] % 2 == 0]
    #print(evens_list)
    a_list[:] = odds_list + evens_list
    #print(a_list)

def splice(a_list, b_list):
    a_list += b_list

def scramble(a_string):
    new_list = []
    for i in range(len(a_string)):
        new_list.append(a_string[i:i+1])
    print(new_list)
    print(new_list[::-1])

def fizz_buzz_list():
    new_list = [x for x in range(1, 101) if x % 3 == 0 or x % 5 == 0]
    return new_list

def multiples(sequence, n):
    new_list = [x for x in sequence if x % n == 0]
    return new_list

def only_vowels(a_string):
    vowels = "AEIOUaeiou"
    new_list = [char for char in a_string if char in vowels]
    return new_list

def random_search(a_list, target):
    while len(a_list) > 0:
        randomIndex = random.randrange(len(a_list))
        randomValue = a_list[randomIndex]
        if randomValue == target:
            return randomIndex
        else:
            a_list.pop(randomIndex)
    return None

def equivalent(sequenceA, sequenceB):
    dictA = dict()
    dictB = dict()

    for element in sequenceA:
        if element not in dictA:
            dictA[element] = 0
        dictA[element] += 1

    for element in sequenceB:
        if element not in dictB:
            dictB[element] = 0
        dictB[element] += 1

    return dictB == dictA

def disjoint(setA, setB):
    for element in setA:
        if element in setB:
            return True
    return False

def union(setA, setB):
    new_set = set()
    for element in setA:
        new_set.add(element)
    for element in setB:
        new_set.add(element)
    return new_set

def random_counts(n):
    new_dict = dict()
    total_calls = 0
    while len(new_dict) < n + 1:
        randomValue = random.randint(0, n)
        if randomValue not in new_dict:
            new_dict[randomValue] = 0
        new_dict[randomValue] += 1
        total_calls += 1
    return new_dict, total_calls

def frequencies(counts):
    frequency_dict = {}
    unique_values = {}

    for value, count in counts.items():
        if count in frequency_dict:
            frequency_dict[count] += 1
        else:
            frequency_dict[count] = 1

        if count in unique_values:
            unique_values[count].append(value)
        else:
            unique_values[count] = [value]

    for count, frequency in sorted(frequency_dict.items()):
        print(count, frequency)

    max_count = max(frequency_dict)
    most_common_values = unique_values[max_count]

    return most_common_values, max_count

def cereal_box_decoder(comma_string):
    decoded_message = ""
    ascii_list = [int(val) for val in comma_string.split(",")]
    for element in ascii_list:
        decoded_message += chr(element)
    return decoded_message

def cereal_box_encoder(String):
    encoded_message = ""
    for char in String:
        encoded_message += str(ord(char)) + ", "
    return encoded_message[:-2]

def find_hash_collisions(a_list, b_list):
    collisions = set()
    hash_set = set()

    for value in a_list:
        hash_value = hash(value)
        if hash_value in hash_set:
            collisions.add(value)
        else:
            hash_set.add(hash_value)

    for value in b_list:
        hash_value = hash(value)
        if hash_value in hash_set:
            collisions.add(value)
        else:
            hash_set.add(hash_value)

    return list(collisions)

def main():
    a_list = [5, 8, 9, 4, 2, 1, 10, 7]
    b_list = [1, 2, 3]
    c_list = [3, 2, 1]
    #print(swap_sort(a_list))
    #what_does_the_fox_say(oof)
    #what_does_the_fox_say(ouchie)
    #print(make_tuple(1, 2, 3))
    #print(make_tuple(3, 2, 1))
    #print(reverse_tuple([1, 2, 3, 4]))
    #print(reverse_tuple("abcdefg"))
    # Borborygmos = make_trading_card("Borborygmos", "3RRGG", 6, 7)
    # Shivan_Dragon = make_trading_card("Shivan Dragon", "4RR", 5, 5)
    # Dragoon = make_trading_card("Dragooon", "6GG", 9, 7)
    # Barbarian = make_trading_card("Barbarian", "9BBLL", 3, 4)
    # Archer = make_trading_card("Archer", "1LL", 6, 2)
    # print(make_trading_card("Borborygmos", "3RRGG", 6, 7))
    # print(make_trading_card("Shivan Dragon", "4RR", 5, 5))
    # print(make_trading_card("Dragooon", "6GG", 9, 7))
    # print(make_trading_card("Barbarian", "9BBLL", 3, 4))
    # print(make_trading_card("Archer", "1LL", 6, 2))
    # cards = [Borborygmos, Shivan_Dragon, Dragoon, Barbarian, Archer]
    # sorted_cards = sorted(cards, key=trading_card_sort_key)
    # print(sorted_cards)
    #print(make_list(1, 2, 3))
    #print(make_list(3, 2, 1))
    #print(nth_list(range(1, 11), 2))
    #print(nth_list([1, 2, 3, 4, 5, 6], 3))
    #print(nth_list("abcdefghijk", 4))
    #odds_before_evens(a_list)
    #splice(a_list, b_list)
    #print(a_list)
    #scramble("Joe Biven")
    #print(fizz_buzz_list())
    #print(multiples(a_list, 2))
    #print(only_vowels("joe biven got nothing on me"))
    #print(random_search(a_list, 5))
    #print(equivalent(b_list, c_list))
    # a_set = {1, 2, 3}
    # b_set = {4, 5, 6}
    # c_set = {1, 3, 5}
    # print(disjoint(a_set, b_set))
    # print(disjoint(a_set, c_set))
    # print(union(a_set, b_set))
    # print(union(a_set, c_set))
    # random.seed(7)
    # count_dict, total_calls = random_counts(10000)
    # print(total_calls)
    # most_common_values, max_count = frequencies(count_dict)
    # print(max_count)
    # print(sorted(most_common_values))
    # print(cereal_box_decoder("55, 89, 110, 90, 95"))
    # print(cereal_box_encoder("pizza pizza"))
    # list1 = ["apple", "banana", "cherry", "date", "elderberry"]
    # list2 = ["fig", "grape", "banana", "date", "apple"]
    # collision_values = find_hash_collisions(list1, list2)
    # print(collision_values)

if __name__ == "__main__":
    main()