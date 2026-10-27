@echo off
REM Script para ejecutar la version WEB de la Calculadora GCS
echo ================================================
echo   Calculadora GCS - Version Web (Navegador)
echo ================================================
echo.

REM Verificar si Streamlit esta instalado
python -c "import streamlit" 2>nul
if errorlevel 1 (
    echo [INFO] Streamlit no esta instalado.
    echo.
    echo Instalando Streamlit, por favor espera...
    echo Esto puede tardar un minuto...
    echo.
    python -m pip install streamlit
    if errorlevel 1 (
        echo.
        echo [ERROR] No se pudo instalar Streamlit.
        echo Por favor, ejecuta manualmente: pip install streamlit
        pause
        exit /b 1
    )
    echo.
    echo [OK] Streamlit instalado correctamente.
    echo.
)

echo Abriendo aplicacion en el navegador...
echo.
echo IMPORTANTE: 
echo - La aplicacion se abrira automaticamente en tu navegador
echo - Para detener el servidor, presiona Ctrl+C en esta ventana
echo.
streamlit run gcs_web.py

pause
