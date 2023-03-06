def hexToDecimal(string: str) -> str:
    hex_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    dec = 0
    n = len(string)
    for s in string:
        if s not in hex_list:
            return "ERROR"
        else:
            dec += hex_list.index(s) * (16 ** (n - 1))
            n -= 1
    return str(dec)

print(hexToDecimal("76A"))
