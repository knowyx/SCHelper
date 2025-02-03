#!/bin/bash

# Убедитесь, что файл main.py существует
if [ -f "main.py" ]; then
    echo "Запуск main.py..."
    python3 main.py
else
    echo "Файл main.py не найден!"
    exit 1
fi
