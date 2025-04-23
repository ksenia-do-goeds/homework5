import json
import random
import string

# Генерация случайного пароля
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Генерация случайного имени
def generate_name():
    first_names = ['John', 'Jane', 'Alice', 'Bob', 'Charlie']
    last_names = ['Doe', 'Smith', 'Johnson', 'Brown', 'Williams']
    return f"{random.choice(first_names)} {random.choice(last_names)}"

# Генерация случайного email
def generate_email(name):
    domains = ['example.com', 'test.com', 'sample.com']
    name_parts = name.lower().replace(" ", ".").split(".")
    return f"{name_parts[0]}.{name_parts[1]}@{random.choice(domains)}"

# Генерация случайного возраста
def generate_age(min_age=18, max_age=99):
    return random.randint(min_age, max_age)

# Создание пользовательского объекта
user_data = {
    "name": generate_name(),
    "age": generate_age(),
    "email": generate_email(user_data["name"] if 'user_data' in locals() else "Test User"),
    "password": generate_password()
}

# Сохранение JSON-объекта в файл
with open('user_data.json', 'w') as json_file:
    json.dump(user_data, json_file, indent=4)

# Чтение JSON-объекта из файла и вывод на экран
with open('user_data.json', 'r') as json_file:
    loaded_user_data = json.load(json_file)
    print(json.dumps(loaded_user_data, indent=4))
