#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Glasgow Coma Scale Calculator - Versión Web
Aplicación web interactiva con Streamlit
"""

import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Calculadora GCS",
    page_icon="🏥",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS personalizado para mejorar la apariencia
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stButton>button {
        background-color: #3498db;
        color: white;
        font-size: 18px;
        font-weight: bold;
        padding: 10px 24px;
        border-radius: 8px;
        border: none;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #2980b9;
    }
    h1 {
        color: #2c3e50;
        text-align: center;
    }
    h2 {
        color: #3498db;
    }
    .resultado-box {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

def clasificar_gravedad(total):
    """
    Clasificar severidad basada en el puntaje total de GCS
    
    Args:
        total (int): Puntaje total de GCS
        
    Returns:
        tuple: Clasificación string y color
    """
    if total >= 13:
        return "Leve (Trauma craneal menor)", "🟢", "#27ae60"
    elif total >= 9:
        return "Moderado (Requiere vigilancia)", "🟡", "#f39c12"
    else:
        return "Grave (Estado crítico)", "🔴", "#e74c3c"

def main():
    # Título principal
    st.markdown("# 🏥 Calculadora de Escala de Coma de Glasgow (GCS)")
    st.markdown("---")
    
    # Descripción
    st.markdown("""
    Esta herramienta permite evaluar el nivel de conciencia en pacientes con daño cerebral,
    basándose en tres criterios fundamentales.
    """)
    
    st.markdown("### 📋 Evaluación del paciente")
    
    # Crear tres columnas para mejor organización
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Sección 1: Apertura de Ojos
        st.markdown("#### 👁️ Apertura de Ojos")
        eye_options = {
            4: "Espontánea - Abre los ojos espontáneamente",
            3: "Al habla - Abre los ojos cuando se le habla",
            2: "Al dolor - Abre los ojos solo ante estímulos dolorosos",
            1: "Ninguna - No abre los ojos bajo ningún estímulo"
        }
        eye_score = st.select_slider(
            "Seleccione el nivel de apertura ocular:",
            options=[4, 3, 2, 1],
            value=4,
            format_func=lambda x: f"{x} - {eye_options[x].split(' - ')[1]}"
        )
        st.info(f"**Seleccionado:** {eye_options[eye_score]}")
        
        st.markdown("---")
        
        # Sección 2: Respuesta Verbal
        st.markdown("#### 🗣️ Respuesta Verbal")
        verbal_options = {
            5: "Orientada - Responde coherentemente",
            4: "Confusa - Responde de manera confusa o desorientada",
            3: "Palabras inapropiadas - Palabras reconocibles pero respuestas aleatorias",
            2: "Sonidos incomprensibles - Solo emite gemidos, quejidos o sonidos",
            1: "Ninguna - No emite sonidos"
        }
        verbal_score = st.select_slider(
            "Seleccione el nivel de respuesta verbal:",
            options=[5, 4, 3, 2, 1],
            value=5,
            format_func=lambda x: f"{x} - {verbal_options[x].split(' - ')[1]}"
        )
        st.info(f"**Seleccionado:** {verbal_options[verbal_score]}")
        
        st.markdown("---")
        
        # Sección 3: Respuesta Motora
        st.markdown("#### 💪 Respuesta Motora")
        motor_options = {
            6: "Obedece órdenes - Sigue comandos simples",
            5: "Localiza el dolor - Intenta localizar/retirar el estímulo doloroso",
            4: "Retirada al dolor - Flexión normal, retira la parte estimulada",
            3: "Flexión anormal - Postura de decorticación (brazos flexionados)",
            2: "Extensión anormal - Postura de descerebración (brazos extendidos)",
            1: "Ninguna - No hay respuesta motora, flacidez"
        }
        motor_score = st.select_slider(
            "Seleccione el nivel de respuesta motora:",
            options=[6, 5, 4, 3, 2, 1],
            value=6,
            format_func=lambda x: f"{x} - {motor_options[x].split(' - ')[1]}"
        )
        st.info(f"**Seleccionado:** {motor_options[motor_score]}")
    
    with col2:
        st.markdown("#### 📊 Resumen")
        st.metric("Apertura de Ojos", f"{eye_score}/4")
        st.metric("Respuesta Verbal", f"{verbal_score}/5")
        st.metric("Respuesta Motora", f"{motor_score}/6")
    
    st.markdown("---")
    
    # Botón de calcular (siempre visible)
    if st.button("🔍 Calcular GCS", use_container_width=True):
        st.session_state.calculated = True
    
    # Inicializar el estado
    if 'calculated' not in st.session_state:
        st.session_state.calculated = True
    
    # Mostrar resultados siempre
    if st.session_state.calculated:
        # Calcular total
        total = eye_score + verbal_score + motor_score
        clasificacion, emoji, color = clasificar_gravedad(total)
        
        # Mostrar resultados en un contenedor destacado
        st.markdown("## 📈 Resultados de la Evaluación")
        
        # Crear tres columnas para los resultados
        res_col1, res_col2, res_col3 = st.columns(3)
        
        with res_col1:
            st.metric("Apertura de ojos", f"{eye_score}/4")
        with res_col2:
            st.metric("Respuesta verbal", f"{verbal_score}/5")
        with res_col3:
            st.metric("Respuesta motora", f"{motor_score}/6")
        
        # Resultado total con estilo
        st.markdown("### 🎯 Puntuación Total")
        st.markdown(f"<h1 style='text-align: center; color: {color}; font-size: 60px;'>{emoji} {total}/15</h1>", 
                   unsafe_allow_html=True)
        
        # Clasificación
        st.markdown(f"<h2 style='text-align: center; color: {color};'>{clasificacion}</h2>", 
                   unsafe_allow_html=True)
        
        # Advertencia si es grave
        if total <= 8:
            st.error("""
            ⚠️ **¡ADVERTENCIA!** Puntuación indicativa de una lesión grave.  
            **Se requiere atención médica inmediata.**
            """)
        elif total <= 12:
            st.warning("⚠️ Paciente requiere vigilancia médica continua.")
        else:
            st.success("✅ Trauma craneal menor. Monitoreo regular recomendado.")
        
        # Interpretación general
        st.markdown("---")
        st.markdown("### 📚 Interpretación de la Escala GCS")
        
        interpretation_col1, interpretation_col2 = st.columns(2)
        
        with interpretation_col1:
            st.markdown("""
            **Rangos de Puntuación:**
            - 🟢 **15:** Estado normal de conciencia
            - 🟢 **13-14:** Lesión leve, alerta
            - 🟡 **9-12:** Lesión moderada
            - 🔴 **3-8:** Lesión grave, coma
            - 🔴 **3:** Profundamente inconsciente
            """)
        
        with interpretation_col2:
            st.markdown(f"""
            **Tu paciente:**
            - Puntuación: **{total}/15**
            - Categoría: **{clasificacion.split('(')[0].strip()}**
            - Estado: {emoji}
            """)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #7f8c8d; font-size: 12px;'>
    <p><strong>Nota importante:</strong> Esta herramienta está diseñada como ayuda para profesionales médicos y estudiantes.<br>
    No reemplaza el juicio clínico profesional. La Escala de Coma de Glasgow es parte de una evaluación más amplia del paciente.</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
