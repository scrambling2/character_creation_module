from random import randint


def attack(char_name: str, char_class: str) -> str:
    """Аттака."""
    if char_class == 'warrior':
        return (f'{char_name} нанёс урон противнику равный{5 + randint(3,5)}')
    if char_class == 'mage':
        return (f'{char_name} нанёс урон противнику равный{5 + randint(5,10)}')
    if char_class == 'healer':
        return (f'{char_name}нанёс урон противнику равный{5 + randint(-3,-1)}')
    return (f'{char_name} не нанёс урон противнику равный{0 + randint(0,-1)}')


def defence(char_name: str, char_class: str) -> str:
    """Защита."""
    if char_class == 'warrior':
        return (f'{char_name} блокировал {10 + randint(5, 10)} урона')
    if char_class == 'mage':
        return (f'{char_name} блокировал {10 + randint(-2, 2)} урона')
    if char_class == 'healer':
        return (f'{char_name} блокировал {10 + randint(2, 5)} урона')
    return (f'{char_name} не блокировал {0 + randint(0, 1)} урона')


def special(char_name: str, char_class: str) -> str:
    """Специальные умения."""
    if char_class == 'warrior':
        return (f'{char_name} применил специальное умение Выносливость{80+25}')
    if char_class == 'mage':
        return (f'{char_name} применил специальное умение «Атака {5 + 40}»')
    if char_class == 'healer':
        return (f'{char_name} применил специальное умение «Защита {10 + 30}»')
    return (f'{char_name} не применил специальное умение «{0 + 0}»')


def start_training(char_name: str, char_class: str) -> str:
    """Начало тренировки."""
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи команду:attack—атака,defence—защита,special—суперсила.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    """Выбор игрока."""
    approve_choice: str = None
    char_class: str = None
    while approve_choice != 'y':
        char_class = input('Введи имя:Воитель—warrior,Маг—mage,Лекарь—healer:')
        if char_class == 'warrior':
            print('Воитель—воин ближнего боя.Сильный,выносливый и отважный.')
        if char_class == 'mage':
            print('Маг — воин дальнего боя.Обладает высоким интеллектом.')
        if char_class == 'healer':
            print('Лекарь—заклинатель.Черпает силы из природы,веры и духов.')
        approve_choice = input('Нажми Y-OK,или другую-выбрать другого').lower()
    return char_class
