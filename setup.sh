#!/bin/bash

echo -e "\e[32m===================================================\e[0m"
echo -e "\e[32m  🚀 Starting Python Project Setup (Linux) 🚀  \e[0m"
echo -e "\e[32m===================================================\e[0m"

# نصب پیش‌نیازهای سیستمی (tkinter و venv) برای اوبونتو/دبیان
echo "[1/4] Installing system dependencies (Requires sudo password)..."
sudo apt update
sudo apt install -y python3-venv python3-tk

echo "[2/4] Creating Virtual Environment (venv)..."
python3 -m venv venv

echo "[3/4] Activating venv..."
source venv/bin/activate

echo "[4/4] Upgrading pip via Iran Mirror 🌐..."
# استفاده از میرور ایران‌سرور
pip install --upgrade pip -i https://mirror.iranserver.com/pypi/simple/

# نصب پکیج‌های اضافی در صورت نیاز
# pip install -i https://mirror.iranserver.com/pypi/simple/ your_package_name

echo -e "\n\e[36m===================================================\e[0m"
echo -e "\e[36m  🎉 DONE! Your project is locked and loaded! 🎉  \e[0m"
echo -e "\e[36m  Run this to activate: source venv/bin/activate  \e[0m"
echo -e "\e[36m===================================================\e[0m"
