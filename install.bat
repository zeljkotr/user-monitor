@echo off
echo Instaliram User Monitor...

set STARTUP=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup
set SOURCE=%~dp0

copy "%SOURCE%user-monitor.exe" "%STARTUP%\user-monitor.exe"

echo.
echo User Monitor ce se pokretati automatski sa Windowsom!
echo Lokacija: %STARTUP%\user-monitor.exe
pause