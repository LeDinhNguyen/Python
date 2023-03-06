def countOccurrence(string: str) -> list:
    occ_list = []
    word_list = []
    string_list = string.split(" ")

    for s in string_list:
        if s not in word_list:
            word_list.append(s)

    for i in range(len(word_list)):
        count = 0
        for s in string_list:
            if s == word_list[i]:
                count += 1
        occ_list.append(count)

    for i in range(len(word_list)):
        print(word_list[i] + ":", occ_list[i])


    return occ_list

countOccurrence("I am a stupid student cuz stupid")