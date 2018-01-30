def have_odd_zeros(num):
    """
    Returns True if binary representation of a num contains block of
    consecutive 0s of odd length. False otherwise."""
    # [2:] to slice out starting 0b from a binary number
    bin_num = bin(num)[2:]
    odd_zeros = False
    num_of_zeros = 0
    for i in bin_num:
        if i == '0':
            num_of_zeros += 1
        elif i == '1':
            if num_of_zeros % 2 != 0:
                odd_zeros = True
                break
            else:
                num_of_zeros = 0

    else:
        if num_of_zeros % 2 != 0:
            odd_zeros = True

    return odd_zeros

def get_baum_sweet_sequence(num):
    """Generates Baum-Sweet sequence from 0 to num. Returns list of
    integer 0s and 1s with len(num)."""
    baum_sweet_sequence = []
    for i in range(num):
        if have_odd_zeros(i):
            baum_sweet_sequence.append(1)
        else:
            baum_sweet_sequence.append(0)
    return baum_sweet_sequence

print(get_baum_sweet_sequence(20))
