# 🎯 Guía Rápida de Ejecución

## ⚡ Forma más rápida (Doble clic)

### Opción 1: Versión de Consola (recomendado para prueba rápida)
1. Haz **doble clic** en `ejecutar_consola.bat`
2. ¡Listo! La aplicación se ejecutará en la consola

### Opción 2: Versión con Interfaz Gráfica
1. Haz **doble clic** en `ejecutar_gui.bat`
2. Si es la primera vez, se instalará Kivy automáticamente
3. La aplicación se abrirá en una ventana

## 📝 Forma manual (PowerShell/CMD)

### Versión Consola:
```powershell
python glasgow_coma_scale.py
```

### Versión GUI:
```powershell
# Instalar Kivy (solo primera vez)
pip install kivy

# Ejecutar la aplicación
python main.py
```

## 📁 Archivos disponibles

- `glasgow_coma_scale.py` - Versión de línea de comandos
- `main.py` - Punto de entrada para versión GUI
- `gcs_app.py` - Código principal de la interfaz gráfica
- `ejecutar_consola.bat` - Script de ejecución rápida (consola)
- `ejecutar_gui.bat` - Script de ejecución rápida (GUI)
- `requirements.txt` - Dependencias del proyecto
- `INSTRUCCIONES_LOCAL.md` - Instrucciones detalladas

## 🎨 Capturas de funcionalidad

**Versión Consola:**
- Interfaz de texto interactiva
- Cálculo inmediato del GCS
- Clasificación automática (Leve/Moderado/Grave)
- Colores para mejor visualización

**Versión GUI:**
- Sliders para seleccionar valores
- Interfaz moderna y visual
- Resultados con colores según gravedad
- Compatible con touch/mouse

## 📊 ¿Qué calcula?

La **Escala de Coma de Glasgow (GCS)** evalúa 3 parámetros:

1. 👁️ **Apertura de ojos**: 1-4 puntos
2. 🗣️ **Respuesta verbal**: 1-5 puntos
3. 💪 **Respuesta motora**: 1-6 puntos

**Puntuación total: 3-15**

- ✅ 13-15: Lesión **leve**
- ⚠️ 9-12: Lesión **moderada**
- 🚨 3-8: Lesión **grave** (atención inmediata)

## ❓ Problemas comunes

### Python no reconocido
→ Instala Python desde: https://www.python.org/downloads/

### `pip` no funciona
→ Ejecuta: `python -m pip install kivy`

### Kivy no se instala
→ Actualiza pip primero: `python -m pip install --upgrade pip`

---

**¡Listo para usar!** 🚀

