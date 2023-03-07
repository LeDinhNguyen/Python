def convertDictionary(dictionary: dict) -> dict:
    converted_dict = {}

    for item in dictionary:
        if dictionary[item] not in converted_dict:
            converted_dict[dictionary[item]] = [item]
        else:
            converted_dict[dictionary[item]].append(item)

    return converted_dict


a = {"john": 4, "Johnny": 4, "jackie": 2, "jamie": 3}
print(convertDictionary(a))
