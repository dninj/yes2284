import sqlite3

# Подключение к базе данных (или создание, если ее нет)
conn = sqlite3.connect('youtube.db')
cursor = conn.cursor()

# Создание таблицы
cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        link TEXT NOT NULL,
        author TEXT,
        date TEXT,
        description TEXT
    )
''')

# Добавление данных
videos = [
    ("Python для начинающих", "https://www.youtube.com/watch?v=1", "Иван Иванов", "2024-01-15", "Основы Python"),
    ("Готовим пиццу", "https://www.youtube.com/watch?v=2", "Елена Петрова", "2024-02-20", "Рецепт вкусной пиццы"),
    ("Путешествие по Японии", "https://www.youtube.com/watch?v=3", "Дмитрий Сидоров", "2024-03-10", "Впечатления от поездки"),
    ("Обзор нового телефона", "https://www.youtube.com/watch?v=4", "Анна Кузнецова", "2024-04-05", "Характеристики и возможности"),
    ("Учимся рисовать", "https://www.youtube.com/watch?v=5", "Мария Новикова", "2024-05-25", "Урок рисования для новичков")
]

cursor.executemany("INSERT INTO videos (title, link, author, date, description) VALUES (?, ?, ?, ?, ?)", videos)


# Вывод всех данных
print("\nВсе видео:")
cursor.execute("SELECT * FROM videos")
all_rows = cursor.fetchall()
for row in all_rows:
    print(row)

# Изменение записи
cursor.execute("UPDATE videos SET author = 'Новый Автор' WHERE id = 1")

# Удаление записи
cursor.execute("DELETE FROM videos WHERE id = 5")

# Вывод данных после изменений
print("\nВидео после изменений:")
cursor.execute("SELECT * FROM videos")
all_rows = cursor.fetchall()
for row in all_rows:
    print(row)


# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()

