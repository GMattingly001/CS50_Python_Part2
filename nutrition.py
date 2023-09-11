def main():
    # fruits = [
    #     {"fruit": "apple", "calories": "130"},
    #     {"fruit": "banana", "calories": "110"},
    #     {"fruit": "avocado", "calories": "50"},
    #     {"fruit": "cantaloupe", "calories": "50"},
    #     {"fruit": "grapefruit", "calories": "60"},
    #     {"fruit": "grapes", "calories": "90"},
    #     {"fruit": "honeydew", "calories": "50"},
    #     {"fruit": "kiwifruit", "calories": "90"},
    #     {"fruit": "lemon", "calories": "15"},
    #     {"fruit": "lime", "calories": "20"},
    #     {"fruit": "nectarine", "calories": "60"},
    #     {"fruit": "orange", "calories": "80"},
    #     {"fruit": "peach", "calories": "60"},
    #     {"fruit": "pear", "calories": "100"},
    #     {"fruit": "pineapple", "calories": "50"},
    #     {"fruit": "plums", "calories": "70"},
    #     {"fruit": "strawberries", "calories": "50"},
    #     {"fruit": "sweet cherries", "calories": "100"},
    #     {"fruit": "tangerine", "calories": "50"},
    #     {"fruit": "watermelon", "calories": "80"},
    # ]

    fruits = \
        {
            "apple": "130",
            "banana": "110",
            "avocado": "50",
            "cantaloupe": "50",
            "grapefruit": "60",
            "grapes": "90",
            "honeydew": "50",
            "kiwifruit": "90",
            "lemon": "15",
            "lime": "20",
            "nectarine": "60",
            "orange": "80",
            "peach": "60",
            "pear": "100",
            "pineapple": "50",
            "plums": "70",
            "strawberries": "50",
            "sweet cherries": "100",
            "tangerine": "50",
            "watermelon": "80",
        }

    s = input("Item: ").lower().strip()
    if s in fruits:
        print("Calories: " + fruits[s])

    # Make a table of all fruits with calories
    # print('{0:^14} {1:<1} {2:^13}'.format("Fruit", "|", "Calories"))
    # print("-" * 30)
    # for fruit in fruits:
    #     print('{0:^14} {1:<1} {2:^13}'.format(fruit["fruit"], "|", fruit["calories"]))
    #     print("-" * 30)

    # for fruit in fruits:
    #     if s == fruit['fruit']:
    #         print(fruit['calories'])
    #         break


main()
