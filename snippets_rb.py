def main():
    # Item 6: Prefer Multiple Assignment Unpacking Over Indexing
    snack_calories = {
        'chips': 140,
        'popcorn': 80,
        'nuts': 190,
    }
    items = tuple(snack_calories.items())
    print(items)

    # >>> (('chips', 140), ('popcorn', 80), ('nuts', 190))

    # tuple unpacking
    item = ('Peanut butter', 'Jelly')
    first, second = item  # Unpacking
    print(first, 'and', second)

    # >>> Peanut butter and Jelly

    favorite_snacks = {
        'salty': ('pretzels', 100),
        'sweet': ('cookies', 180),
        'veggie': ('carrots', 20),
    }
    ((type1, (name1, cals1)),
     (type2, (name2, cals2)),
     (type3, (name3, cals3))) = favorite_snacks.items()

    print(f'Favorite {type1} is {name1} with {cals1} calories')
    print(f'Favorite {type2} is {name2} with {cals2} calories')
    print(f'Favorite {type3} is {name3} with {cals3} calories')

    # >>>
    # Favorite salty is pretzels with 100 calories
    # Favorite sweet is cookies with 180 calories
    # Favorite veggie is carrots with 20 calories

    # unpacking to Bubble sort
    def bubble_sort(a):
        for _ in range(len(a)):
            for i in range(1, len(a)):
                if a[i] < a[i - 1]:
                    a[i - 1], a[i] = a[i], a[i - 1]  # Swap

    names = ['pretzels', 'carrots', 'arugula', 'bacon']
    bubble_sort(names)
    print(names)

    # >>> ['arugula', 'bacon', 'carrots', 'pretzels']

##############################################################
if __name__ == "__main__":
    # execute only if run as a script
    main()

    # run as such: ~ / src / effectivepython[master *] python3 snippets_rb.py
