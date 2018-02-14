def pins_knocked_in_frame(frame):
    """Get number of knocked pins in given frame
    Args:
        frame(str): string containing information about throws
            in the frame formatted by "bowling rules"
    Returns:
        pins_knocked(int): number of knocked pins in given frame
    """
    pins_knocked = 0
    for i, throw in enumerate(frame):
        if throw.isnumeric():
            pins_knocked += int(throw)
        elif throw == "X":
            pins_knocked += 10
        elif throw == "-":
            pins_knocked += 0
        elif throw == r"/":
            pins_knocked += 10 - pins_knocked_in_frame(frame[i-1])
    return pins_knocked

def get_score_table(throws):
    """Creates a string formatted by "bowling rules" from given string.
    Args:
        throws(str): string conteining number of knocked pins in every throw
    Retuns:
        formatted_table(str): string formatted by "bowling rules". Every
        frame is 3 characters long (including spaces).
    """
    table = []
    frame = ""
    frame_num = 1

    throws = [int(x) for x in throws.split()]

    for throw in throws:
        if throw == 10:
            if frame_num != 10:
                frame = "X"
                table.append(frame)

                frame = ""
                frame_num += 1
            else:
                frame += "X"
        else:
            if throw == 0:
                frame += "-"
            elif pins_knocked_in_frame(frame) + throw == 10:
                frame += r'/'
            else:
                frame += str(throw)

            if frame_num != 10 and len(frame) == 2:
                table.append(frame)

                frame = ""
                frame_num += 1
    else:
        # here throws from the last frame added to the table
        # this will always be executed since "for" loop
        # has no "break" statement
        table.append(frame)

    # with str.ljust(3) all scores will be nicely aligned
    formatted_table = "".join([x.ljust(3) for x in table])
    return formatted_table

if __name__ == "__main__":
    bowling_games = """6 4 5 3 10 10 8 1 8 0 10 6 3 7 3 5 3
    9  0  9  0  9  0  9  0  9  0  9  0  9  0  9  0  9  0  9  0
    10 10 10 10 10 10 10 10 10 10 10 10
    5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5
    10 3  7  6  1  10 10 10 2  8  9  0  7  3  10 10 10
    9  0  3  7  6  1  3  7  8  1  5  5  0  10 8  0  7  3  8  2  8"""

    bowling_games = bowling_games.split("\n")
    for game in bowling_games:
        print(get_score_table(game))
