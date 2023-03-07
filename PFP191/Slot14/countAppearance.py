def countAppearance(string: str) -> dict:
    name_dict = {}
    name_list = string.split("/")
    for name in name_list:
        if name not in name_dict.keys():
            name_dict[name] = 1
        else:
            name_dict[name] += 1
    return name_dict


print(max(countAppearance("nguyen/duong/nguyen/duong/nguyen")))
