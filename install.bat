@echo off
cls
echo ================================================
echo   User Monitor v1.0 - Instalacija
echo   Autor: Zeljko Tripcevski
echo ================================================
echo.

set STARTUP=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup

copy "%~dp0user-monitor.exe" "%STARTUP%\user-monitor.exe"

echo.
echo ================================================
echo   Instalacija zavrsena!
echo   User Monitor ce se pokretati sa Windowsom.
echo   Desni klik na ikonicu u taskbaru za
echo   podesavanja.
echo ================================================
echo.
pause