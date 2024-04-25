def make_myset(length, hash_func=hash):
    return (hash_func, [[] for _ in range(length)])

def add(element, myset):
    hash_func = myset[0]
    table = myset[1]

    hash_code = hash_func(element)

    index = hash_code % len(table)
    chain = table[index]
    if element not in chain:
        chain.append(element)

def contains(myset, element):
    hash_func = myset[0]
    table = myset[1]

    hash_code = hash_func(element)

    index = hash_code % len(table)
    chain = table[index]

    return element in chain

def main():
    #print(make_myset(100))
    myset = make_myset(7)
    add("abc", myset)
    add(123, myset)
    add(False, myset)
    add("abc", myset)
    print(myset)
    print(contains(myset, "abc"))
    print(contains(myset, 123))
    print(contains(myset, False))
    print(contains(myset, "def"))

if __name__ == "__main__":
    main()