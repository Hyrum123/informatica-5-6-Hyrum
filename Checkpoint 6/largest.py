def main():
    numbers = input("Enter a list of numbers seperated by a comma: ").replace(" ", "").split(",")
    name = input("Enter a file name: ")
    print(numbers)
    write_numbers(numbers, name)
    list = read_numbers(name)
    print(list)


def write_numbers(num_list, filename):
    with open(f"{filename}.txt", "a") as file:
        for num in list(num_list):
            file.write(f"{num}\n")

def read_numbers(filename):
    with open(f"{filename}.txt", "r") as file:
        for line in list(file.readlines()):
            returnable_list = []
            returnable_list.append(line.rstrip())
        return returnable_list
    

main()