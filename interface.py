import engine
           
def user_action():
    print('Добро пожаловать!')
    while (user_input := int(input('Выберите действие со справочником:\n \
    1 - Добавить заметку.\n \
    2 - Вывести все заметки.\n \
    3 - Найти заметку.\n \
    4 - Удалить заметку.\n \
    5 - Редактировать заметку.\n \
    6 - Поиск по дате создания заметки.\n \
    0 - Завершение работы.\n'))) != 0:
        if user_input == 1:
            engine.add_note()
        elif user_input == 2:
            engine.read_note()
        elif user_input == 3:
            engine.search_note()
        elif user_input == 4:
            engine.delete_note()
        elif user_input == 5:
            engine.edit_note()
        elif user_input == 6:
            engine.date_filter()
        else:
            print('Некорректный ввод')
    
    print('Ждем Вас снова!')