from operator import le, ge, eq, lt, gt
from itertools import combinations

def parse_input(input_str):
    """Parse input string.
    Args:
        input_str (str): string in form:
            "Input: [required_number] [given_coins]
            Output: [comparison_clause]"
    Returns:
        (tuple): (change_data, comparison),
            where change_data is a list of integers, first of which
            is target number and the other ones are coins at hand and
            comparison is a tuple in form
            (comparison_function, (None as placeholder, number_to_compare))
    """

    input_str = input_str.split('\n')
    change_data = num_of_coins = None

    for i in input_str:
        if 'Input' in i:
            change_data = i[i.index(':')+1:].strip().split(" ")
            change_data = [int(x) for x in change_data]
        if 'Output' in i:
            num_of_coins = i[i.index(':')+1:].strip()
            operators = {'<=': le, '>=': ge, '=': eq, '<': lt, '>': gt}
            _, sign, value = num_of_coins.split()
            comparison = (operators[sign], (None, int(value)))

    return (change_data, comparison)

def get_change(input_str, compare=True):
    """Get all possible unique combinations of spare change.
    Args:
        input_str (str): string in form:
            "Input: [required_number] [given_coins]
            Output: [comparison_clause]"
        compare (bool): if True comparison clause
    Returns:
        suitable_sums (list): list of suitable sums, empty of none
    """
    change_data, comparison_clause = parse_input(input_str)
    target, coins = change_data[0], change_data[1:]

    possible_summs = []
    num_of_coins = len(coins)
    for r in range(1, num_of_coins+1):
        combos = combinations(coins, r)
        for c in combos:
            if sum(c) == target:
                c = sorted(c, reverse=True)
                # Converted to tuple to allow duplicate removal using set()
                c = tuple(c)
                possible_summs.append(c)
    # Removing duplicates
    possible_summs = list(set(possible_summs))
    # Checking number of coins in change clause if compare is True
    if compare:
        suitable_sums = []
        comparison, num1, num2 = comparison_clause[0], *comparison_clause[1]
        for change in possible_summs:
            num1 = len(change)
            if comparison(num1, num2):
                suitable_sums.append(change)
    else:
        suitable_sums = possible_summs

    return suitable_sums

def min_num_of_coins(input_str):
    """Calculates minimal number of coins that add up to given in
    input_str number.
    Args:
        input_str (str)
    Returns:
        min_coins (int): munimal number of coins or None
    """
    possible_summs = get_change(input_str, compare=False)
    if possible_summs:
        min_coins = min([len(i) for i in possible_summs])
    else:
        min_coins = None
    return min_coins

if __name__ == '__main__':
    # Four input_n output all possible unique combinations of
    # coins that add up to given number and satisfy
    # comparison clause given in the "Output"
    input_1 = """Input: 10 5 5 2 2 1
    Output: n <= 3"""

    input_2 = """Input: 150 100 50 50 50 50
    Output: n < 5"""

    input_3 = """Input: 130 100 20 18 12 5 5
    Output: n < 6"""

    input_4 = """Input: 200 50 50 20 20 10
    Output: n >= 5"""

    # For bonus_input_n output minimal nimber of coins
    # that add up to given number
    # Changed 2 and 3 to n = 2 and n = 3
    bonus_input_1 = """Input: 150 100 50 50 50 50
    Output: n = 2"""
    bonus_input_2 = """Input: 130 100 20 18 12 5 5
    Output: n = 3"""

    # rdp challenge
    # Changed 150 to n = 150
    challenge_change = ' '.join(['1']*10000)
    challenge_input = """Input: 150 {}\n
    Output: n = 150""".format(challenge_change)

    print('input_1:', get_change(input_1))
    print('input_2:', get_change(input_2))
    print('input_3:', get_change(input_3))
    print('input_4:', get_change(input_4))

    print('bonus_input_1:', min_num_of_coins(bonus_input_1))
    print('bonus_input_2:', min_num_of_coins(bonus_input_2))

    # Subset sum problem is an NP problem. It is impossible to brute force
    # the solution in a reasonable amount of time.
    # print('challenge_input:', get_change(challenge_input))
