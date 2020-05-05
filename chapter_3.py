def main():

    # Item 19: Never Unpack More Than Three Variables When Functions Return Multiple Values
    def get_stats(numbers):
        minimum = min(numbers)
        maximum = max(numbers)
        return minimum, maximum

    lengths = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]

    minimum, maximum = get_stats(lengths)  # Two return values

    print(f'Min: {minimum}, Max: {maximum}')

    # >>> Min: 60, Max: 73

    # catch-all unpacking
    def get_avg_ratio(numbers):
        average = sum(numbers) / len(numbers)
        scaled = [x / average for x in numbers]
        scaled.sort(reverse=True)
        return scaled

    longest, *middle, shortest = get_avg_ratio(lengths) # catch-all starred expression

    print(f'Longest: {longest:>4.0%}')
    print(f'Shortest: {shortest:>4.0%}')

    # >>>
    # Longest: 108 %
    # Shortest: 89 %

    # Item 20: Prefer Raising Exceptions to Returning None
    def careful_divide(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return None

    x, y = 5, 2
    try:
        result = careful_divide(x, y)
    except ValueError:
        print('Invalid inputs')
    else:
        print('Result is %.1f' % result)

    # >>> Result is 2.5

    # Item 21: Know How Closures Interact with Variable Scope
    def sort_priority(values, group):
        def helper(x):
            if x in group: # closure function
                return (0, x)
            return (1, x)

        values.sort(key=helper) # sort method accepts helper (a closure function) as the key argument

    numbers = [8, 3, 1, 2, 5, 4, 7, 6]
    group = {2, 3, 5, 7}
    sort_priority(numbers, group)
    print(numbers)

    # >>> [2, 3, 5, 7, 1, 4, 6, 8]

    # Scope demonstration
    def sort_priority2(numbers, group):
        found = False # Scope: 'sort_priority2'

        def helper(x):
            if x in group:
                found = True  # new variable, not a reassignment as expected; scope: 'helper'
                return (0, x)
            return (1, x)

        numbers.sort(key=helper)
        return found

    found = sort_priority2(numbers, group)
    print('Found:', found)
    print(numbers)

    # >>> Found: False
    # [2, 3, 5, 7, 1, 4, 6, 8]  # hoped for True, but did not get it due to scope
    # found trapped in helper function in which it was defined (scope: helper)

    # using nonlocal statement
    def sort_priority3(numbers, group):
        found = False

        def helper(x):
            nonlocal found  # Added nonlocal statement
            if x in group:
                found = True
                return (0, x)
            return (1, x)

        numbers.sort(key=helper)
        return found

    #Better: wrap state in helper class when nonlocal gets complicated
    class Sorter:
        def __init__(self, group):
            self.group = group
            self.found = False

        def __call__(self, x):
            if x in self.group:
                self.found = True
                return (0, x)

        return (1, x) # parantheses are redundant, can be removed

    sorter = Sorter(group)
    numbers.sort(key=sorter)
    assert sorter.found is True


##############################################################
if __name__ == "__main__":
    # execute only if run as a script
    main()

    # run as such: ~ / src / effectivepython[master *] python3 chapter_1.py
