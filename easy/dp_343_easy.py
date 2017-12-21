notes_chromatic = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

solfege = {'Do': 0, 'Re': 2, 'Mi': 4, 'Fa': 5, 'So': 7, 'La':9, 'Ti': 11}

def get_note(note_chrom, solfege_name):
    i = notes_chromatic.index(note_chrom)
    note_index = (i + solfege[solfege_name]) % len(notes_chromatic)
    note = notes_chromatic[note_index]
    return note

print(get_note('C', 'Do'))
print(get_note('C', 'Re'))
print(get_note('C', 'Mi'))
print(get_note('D', 'Mi'))
print(get_note('A#', 'Re'))
