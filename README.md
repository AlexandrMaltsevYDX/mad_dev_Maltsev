# mad_dev_Maltse
## Краткое описание
###  Основной скрипт
split_msg.py
## Структура проекта
```
./
├── msg/                1. Примеры html файлов
│   ├── test-1.html     2. html файл
│   ├── test-2.html     ----//----
│   └── test-3.html     ----//----
├── exceptions.py       3. Имплементация исключений
├── utils.py            4. Вспомогательные функции
├── test_spliting.py    5. Unit тесты
├── split_msg.py        6. !!! ОСНОВНОЙ СКРИПТ
├── requirements.txt    7. Файл с зависимостями
├── Тестовое_задание_для_кандидатов_backend.pdf    
└── README.md
```
## Используемые библиотеки
- Версия Python:        3.10
- Парсинг html:         HtmlParser  (стандартная библиотека)
- Unit тесты:           pytest
- Генерация фикстур:    itertools   (стандартная библиотека)   
- аргументы shell:      argparse    (стандартная библиотека)

## Установка
### Клонировать репозиторий и перейти в папку с ним
### Установить Виртуальное окружение
```
python -m venv venv
```
```
python3 -m venv venv
```
### Активацировать виртуальное окружение
#### - для Windows;
```
venv\Scripts\activate.bat
```
#### - для Linux и MacOS.
```
source venv/bin/activate
```
### Установка зависимостей
```
pip install -r requirements.txt
```
### Запуск тестов
```
pytest -v
```
## Скрипты для теста основного файла(также в коментарии в split_msg.py)
```
python split_msg.py --max-len=120 ./msg/test-1.html
```
```
python split_msg.py --max-len=150 ./msg/test-2.html
```
```
python split_msg.py --max-len=200 ./msg/test-3.html
```
```
python split_msg.py --max-len=20  ./msg/test-1.html
```