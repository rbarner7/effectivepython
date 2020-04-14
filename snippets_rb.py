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


    # Item 7: Prefer enumerate Over range
    # range
    from random import randint

    random_bits = 0
    for i in range(32):
        if randint(0, 1):
            random_bits |= 1 << i

    print(bin(random_bits))

    # >>> 0b11101000100100000111000010000001

    flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']

    for i in range(len(flavor_list)):
        flavor = flavor_list[i]
        print(f'{i + 1}: {flavor}')

    # >>>
    # 1: vanilla
    # 2: chocolate
    # 3: pecan
    # 4: strawberry

    # enumerate
    it = enumerate(flavor_list)
    print(next(it))
    print(next(it))

    # >>>
    # (0, 'vanilla')
    # (1, 'chocolate')

    for i, flavor in enumerate(flavor_list):
        print(f'{i + 1}: {flavor}')

    # >>>
    # 1: vanilla
    # 2: chocolate
    # 4: strawberry
    # 3: pecan

    # specify when to begin counting
    # ????
    for i, flavor in enumerate(flavor_list, 4):
        print(f'{i}: {flavor}')

    # >>>
    # 1: vanilla
    # 2: chocolate
    # 3: pecan
    # 4: strawberry

    # Item 8: Use zip to Process Iterators in Parallel
    # zip
    names = ['Cecilia', 'Lise', 'Marie']
    counts = [len(n) for n in names]
    print(counts)

    # >>> [7, 4, 5]

    longest_name = None
    max_count = 0

    for name, count in zip(names, counts):
        if count > max_count:
            longest_name = name
            max_count = count

    print(longest_name)

    # >>> Cecilia

    names.append('Rosalind')

    for name, count in zip(names, counts):
        print(name)

    # >>> # Does not return Rosalind since the output always as long as the shortest input list
    # Cecilia
    # Lisa
    # Marie

    # use itertools' zip_longest for lists of different lengths to cover lists of longer items; None is default
    import itertools
    for name, count in itertools.zip_longest(names, counts):
        print(f'{name}: {count}')

    # >>>
    # Cecilia: 7
    # Lise: 4
    # Marie: 5
    # Rosalind: None

    # Item 9: Avoid else Blocks After for and while Loops
    # break skips the else block
    for i in range(3):
        print('Loop', i)
        if i == 1:
            break

    else:
        print('Else block!')

    # >>>
    # Loop 0
    # Loop 1

    #
    # walrus operator
    fresh_fruit = {
        'apple': 10,
        'banana': 8,
        'lemon': 5,
    }

    def make_lemonade(lemons):
        print(f'Making lemonade from {lemons} lemons')

    def make_cider(apples):
        print(f'Making cider from {apples} apples')

    def slice_bananas(bananas):
        print(f'Slicing {bananas} bananas.')
        return bananas

    def make_smoothies(dranks):
        print(f'Making {dranks} smoothies.')

    def out_of_stock():
        print("we aint got no mo'!")

    # assign value to count variable, then evaluate value in the context of the if statement to determine how to proceed
    # w/flow control and non-0 check
    if count := fresh_fruit.get('lemon', 0):  # obvious that count is only relevant to the first statement
        make_lemonade(count)
    else:
        out_of_stock()

    if (count := fresh_fruit.get('apple', 0)) >= 4:  # parenthesis required
        make_cider(count)
    else:
        out_of_stock()

    pieces = 0
    if (count := fresh_fruit.get('banana', 0)) >= 2:
        pieces = slice_bananas(count)

    try:
        smoothies = make_smoothies(pieces)
    except OutOfBananas:
        out_of_stock()

    if (count := fresh_fruit.get('banana', 0)) >= 2:
        pieces = slice_bananas(count)
        to_enjoy = make_smoothies(pieces)
    elif (count := fresh_fruit.get('apple', 0)) >= 4:
        to_enjoy = make_cider(count)
    elif count := fresh_fruit.get('lemon', 0):
        to_enjoy = make_lemonade(count)
    else:
        to_enjoy = 'Nothing'

    print(to_enjoy)

    # loop-and-a-half idiom
    # what should this look like??

    bottles = []
    while True:  # Loop
        fresh_fruit = pick_fruit()
        if not fresh_fruit:  # And a half
            break

        for fruit, count in fresh_fruit.items():
            batch = make_juice(fruit, count)
            bottles.extend(batch)

    # walrus assignment statement version
    bottles = []
    while fresh_fruit := pick_fruit():
        for fruit, count in fresh_fruit.items():
            batch = make_juice(fruit, count)
            bottles.extend(batch)

##############################################################
if __name__ == "__main__":
    # execute only if run as a script
    main()

    # run as such: ~ / src / effectivepython[master *] python3 snippets_rb.py
