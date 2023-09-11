def main():
    str1 = input("Input: ")
    str1 = del_vowel(str1)

    for element in str1:
        print(element, end="")


def del_vowel(str1):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    for element in vowels:
        str1 = str1.replace(element,"")
    return str1


if __name__ == "__main__":
    main()
