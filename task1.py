import random
import string
from pathlib import Path

def generate_random_filename(length=8):
    """Генерирует случайное имя файла длиной length символов."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length)) + '.txt'

def create_random_files(directory, num_files=10):
    """Создает num_files случайных файлов в указанной директории."""
    path = Path(directory)
    path.mkdir(parents=True, exist_ok=True) 
    
    created_files = []
    
    for _ in range(num_files):
        filename = generate_random_filename()
        file_path = path / filename
        with open(file_path, 'w') as f:
            f.write("")
        created_files.append(file_path.resolve())
    
    return created_files

# Пример использования
directory = '/home/user/random_files'
created_files = create_random_files(directory)

# Вывод списка созданных файлов
for file in created_files:
    print(file)
