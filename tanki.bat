@echo off
cd /d "%~dp0"

:: Проверяем, существует ли файл интерпретатора
if exist "mir_tankov\Scripts\pythonw.exe" (
    set PYTHON_EXE="mir_tankov\Scripts\pythonw.exe"
) else (
    echo ОШИБКА: Не найден pythonw.exe в папке mir_tankov\Scripts
    pause
    exit
)

:: Запуск скрипта
start "" %PYTHON_EXE% "main.py"