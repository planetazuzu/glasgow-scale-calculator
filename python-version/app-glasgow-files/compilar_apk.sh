#!/bin/bash
# Script para compilar la aplicación GCS Calculator para Android
# Este script te guiará por el proceso de compilación

echo "================================================="
echo "   Compilación de Calculadora GCS para Android   "
echo "================================================="

# Verificar si buildozer está instalado
if ! command -v buildozer &> /dev/null; then
    echo "Buildozer no está instalado. Instalando..."
    pip install buildozer
else
    echo "Buildozer ya está instalado."
fi

# Verificar si kivy está instalado
if ! pip show kivy &> /dev/null; then
    echo "Kivy no está instalado. Instalando..."
    pip install kivy
else
    echo "Kivy ya está instalado."
fi

echo "Instalando dependencias del sistema (esto puede requerir contraseña)..."
echo "En Ubuntu/Debian, ejecuta estos comandos:"
echo "sudo apt update"
echo "sudo apt install -y python3-pip build-essential git python3-dev ffmpeg libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev zlib1g-dev openjdk-11-jdk autoconf libtool pkg-config"

echo "Iniciando compilación de APK..."
echo "Este proceso puede tardar varios minutos la primera vez."

# Iniciar compilación
buildozer -v android debug

# Verificar si se generó el APK
if [ -d "./bin" ] && [ "$(ls -A ./bin)" ]; then
    echo "================================================="
    echo "¡Compilación exitosa!"
    echo "El archivo APK se encuentra en la carpeta bin/"
    echo "Puedes instalar el APK en tu dispositivo Android"
    echo "================================================="
else
    echo "================================================="
    echo "Hubo un problema en la compilación."
    echo "Revisa los mensajes de error anteriores."
    echo "================================================="
fi