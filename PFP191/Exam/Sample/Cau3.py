def bow(num: int):
    nextToMid = int((num - 1) / 2)
    for i in range(1, nextToMid + 1):
        for j in range(0, i):
            print("* ", end="")
        for j in range(0, num - 2 * i):
            print("  ", end="")
        for j in range(0, i):
            print("* ", end="\n")
            print("")


def main():
    bow(9)


if __name__ == "__main__":
    main()
