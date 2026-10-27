#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Glasgow Coma Scale Calculator

This tool calculates the Glasgow Coma Scale (GCS) score to assess 
the level of consciousness in patients after brain injury.

Note: GCS is often incorrectly referred to as ECG (which is an electrocardiogram).
The correct abbreviation is GCS (Glasgow Coma Scale).
"""

import os
import sys


def clear_screen():
    """Clear the terminal screen based on the operating system."""
    os.system('cls' if os.name == 'nt' else 'clear')


def get_valid_input(prompt, min_value, max_value):
    """
    Get and validate user input within a specific range.
    
    Args:
        prompt (str): The input prompt to display
        min_value (int): Minimum acceptable value
        max_value (int): Maximum acceptable value
        
    Returns:
        int: The validated input value
    """
    while True:
        try:
            value = input(prompt)
            # Allow user to exit
            if value.lower() in ['q', 'quit', 'salir', 'exit']:
                print("\nSaliendo del programa. ¡Hasta luego!")
                sys.exit(0)
                
            value = int(value)
            if min_value <= value <= max_value:
                return value
            else:
                print(f"\033[91mError: Ingrese un valor entre {min_value} y {max_value}.\033[0m")
        except ValueError:
            print("\033[91mError: Por favor ingrese un número válido.\033[0m")


def display_header():
    """Display a formatted header for the tool."""
    print("\033[1;36m")  # Cyan, bold
    print("=" * 60)
    print("      CALCULADORA DE LA ESCALA DE COMA DE GLASGOW (GCS)")
    print("=" * 60)
    print("\033[0m")  # Reset formatting
    print("Esta herramienta permite evaluar el nivel de conciencia en pacientes")
    print("con daño cerebral, basándose en tres criterios: apertura ocular,")
    print("respuesta verbal y respuesta motora.")
    print("\nEn cualquier momento, escriba 'q' o 'salir' para terminar.")
    print("-" * 60)


def calcular_gcs():
    """
    Calculate the Glasgow Coma Scale (GCS) score based on user input.
    
    Returns:
        tuple: Contains eye score, verbal score, motor score, and total score
    """
    clear_screen()
    display_header()
    
    # 1. Eye Opening (Apertura de ojos)
    print("\n\033[1;33m[1] APERTURA DE OJOS:\033[0m")
    print("  4) Espontánea - Abre los ojos espontáneamente")
    print("  3) Al habla - Abre los ojos cuando se le habla")
    print("  2) Al dolor - Abre los ojos solo ante estímulos dolorosos")
    print("  1) Ninguna - No abre los ojos bajo ningún estímulo")
    ojos = get_valid_input("\nSeleccione el valor (1-4): ", 1, 4)
    
    # 2. Verbal Response (Respuesta verbal)
    print("\n\033[1;33m[2] MEJOR RESPUESTA VERBAL:\033[0m")
    print("  5) Orientada - Responde coherentemente, orientado en tiempo, lugar y persona")
    print("  4) Confusa - Responde pero de manera confusa o desorientada")
    print("  3) Palabras inapropiadas - Palabras reconocibles pero respuestas aleatorias")
    print("  2) Sonidos incomprensibles - Solo emite gemidos, quejidos o sonidos")
    print("  1) Ninguna - No emite sonidos")
    verbal = get_valid_input("\nSeleccione el valor (1-5): ", 1, 5)
    
    # 3. Motor Response (Respuesta motora)
    print("\n\033[1;33m[3] MEJOR RESPUESTA MOTORA:\033[0m")
    print("  6) Obedece órdenes - Sigue comandos simples")
    print("  5) Localiza el dolor - Intenta localizar/retirar el estímulo doloroso")
    print("  4) Retirada al dolor - Flexión normal, retira la parte estimulada")
    print("  3) Flexión anormal - Postura de decorticación (brazos flexionados)")
    print("  2) Extensión anormal - Postura de descerebración (brazos extendidos)")
    print("  1) Ninguna - No hay respuesta motora, flacidez")
    motora = get_valid_input("\nSeleccione el valor (1-6): ", 1, 6)
    
    # Calculate total
    total = ojos + verbal + motora
    
    return ojos, verbal, motora, total


def clasificar_gravedad(total):
    """
    Classify severity based on total GCS score.
    
    Args:
        total (int): Total GCS score
        
    Returns:
        tuple: Classification string and color code
    """
    if total >= 13:
        return "Leve (Trauma craneal menor)", "\033[92m"  # Green
    elif total >= 9:
        return "Moderado (Requiere vigilancia)", "\033[93m"  # Yellow
    else:
        return "Grave (Estado crítico)", "\033[91m"  # Red


def mostrar_resultados(ojos, verbal, motora, total):
    """
    Display the assessment results with color formatting.
    
    Args:
        ojos (int): Eye opening score
        verbal (int): Verbal response score
        motora (int): Motor response score
        total (int): Total GCS score
    """
    clasificacion, color = clasificar_gravedad(total)
    
    print("\n" + "=" * 60)
    print("\033[1;36mRESULTADOS DE LA EVALUACIÓN\033[0m")
    print("=" * 60)
    print(f"• Apertura de ojos: {ojos}/4")
    print(f"• Respuesta verbal: {verbal}/5")
    print(f"• Respuesta motora: {motora}/6")
    print("-" * 60)
    print(f"• Puntuación total GCS: {color}{total}/15\033[0m")
    print(f"• Clasificación: {color}{clasificacion}\033[0m")
    print("=" * 60)
    
    if total <= 8:
        print("\033[91m¡ADVERTENCIA! Puntuación indicativa de una lesión grave.\033[0m")
        print("\033[91mSe requiere atención médica inmediata.\033[0m")
    
    print("\nInterpretación general:")
    print("- 15: Estado normal de conciencia")
    print("- 13-14: Lesión leve, alerta y orientación normal o ligeramente alterada")
    print("- 9-12: Lesión moderada, desorientado pero consciente")
    print("- 3-8: Lesión grave, estado de coma, requiere intubación")
    print("- 3: Puntuación mínima, profundamente inconsciente")


def main():
    """Main function to run the GCS calculator."""
    try:
        while True:
            ojos, verbal, motora, total = calcular_gcs()
            mostrar_resultados(ojos, verbal, motora, total)
            
            continuar = input("\n¿Desea realizar otra evaluación? (s/n): ")
            if continuar.lower() not in ['s', 'si', 'sí', 'y', 'yes']:
                print("\n¡Gracias por utilizar la calculadora de GCS!")
                break
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido. Saliendo...")
    except Exception as e:
        print(f"\n\033[91mError inesperado: {e}\033[0m")
        print("Por favor, inténtelo de nuevo.")


if __name__ == "__main__":
    main()
