@echo off

py "%~dp0mp3\shuffle_mp3.py"
if errorlevel 1 (
    echo.
    echo Failed to shuffle MP3 files.
    pause
    exit /b 1
)

if exist "%~dp0gta-vc.exe" (
    start "" "%~dp0gta-vc.exe"
) else if exist "%~dp0gta3.exe" (
    start "" "%~dp0gta3.exe"
) else (
    echo.
    echo Could not find gta-vc.exe or gta3.exe.
    pause
    exit /b 1
)