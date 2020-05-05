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


##############################################################
if __name__ == "__main__":
    # execute only if run as a script
    main()

    # run as such: ~ / src / effectivepython[master *] python3 chapter_1.py
