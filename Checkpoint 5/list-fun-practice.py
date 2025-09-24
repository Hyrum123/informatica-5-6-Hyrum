def main():
    my_list = [1, 2, 3, 4, 5, 5, 5, 6, 7, 7]
    print(length(my_list))
    print(mean(my_list))
    print(range_of_list(my_list))


def length(lists):
    return len(list(lists))

def mean(lists):
    return sum(lists) / len(lists)

def range_of_list(lists):
    return max(lists) - min(lists)

def enter():
    while True: 
        lists = []


main()