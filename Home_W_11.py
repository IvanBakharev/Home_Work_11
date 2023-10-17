                                                    # Первое задание
def factorial(x):
    # Вычисление факториала числа x
    nx = 1
    for i in range(x):
        nx *= i + 1
    return nx

def listFactorialNumbers(x):
    # Создание списка факториалов чисел от факториала числа x до 1
    numbers = factorial(x)
    arr = list()
    for i in range(numbers, 0, -1):
        arr.append(factorial(i))
    return arr

# Вычисление и вывод факториала числа 3
print(factorial(3))

# Создание и вывод списка факториалов чисел от факториала числа 3 до 1
print(listFactorialNumbers(3))

                                                   # Второе задание
import collections

# Создание пустого словаря pets
pets = {}

# Функция для получения информации о питомце по его ID
def get_pet(ID):
    # Проверка наличия питомца с указанным ID
    if ID in pets.keys():
        return pets[ID]  # Возвращаем информацию о питомце
    else:
        return False  # Если питомца нет, возвращаем False

# Функция для получения суффикса 'год', 'года', 'лет'
def get_suffix(age):
    # Логика определения суффикса в зависимости от возраста
    if age == 1:
        return 'год'
    elif 1 < age < 5:
        return 'года'
    else:
        return 'лет'

# Функция для отображения списка питомцев
def pets_list():
    # Цикл для вывода информации о каждом питомце
    for ID, pet_info in pets.items():
        name = list(pet_info.keys())[0]
        animal_type = pet_info[name]['Вид питомца']
        age = pet_info[name]['Возраст питомца']
        owner_name = pet_info[name]['Имя владельца']
        age_suffix = get_suffix(age)
        info_string = f'Это {animal_type} по кличке "{name}". Возраст питомца: {age} {age_suffix}. Имя владельца: {owner_name}'
        print(info_string)

# Функция для создания новой записи о питомце
def create():
    last = collections.deque(pets, maxlen=1)[0]  # Получение последнего ключа (идентификатора)
    new_id = last + 1  # Увеличение идентификатора на единицу
    name = input("Введите имя питомца: ")
    animal_type = input("Введите вид питомца: ")
    age = int(input("Введите возраст питомца: "))
    owner_name = input("Введите имя владельца: ")
    pet_info = {
        name: {
            'Вид питомца': animal_type,
            'Возраст питомца': age,
            'Имя владельца': owner_name
        }
    }
    pets[new_id] = pet_info  # Добавление новой записи в словарь pets

# Функция для обновления информации о питомце
def update():
    ID = int(input("Введите ID питомца для обновления: "))
    pet_info = get_pet(ID)  # Получение информации о питомце
    if pet_info:
        name = list(pet_info.keys())[0]
        print(f"Текущая информация о питомце {name}:")
        print(pet_info[name])
        animal_type = input("Введите новый вид питомца: ")
        age = int(input("Введите новый возраст питомца: "))
        owner_name = input("Введите новое имя владельца: ")
        pet_info[name]['Вид питомца'] = animal_type
        pet_info[name]['Возраст питомца'] = age
        pet_info[name]['Имя владельца'] = owner_name
        print("Информация о питомце успешно обновлена!")
    else:
        print("Питомец с указанным ID не найден!")

# Функция для удаления записи о питомце
def delete():
    ID = int(input("Введите ID питомца для удаления: "))
    pet_info = get_pet(ID)  # Получение информации о питомце
    if pet_info:
        name = list(pet_info.keys())[0]
        del pets[ID]  # Удаление записи о питомце
        print(f"Информация о питомце {name} успешно удалена!")
    else:
        print("Питомец с указанным ID не найден!")

# Основной цикл программы
command = ''
while command != 'stop':
    command = input("Введите команду (create, read, update, delete, pets_list, stop): ")
    if command == 'create':
        create()
    elif command == 'read':
        ID = int(input("Введите ID питомца для отображения информации: "))
        pet_info = get_pet(ID)
        if pet_info:
            name = list(pet_info.keys())[0]
            animal_type = pet_info[name]['Вид питомца']
            age = pet_info[name]['Возраст питомца']
            owner_name = pet_info[name]['Имя владельца']
            age_suffix = get_suffix(age)
            info_string = f'Это {animal_type} по кличке "{name}". Возраст питомца: {age} {age_suffix}. Имя владельца: {owner_name}'
            print(info_string)
        else:
            print("Питомец с указанным ID не найден!")
    elif command == 'update':
        update()
    elif command == 'delete':
        delete()
    elif command == 'pets_list':
        pets_list()
    elif command == 'stop':
        print("Работа программы завершена.")
    else:
        print("Неверная команда! Попробуйте снова.")
