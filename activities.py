import timing
import random

def apply_transformation(a_list, transform_function):
    copy = []
    for element in a_list:
        copy.append(transform_function(element))
    return copy

def square(x):
    return x ** 2

def double(x):
    return x * 2

def negate(x):
    return x * -1

def unique_list(a_list, value):
    if value in a_list:
        return
    a_list.append(value)

def fill_list(length):
    a_list = []
    for i in range(length):
        unique_list(a_list, i)
    return a_list

def sets():
    a_set = {1, 7, 3, 4}
    print(a_set)
    a_set.add(7)
    a_set.add(10)
    a_set.add("A")
    a_set.add(12)
    print(a_set)

    b_set = set("joe biven")
    print(b_set)

def unique_set(a_set, value):
    if value not in a_set:
        a_set.add(value)

def fill_set(length):
    a_set = set()
    for i in range(length):
        unique_set(a_set, i)
    return a_set

def coupon_collector(n):
    total_coupons = 0
    coupon_set = set()
    while len(coupon_set) < n:
        coupon = random.randint(1, n)
        total_coupons += 1
        if coupon not in coupon_set:
            coupon_set.add(coupon)
    return total_coupons

def mixup():
    new_set = set("I am Joe Biven")
    for i in new_set:
        print(i, end=" ")
    print()

def unique_words(filename):
    unique_word_set = set()
    with open(filename) as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower()
                unique_word_set.add(word)
        return unique_word_set

def superset(a_set, b_set):
    if len(a_set) <= len(b_set):
        return False
    else:
        for element in b_set:
            if element in a_set:
                continue
            return False
        return True
    
def subset(a_set, b_set):
    if len(a_set) >= len(b_set):
        return False
    else:
        for element in a_set:
            if element in b_set:
                continue
            return False
        return True
    
def intersection(a_set, b_set):
    c_set = set()
    for element in a_set:
        if element in b_set:
            c_set.add(element)
    return c_set

def union(a_set, b_set):
    c_set = set()
    for element in a_set:
        c_set.add(element)
    for element in b_set:
        c_set.add(element)
    return c_set

def minus(a_set, b_set):
    to_remove = []
    for element in a_set:
        if element in b_set:
            to_remove.append(element)
    for element in to_remove:
        a_set.remove(element)

def names():
    dictionary = dict()
    dictionary = {"L":"Luke", "C":"Christian", "D":"Demi", "K":"Kyle", "J":"Jonathan", "D":"Demi", "N":"Natalie", "L":"Lauren", "D":"Demi"}
    print(dictionary["L"])
    print(dictionary["K"])
    print(dictionary["N"])

def print_dict(dictionary):
    for key in dictionary:
        value = dictionary[key]
        print(key, "=", value)

def find_maximum(dictionary):
    max_key = None
    max_value = None
    for key in dictionary:
        value = dictionary[key]
        if max_key is None:
            max_key = key
            max_value = value
        elif value > max_value:
            max_key = key
            max_value = value
    return max_key, max_value

def count_words(filename):
    a_dict = dict()
    with open(filename) as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower()
                if word not in a_dict:
                    a_dict[word] = 0
                a_dict[word] += 1
    return a_dict

def hashes():
    string1 = "Hello World!"
    string2 = "Hello world!"
    long_string = "A" * 100000
    longer_string = "A" * 1000000000
    print(hash(string1))
    print(hash(string2))
    print(hash(long_string))
    print(hash(longer_string))
    print("False =", hash(False))
    print("123 =", hash(123))
    print("1.234 =", hash(1.234))
    #lists cannot be hashed

def collisions(filename, length, hash_func=hash):
    a_list = [None for _ in range(length)]
    count = 0
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if len(line) == 0:
                continue
            line_hash = hash_func(line)
            index = line_hash % length
            if a_list[index] is None:
                a_list[index] = line
                count += 1
            elif a_list[index] == line:
                continue
            else:
                return count, a_list
def main():
    #a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #print(apply_transformation(a_list, square))
    #print(apply_transformation(a_list, double))
    #print(apply_transformation(a_list, negate))
    #print(coupon_collector(10000))
    #timing.time_function(fill_list, 10000)
    #timing.time_function(fill_list, 15000)
    #timing.time_function(fill_set, 500000)
    #timing.time_function(fill_set, 1000000)
    #timing.time_function(fill_set, 1500000)
    #sets()
    #sets()
    #sets()
    #mixup()
    #mixup()
    #mixup()
    #print(len(unique_words("data/alice.txt")))
    #a_set = {1, 2, 3, 4, 5}
    #b_set = {1, 2, 3}
    #print(superset(a_set, b_set))
    #print(superset(b_set, a_set))
    #print(subset(a_set, b_set))
    #print(subset(b_set, a_set))
    #print(intersection(a_set, b_set))
    #print(union(a_set, b_set))
    #minus(a_set, b_set)
    #print(a_set)
    #names()
    #important_dictionary = {}
    #important_dictionary["Luke"] = "Skywalker"
    #important_dictionary["Leia"] = "Organa"
    #important_dictionary["Lando"] = "Calrissian"
    #print_dict(important_dictionary)
    # a_dict = dict()
    # a_dict["a"] = -1
    # a_dict["b"] = -2
    # a_dict["c"] = 0
    # a_dict["d"] = 1
    # a_dict["e"] = 2
    # print(find_maximum(a_dict))
    counts = count_words("data/alice.txt")
    print(counts)
    print(find_maximum(counts))
    #hashes()
    #print("Collisions:", collisions("data/alice.txt", 10))

if __name__ == "__main__":
    main()