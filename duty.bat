@echo off
REM Перейти в директорию скрипта
cd /d C:\Users\Admin\DutyBotProject\Cash2uDutyBot

REM Активировать виртуальное окружение
call C:\Users\Admin\DutyBotProject\Cash2uDutyBot\.venv\Scripts\activate

REM Запустить Python скрипт
python main.py
