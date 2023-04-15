import creation
import tools

def add_note():
    note = creation.Note
    creation.Note.set_id(note)
    creation.Note.set_title(note)
    creation.Note.set_body(note)
    creation.Note.set_date(note)
    
    with open('notes.csv', 'a', encoding='utf-8') as f:
        f.write(f'{creation.Note.output(note)}')
    print('Заметка добавлена')

def read_note():
    array = tools.create_note()
    for note in array:
        print(creation.Note.show_note(note))
        
def search_note():
    search = input('Введите ID заметки: ')
    array = tools.create_note()
            
    find = False
    for note in array:
        if search == creation.Note.get_id(note):
            print(creation.Note.show_note(note))
            find = True
    if find == False:
        print('Такой заметки нет.')
                
def delete_note():
    deletion = input('Введите ID заметки: ')
    array = tools.create_note()
            
    find = False
    for note in array:
        if deletion == creation.Note.get_id(note):
            array.remove(note)
            find = True
            print('Заметка удалена.')
    if find == False:
        print('Такой заметки нет.')
    
    with open('notes.csv', 'w', encoding='utf-8') as f:
        for note in array:
            f.write(f'{creation.Note.output(note)}')
                
def edit_note():
    edit = input('Введите ID заметки: ')
    array = tools.create_note()
    
    find = False
    for note in array:
        if edit == creation.Note.get_id(note):
            creation.Note.set_title(note)
            creation.Note.set_body(note)
            find = True
            print('Заметка отредактирована')
    if find == False:
        print('Такой заметки нет.')
        
    with open('notes.csv', 'w', encoding='utf-8') as f:
        for note in array:
            f.write(f'{creation.Note.output(note)}')
            
def date_filter():
    array = tools.create_note()
    start_date = input('Введите с какого даты и времени искать в формате дд.мм.гггг: ')
    for note in array:
        if start_date in creation.Note.get_date(note):
            print(creation.Note.show_note(note))