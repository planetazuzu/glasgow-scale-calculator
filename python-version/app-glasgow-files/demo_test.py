#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demo rápida de la Calculadora GCS con valores de ejemplo
"""

from glasgow_coma_scale import clasificar_gravedad

print("\n" + "="*60)
print("   DEMO - CALCULADORA GCS")
print("="*60)

# Ejemplo 1: Caso leve
print("\n📊 EJEMPLO 1: Paciente con trauma leve")
print("-" * 60)
ojos, verbal, motora = 4, 5, 6
total = ojos + verbal + motora
clasificacion, _ = clasificar_gravedad(total)
print(f"• Apertura de ojos: {ojos}/4 (Espontánea)")
print(f"• Respuesta verbal: {verbal}/5 (Orientada)")
print(f"• Respuesta motora: {motora}/6 (Obedece órdenes)")
print(f"• TOTAL GCS: {total}/15")
print(f"• Clasificación: {clasificacion}")

# Ejemplo 2: Caso moderado
print("\n📊 EJEMPLO 2: Paciente con trauma moderado")
print("-" * 60)
ojos, verbal, motora = 3, 4, 5
total = ojos + verbal + motora
clasificacion, _ = clasificar_gravedad(total)
print(f"• Apertura de ojos: {ojos}/4 (Al habla)")
print(f"• Respuesta verbal: {verbal}/5 (Confusa)")
print(f"• Respuesta motora: {motora}/6 (Localiza el dolor)")
print(f"• TOTAL GCS: {total}/15")
print(f"• Clasificación: {clasificacion}")

# Ejemplo 3: Caso grave
print("\n📊 EJEMPLO 3: Paciente en estado crítico")
print("-" * 60)
ojos, verbal, motora = 2, 2, 3
total = ojos + verbal + motora
clasificacion, _ = clasificar_gravedad(total)
print(f"• Apertura de ojos: {ojos}/4 (Al dolor)")
print(f"• Respuesta verbal: {verbal}/5 (Sonidos incomprensibles)")
print(f"• Respuesta motora: {motora}/6 (Flexión anormal)")
print(f"• TOTAL GCS: {total}/15")
print(f"• Clasificación: {clasificacion}")
print("⚠️ ADVERTENCIA: Requiere atención médica inmediata")

print("\n" + "="*60)
print("✅ La aplicación está funcionando correctamente")
print("="*60)
print("\nPara usar la aplicación interactiva:")
print("  - Versión consola: python glasgow_coma_scale.py")
print("  - Versión GUI:     python main.py")
print("="*60 + "\n")
