# Calculadora de la Escala de Coma de Glasgow (GCS)

Esta herramienta permite calcular la Escala de Coma de Glasgow (GCS), un método utilizado para evaluar el nivel de conciencia en pacientes que han sufrido traumatismos craneoencefálicos u otros daños cerebrales.

## Aclaración Importante

En algunos contextos, la Escala de Coma de Glasgow es incorrectamente referida como "ECG" (que corresponde al Electrocardiograma, una prueba completamente diferente). La abreviatura correcta para la Escala de Coma de Glasgow es **GCS** (Glasgow Coma Scale).

## Versiones Disponibles

El proyecto ofrece dos versiones:

1. **Versión de línea de comandos** - Interfaz basada en texto para uso en terminal
2. **Aplicación Android** - Versión móvil con interfaz gráfica táctil

## Características

- Cálculo preciso de la Escala de Coma de Glasgow (GCS)
- Evaluación de los tres componentes principales:
  - Apertura de ojos (1-4 puntos)
  - Mejor respuesta verbal (1-5 puntos)
  - Mejor respuesta motora (1-6 puntos)
- Muestra la puntuación total (3-15 puntos)
- Clasifica la gravedad de la lesión (Leve, Moderada, Grave)
- Incluye manejo de errores para entradas inválidas
- Información detallada sobre cada criterio de evaluación

## Requisitos

### Versión de línea de comandos
- Python 3.6 o superior

### Versión Android
- Dispositivo Android con versión 5.0 (API 21) o superior

## Uso

### Línea de comandos

1. Asegúrese de tener Python instalado en su sistema
2. Descargue el archivo `glasgow_coma_scale.py`
3. Ejecute el siguiente comando en la terminal:

```bash
python glasgow_coma_scale.py
```

### Android

Para usar la aplicación Android:

1. Descargue e instale el APK en su dispositivo
2. Abra la aplicación "Calculadora GCS"
3. Use los deslizadores para seleccionar los valores
4. Presione "Calcular" para ver el resultado

## Compilación de la versión Android

Si desea compilar la aplicación Android desde el código fuente:

1. Consulte el archivo [INSTRUCCIONES_COMPILACION.md](INSTRUCCIONES_COMPILACION.md) para instrucciones detalladas
2. Use el script [compilar_apk.sh](compilar_apk.sh) para automatizar el proceso

Para más información:
- [README_ANDROID.md](README_ANDROID.md) - Detalles técnicos de la versión Android
- [README_ES.md](README_ES.md) - Documentación en español
