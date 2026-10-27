# 🚀 Instrucciones para ejecutar la aplicación localmente

Esta aplicación tiene dos versiones que puedes ejecutar en tu computadora Windows:

## 📋 Requisitos previos

- **Python 3.6 o superior** instalado en tu sistema
- Verificar con: `python --version` o `python3 --version`

## 🖥️ Opción 1: Versión de Línea de Comandos (Más simple)

Esta versión **NO requiere instalar nada adicional**, solo Python.

### Pasos:

1. Abre PowerShell o CMD en la carpeta `app-glasgow-files`

2. Ejecuta:
   ```powershell
   python glasgow_coma_scale.py
   ```

3. Sigue las instrucciones en pantalla

**✅ Esta es la opción más rápida para probar la aplicación!**

---

## 🎨 Opción 2: Versión con Interfaz Gráfica (GUI)

Esta versión tiene una interfaz visual moderna con sliders y botones.

### Instalación (solo la primera vez):

1. Abre PowerShell o CMD en la carpeta `app-glasgow-files`

2. Instala las dependencias:
   ```powershell
   pip install -r requirements.txt
   ```
   
   O directamente:
   ```powershell
   pip install kivy
   ```

### Ejecución:

Una vez instalado Kivy, ejecuta:

```powershell
python main.py
```

O alternativamente:

```powershell
python gcs_app.py
```

---

## 🔧 Solución de problemas

### Si `python` no funciona:

Intenta con `python3`:
```powershell
python3 glasgow_coma_scale.py
# o
python3 main.py
```

### Si pip no funciona:

Usa:
```powershell
python -m pip install kivy
```

### Problemas al instalar Kivy en Windows:

1. Asegúrate de tener la última versión de pip:
   ```powershell
   python -m pip install --upgrade pip
   ```

2. Instala Kivy:
   ```powershell
   python -m pip install kivy[base] kivy_examples
   ```

3. Si sigue fallando, visita: https://kivy.org/doc/stable/installation/installation-windows.html

---

## 📱 ¿Qué versión elegir?

- **Línea de comandos** → Si quieres probar rápido sin instalar nada
- **Interfaz gráfica** → Si prefieres una experiencia visual más agradable

---

## 🎯 Funcionalidad

Ambas versiones calculan la **Escala de Coma de Glasgow (GCS)** evaluando:

- 👁️ Apertura de ojos (1-4 puntos)
- 🗣️ Respuesta verbal (1-5 puntos)  
- 💪 Respuesta motora (1-6 puntos)

**Total: 3-15 puntos**

- 13-15: Lesión leve
- 9-12: Lesión moderada
- 3-8: Lesión grave (requiere atención inmediata)

---

## 📞 Compilar para Android

Si deseas compilar la aplicación para instalarla en un dispositivo Android, consulta:
- `INSTRUCCIONES_COMPILACION.md` - Instrucciones completas
- `compilar_apk.sh` - Script automatizado para Linux/Mac

**Nota:** La compilación de Android requiere un entorno Linux o WSL en Windows.

