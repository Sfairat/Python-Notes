import creation

def create_note():
    array = []
    with open('notes.csv', 'r', encoding='utf-8') as f:
        notes = f.read().strip().split("\n")
        for index in notes:
            split_notes = index.split(';')
            note = creation.Note(id = split_notes[0], title = split_notes[1], body = split_notes[2], date = split_notes[3])
            array.append(note)
    return array      