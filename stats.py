def word_counter(text):
    words = text.split()
    return len(words)


def charakter_counter(text):
    new_text = text.lower()
    charakters = list(new_text)
    counter = {}
    
    for charakter in charakters:
        if charakter in counter:
            counter[charakter] += 1
        else:
            counter[charakter] = 1
    return counter


def sort_on(items):
    return items["num"]


def sorting_charakters(charakters):

    list = []
    for key in charakters:
        temp = {}
        temp["char"] = key
        temp["num"] = charakters[key]
        list.append(temp)
    list.sort(reverse = True, key = sort_on)
    return list