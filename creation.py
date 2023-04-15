from datetime import datetime
import uuid

class Note:
    def __init__(self, id = str(uuid.uuid1())[0:5],  title = "ввод", body = "ввод", date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))):
        self.id = id
        self.title = title
        self.body = body
        self.date = date
    
    def set_title(note):
        note.title = input('Введите название заметки: ')

    def set_body(note):
        note.body = input('Введите описание заметки: ')
        
    def set_id(note):
        note.id = str(uuid.uuid1())[0:5]
        
    def set_date(note):
        note.date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
        
    def get_id(note):
        return note.id
    
    def get_date(note):
        return note.date
        
    def output(note):
        return note.id + ';' + note.title + ';' + note.body + ';' + note.date + '\n'
    
    def show_note(note):
        return '\nID: ' + note.id + '\n' + 'Наименование: ' + note.title + '\n' + 'Текст заметки: ' + note.body + '\n' + 'Дата создания: ' + note.date