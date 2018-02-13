def read_frame(frame):
    pins_knocked = 0
    for i, throw in enumerate(frame):
        if throw.isnumeric():
            pins_knocked += int(throw)
        elif throw == "X":
            pins_knocked += 10
        elif throw == "-":
            pins_knocked += 0
        elif throw == r"/":
            pins_knocked += 10 - read_frame(frame[i-1])
    return pins_knocked
def get_frames(throws):
    table = []
    frame = None
    frame_num = 1

    throws = [int(x) for x in throws.split()]

    for throw in throws:
        if throw == 10:
            if not frame_num == 10:
                frame = "X"
                table.append(frame)
                frame = None
                frame_num += 1
            else:
                if frame:
                    frame += "X"
                else:
                    frame = "X"
        elif not frame:
            if throw == 0:
                frame = "-"
            else:
                frame = str(throw)
        elif frame:
            if throw == 0:
                frame += "-"
            elif read_frame(frame) + throw == 10:
                frame += r'/'
            else:
                frame += str(throw)

            if not frame_num == 10:
                table.append(frame)
                frame = None
                frame_num += 1
    else:
        table.append(frame)
        frame = None

    table = "".join([x.ljust(3) for x in table])
    return table

if __name__ == "__main__":
    inputs = """6 4 5 3 10 10 8 1 8 0 10 6 3 7 3 5 3
    9  0  9  0  9  0  9  0  9  0  9  0  9  0  9  0  9  0  9  0
    10 10 10 10 10 10 10 10 10 10 10 10
    5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5
    10 3  7  6  1  10 10 10 2  8  9  0  7  3  10 10 10
    9  0  3  7  6  1  3  7  8  1  5  5  0  10 8  0  7  3  8  2  8"""

    inputs = inputs.split("\n")
    for i in inputs:
        print(get_frames(i))
