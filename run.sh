#!/bin/bash

# ���������, ��� ���� main.py ����������
if [ -f "main.py" ]; then
    echo "������ main.py..."
    python3 main.py
else
    echo "���� main.py �� ������!"
    exit 1
fi
