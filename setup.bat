@echo off
color 0A
echo ===================================================
echo   🚀 Starting Python Project Setup (Windows) 🚀
echo ===================================================

echo [1/3] Creating Virtual Environment (venv)...
python -m venv venv

echo [2/3] Activating venv...
call venv\Scripts\activate

echo [3/3] Upgrading pip and installing packages via Iran Mirror 🌐...
:: استفاده از میرور ایران‌سرور برای سرعت بالاتر
python -m pip install --upgrade pip -i https://mirror.iranserver.com/pypi/simple/

:: اگه پکیج دیگه‌ای خواستی اینجا اضافه کن (مثلا numpy یا هر چی)
:: pip install -i https://mirror.iranserver.com/pypi/simple/ your_package_name

echo.
echo ===================================================
echo   🎉 DONE! The environment is ready to use! 🎉
echo   To activate manually later, run: venv\Scripts\activate
echo ===================================================
pause
