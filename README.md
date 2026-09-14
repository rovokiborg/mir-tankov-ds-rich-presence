# Мир Танков (Lesta) — Discord Rich Presence

Небольшой Python-скрипт, который автоматически включает Discord Rich Presence при запуске **Мира Танков**.

Скрипт отслеживает процесс игры и:

* автоматически подключается к Discord, когда игра запущена;
* показывает кастомный статус в профиле Discord;
* отображает время текущей игровой сессии;
* случайно меняет описание активности;
* автоматически убирает статус после закрытия игры;
* работает в фоне через `pythonw.exe`.

## Требования

* Windows 10/11
* Python 3.10+
* Discord Desktop
* Мир Танков
* созданное Discord Application с Rich Presence Asset

Python-библиотеки:

```text
psutil
pypresence
```

## Структура проекта

Пример:

```text
tanki-rpc/
│
├── tanki.bat
├── tanki.pyw
├── requirements.txt
│
└── mir_tankov/
    ├── Scripts/
    │   ├── python.exe
    │   ├── pythonw.exe
    │   └── pip.exe
    └── ...
```

`mir_tankov` — Python virtual environment.

## Установка

### 1. Создать виртуальное окружение

Откройте командную строку в папке проекта:

```bat
python -m venv mir_tankov
```

### 2. Установить зависимости

```bat
mir_tankov\Scripts\pip.exe install -r requirements.txt
```

Либо:

```bat
mir_tankov\Scripts\python.exe -m pip install -r requirements.txt
```

## Настройка Discord Application

В коде используется:

```python
CLIENT_ID = "1458048320575508665"
```

Это ID Discord Application. Полностью рабочий, но если вы хотите добавить что то своё:

Для собственного приложения необходимо:

1. Открыть Discord Developer Portal.
2. Создать Application.
3. Скопировать `Application ID`.
4. Указать его в:

```python
CLIENT_ID = "ВАШ_APPLICATION_ID"
```

5. Добавить изображение для Rich Presence с ключом:

```text
tank
```

Этот ключ должен совпадать с:

```python
IMAGE_KEY = "tank"
```

## Отслеживаемые процессы

Скрипт считает игру запущенной, если обнаруживает один из процессов:

```python
POSSIBLE_PROCESSES = [
    "tanki.exe",
    "worldoftanks.exe",
    "wot.exe"
]
```

Если реальный `.exe` игры называется иначе, добавьте его название в этот список.

## Запуск

Для запуска используется:

```text
tanki.bat
```

Содержимое:

```bat
@echo off
cd /d "%~dp0"

if exist "mir_tankov\Scripts\pythonw.exe" (
    set PYTHON_EXE="mir_tankov\Scripts\pythonw.exe"
) else (
    echo ОШИБКА: Не найден pythonw.exe в папке mir_tankov\Scripts
    pause
    exit /b 1
)

start "" %PYTHON_EXE% "tanki.pyw"
```

После запуска окно консоли не будет отображаться, потому что используется `pythonw.exe`.

Скрипт продолжит работать в фоне и будет ждать запуска игры.

## Как это работает

Каждые 15 секунд скрипт проверяет список процессов Windows:

```python
time.sleep(15)
```

Когда обнаруживается Мир Танков:

1. выполняется подключение к Discord RPC;
2. запоминается время запуска;
3. устанавливается Discord Activity.

Пример активности:

```text
Мир Танков

Раздает в зюзю
На поле боя

00:42:17 elapsed
```

Описание выбирается случайно из списка:

```python
DESCRIPTIONS = [
    "Пьет пиво",
    "Ебет на бабахе",
    "Качает ветку",
    "Отращивает пузо",
    "Ебет тухлозадых",
    "Раздает в зюзю",
    "Артаводы кто?"
]
```

После закрытия игры Rich Presence автоматически очищается.

## Discord должен быть запущен

`pypresence` подключается к локальному Discord-клиенту.

Если Discord не запущен, подключение не произойдет.

Скрипт попробует подключиться снова после следующей проверки.

## Автозапуск с Windows

Если необходимо запускать скрипт автоматически вместе с Windows:

1. Нажмите `Win + R`.
2. Введите:

```text
shell:startup
```

3. Создайте в открывшейся папке ярлык на:

```text
tanki.bat
```

После этого скрипт будет автоматически запускаться после входа в Windows.

## Остановка

Так как используется `pythonw.exe`, окно консоли отсутствует.

Для остановки можно завершить процесс `pythonw.exe` через Диспетчер задач.

Если на компьютере одновременно работают другие Python-программы через `pythonw.exe`, убедитесь, что завершаете именно нужный процесс.

## Основные настройки

### Изменить статус

```python
state="На поле боя"
```

### Изменить описания

Отредактируйте:

```python
DESCRIPTIONS = [...]
```

### Изменить картинку

```python
IMAGE_KEY = "tank"
```

Изображение с таким же ключом должно существовать в Discord Application.

### Изменить частоту проверки

```python
time.sleep(15)
```

Например, проверка каждые 5 секунд:

```python
time.sleep(5)
```

## Зависимости

Проект использует:

* `psutil` — поиск процесса игры;
* `pypresence` — работа с Discord Rich Presence.

## License

Проект предназначен для личного использования.
