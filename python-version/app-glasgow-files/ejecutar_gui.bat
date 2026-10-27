@echo off
REM Script para ejecutar la version GUI de la Calculadora GCS
echo ================================================
echo   Calculadora GCS - Version Interfaz Grafica
echo ================================================
echo.

REM Verificar si Kivy esta instalado
python -c "import kivy" 2>nul
if errorlevel 1 (
    echo [ERROR] Kivy no esta instalado.
    echo.
    echo Instalando Kivy, por favor espera...
    echo.
    python -m pip install kivy
    if errorlevel 1 (
        echo.
        echo [ERROR] No se pudo instalar Kivy.
        echo Por favor, ejecuta manualmente: pip install kivy
        pause
        exit /b 1
    )
    echo.
    echo [OK] Kivy instalado correctamente.
    echo.
)

echo Iniciando aplicacion...
echo.
python main.py

pause

