from collections import Counter

def get_substrings(input_str):
    """Get all substrings of len 2 or more of given string."""
    substrings = []
    for j in range(1, len(input_str)):
        for i in range(j):
            substrings.append(input_str[i:j+1])
    return substrings


def get_repetitions(input_str):
    """Count all repeting patterns of 2 or more characters in given string.
    """
    # TODO: What if input_str is 2 characters or less?
    substrings = get_substrings(input_str)
    repetitions = Counter(substrings)
    keys = list(repetitions.keys())
    for k in keys:
        if repetitions[k] < 2:
            del repetitions[k]
    return repetitions


if __name__ == '__main__':
    num_1 = "11325992321982432123259"
    repetitions = get_repetitions(num_1)
    if not repetitions:
        print(0)
    else:
        for i in repetitions:
            print("%s: %d" % (i, repetitions[i]))
