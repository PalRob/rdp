input_str = '*l1J?)yn%R[}9~1"=k7]9;0[$'

def rec_char(input_str):
    chars = []
    for c in input_str:
        if c not in chars:
            chars.append(c)
        else:
            return c
    else:
        return None

print(rec_char(input_str))