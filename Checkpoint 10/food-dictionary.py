def count(fruits):
    fruit_dictionary = {}

    for item in fruits:
        if item in fruit_dictionary:
            fruit_dictionary[item] += 1
        else:
            fruit_dictionary.setdefault(item, 1)

    print(fruit_dictionary)

word_list = [
"banana", "milk", "soda", "cheese", "sourmilk", "juice", "sausage",
"tomato", "cucumber", "butter", "margarine", "cheese", "sausage",
"soda", "sourmilk", "sourmilk", "butter", "soda", "chocolate"
]

count(word_list)

