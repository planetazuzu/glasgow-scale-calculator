# Instrucciones para compilar la Calculadora GCS para Android

Este documento contiene las instrucciones detalladas para compilar la aplicación Calculadora de la Escala de Coma de Glasgow (GCS) en un APK para dispositivos Android.

## Requisitos previos

Para compilar esta aplicación necesitarás:

1. **Python**: Versión 3.7 o superior
2. **Kivy**: Framework para la interfaz gráfica
3. **Buildozer**: Herramienta para empaquetar aplicaciones Python para Android
4. **JDK**: Java Development Kit (versión 8 o superior)
5. **Android SDK**: Kit de desarrollo de Android
6. **Otras dependencias**: Bibliotecas de desarrollo necesarias

## Pasos para la compilación

### 1. Preparación del entorno (Linux - Recomendado)

**Ubuntu/Debian**:

```bash
# Instalar dependencias necesarias
sudo apt update
sudo apt install -y python3-pip build-essential git python3-dev ffmpeg libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev zlib1g-dev openjdk-11-jdk autoconf libtool pkg-config

# Instalar kivy y buildozer
pip3 install kivy buildozer
```

**Windows**:
La compilación en Windows es más compleja. Recomendamos usar WSL (Windows Subsystem for Linux) o una máquina virtual con Ubuntu.

### 2. Compilación del APK

1. Coloca todos los archivos del proyecto en una carpeta
2. Abre una terminal en esa carpeta
3. Puedes compilar de dos formas:

   **a) Usando el script incluido:**
   ```bash
   # Dar permisos de ejecución
   chmod +x compilar_apk.sh
   
   # Ejecutar el script
   ./compilar_apk.sh
   ```

   **b) Manualmente:**
   ```bash
   # Crear APK de depuración
   buildozer -v android debug
   ```

4. La primera compilación puede tardar entre 15-30 minutos, ya que descarga e instala muchas dependencias.

### 3. Instalación en el dispositivo

Una vez que la compilación termine con éxito, encontrarás el archivo APK en la carpeta `bin/`.

Para instalar:
1. Habilita la instalación de aplicaciones de fuentes desconocidas en tu dispositivo Android
2. Transfiere el archivo APK a tu dispositivo (USB, email, etc.)
3. Toca el archivo APK en tu dispositivo para instalarlo
4. Alternativamente, puedes usar ADB:
   ```bash
   adb install -r bin/gcs_calculator-0.1-*-debug.apk
   ```

## Solución de problemas

### Errores comunes:

1. **Error de SDK de Android**: Si buildozer no encuentra el SDK de Android, descargará uno automáticamente.

2. **Error de JDK**: Asegúrate de tener instalado JDK 8 o superior y que JAVA_HOME esté configurado correctamente.

3. **Error de memoria**: La compilación requiere bastante memoria RAM. Si encuentras errores, intenta cerrar otras aplicaciones.

4. **Errores de dependencias**: Si faltan dependencias, buildozer suele mostrar mensajes claros sobre qué paquetes faltan.

## Código fuente

El proyecto consta de los siguientes archivos principales:
- `main.py`: Punto de entrada de la aplicación
- `gcs_app.py`: Implementación principal con Kivy
- `buildozer.spec`: Configuración para la compilación

Si encuentras problemas o tienes preguntas, consulta la documentación oficial de Kivy y Buildozer.