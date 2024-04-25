def gcis_sort(a_list):
    for value in range(len(a_list)):
        for index in range(0, (len(a_list) - 1 - value)):
            sorted = True
            if a_list[index] > a_list[index+1]:
               temp = a_list[index+1]
               a_list[index+1] = a_list[index]
               a_list[index] = temp
               sorted = False
        if sorted == True:
           break
    return a_list

def in_place_reverse(a_list):
    '''
    The time complexity of this function is O(n^2)
    '''
    for i in range(len(a_list)):
        a_list.insert(i, a_list.pop())
    return a_list

def make_multiplication_table():
    return [[i * j for j in range(1, 11)] for i in range(1, 11)]

def main():
    a_list = [5, 4, 3, 2, 1]
    print(a_list)
    print(gcis_sort(a_list))
    print(in_place_reverse(a_list))
    for row in make_multiplication_table():
        print(row)

if __name__ == "__main__":
    main()