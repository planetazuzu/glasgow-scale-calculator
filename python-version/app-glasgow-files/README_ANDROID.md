# Calculadora GCS para Android

Este proyecto es una versión para Android de la Calculadora de la Escala de Coma de Glasgow (GCS), desarrollada utilizando Python y Kivy.

## Requisitos para compilar

Para compilar la aplicación Android, necesitarás:

1. Python 3.7 o superior
2. Kivy 2.0.0 o superior
3. Buildozer (herramienta para empaquetar aplicaciones Python para Android)
4. JDK 8 o superior
5. Android SDK y Android NDK

## Pasos para compilar la aplicación

### 1. Preparación del entorno

Si estás en un sistema Linux (recomendado para la compilación), instala las dependencias necesarias:

```bash
sudo apt update
sudo apt install -y python3-pip build-essential git python3-dev ffmpeg libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev zlib1g-dev
```

Instala Kivy y Buildozer:

```bash
pip3 install kivy buildozer
```

### 2. Configuración del proyecto

El archivo `buildozer.spec` ya está configurado para esta aplicación. Si necesitas personalizarlo, puedes editar este archivo para cambiar:

- Nombre de la aplicación
- Paquete Android
- Versión
- Permisos
- Icono y splash screen
- Y muchas otras opciones

### 3. Compilar la aplicación

En el directorio del proyecto, ejecuta:

```bash
buildozer android debug
```

Este proceso puede tardar bastante tiempo la primera vez, ya que descarga e instala muchas dependencias.

Una vez terminada la compilación, encontrarás el archivo APK en la carpeta `bin/`.

### 4. Instalación en un dispositivo o emulador Android

Puedes instalar la aplicación generada en cualquier dispositivo Android:

```bash
adb install -r bin/gcs_calculator-0.1-arm64-v8a_armeabi-v7a-debug.apk
```

## Ejecución local (para desarrollo)

Para ejecutar la aplicación localmente durante el desarrollo:

```bash
python main.py
```

## Estructura del proyecto

- `main.py`: Punto de entrada de la aplicación
- `gcs_app.py`: Implementación principal de la aplicación con Kivy
- `buildozer.spec`: Configuración para la compilación Android

## Notas importantes

1. La compilación para Android puede requerir significativos recursos de CPU y memoria.
2. El proceso de compilación puede tardar entre 15-30 minutos la primera vez.
3. Para una experiencia de desarrollo más rápida, prueba los cambios localmente antes de compilar para Android.
4. La aplicación requiere un mínimo de Android 5.0 (API 21).