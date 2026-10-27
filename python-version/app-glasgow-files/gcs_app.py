#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Glasgow Coma Scale Calculator - App móvil
Desarrollado con Kivy para Android
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp

# Configuración de la ventana
Window.clearcolor = (0.95, 0.95, 0.95, 1)

class GCSCalculatorScreen(Screen):
    def __init__(self, **kwargs):
        super(GCSCalculatorScreen, self).__init__(**kwargs)
        self.eye_score = 4
        self.verbal_score = 5
        self.motor_score = 6
        
        # Layout principal
        main_layout = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))
        
        # Título
        title_label = Label(
            text='Calculadora de Escala de Coma de Glasgow (GCS)',
            font_size=dp(20),
            size_hint_y=None,
            height=dp(50),
            color=(0.2, 0.6, 0.8, 1)
        )
        main_layout.add_widget(title_label)
        
        # ScrollView para el contenido
        scroll_view = ScrollView()
        content_layout = BoxLayout(orientation='vertical', spacing=dp(15), size_hint_y=None)
        content_layout.bind(minimum_height=content_layout.setter('height'))
        
        # Sección de Apertura de Ojos
        content_layout.add_widget(self.create_section_title("Apertura de Ojos"))
        eye_options = [
            "4: Espontánea - Abre los ojos espontáneamente",
            "3: Al habla - Abre los ojos cuando se le habla",
            "2: Al dolor - Abre los ojos solo ante estímulos dolorosos",
            "1: Ninguna - No abre los ojos bajo ningún estímulo"
        ]
        self.eye_slider = self.create_slider_section(eye_options, 1, 4, self.eye_score, self.update_eye_score)
        content_layout.add_widget(self.eye_slider)
        
        # Sección de Respuesta Verbal
        content_layout.add_widget(self.create_section_title("Respuesta Verbal"))
        verbal_options = [
            "5: Orientada - Responde coherentemente",
            "4: Confusa - Responde de manera confusa o desorientada",
            "3: Palabras inapropiadas - Palabras reconocibles pero respuestas aleatorias",
            "2: Sonidos incomprensibles - Solo emite gemidos, quejidos o sonidos",
            "1: Ninguna - No emite sonidos"
        ]
        self.verbal_slider = self.create_slider_section(verbal_options, 1, 5, self.verbal_score, self.update_verbal_score)
        content_layout.add_widget(self.verbal_slider)
        
        # Sección de Respuesta Motora
        content_layout.add_widget(self.create_section_title("Respuesta Motora"))
        motor_options = [
            "6: Obedece órdenes - Sigue comandos simples",
            "5: Localiza el dolor - Intenta localizar/retirar el estímulo doloroso",
            "4: Retirada al dolor - Flexión normal, retira la parte estimulada",
            "3: Flexión anormal - Postura de decorticación (brazos flexionados)",
            "2: Extensión anormal - Postura de descerebración (brazos extendidos)",
            "1: Ninguna - No hay respuesta motora, flacidez"
        ]
        self.motor_slider = self.create_slider_section(motor_options, 1, 6, self.motor_score, self.update_motor_score)
        content_layout.add_widget(self.motor_slider)
        
        # Botón de cálculo
        calculate_button = Button(
            text='Calcular GCS',
            background_color=(0.2, 0.6, 0.8, 1),
            size_hint_y=None,
            height=dp(50)
        )
        calculate_button.bind(on_press=self.calculate_gcs)
        content_layout.add_widget(calculate_button)
        
        # Resultado
        self.result_layout = GridLayout(cols=2, size_hint_y=None, height=dp(200), spacing=dp(5))
        content_layout.add_widget(self.result_layout)
        
        # Añadir el contenido al scroll view
        scroll_view.add_widget(content_layout)
        main_layout.add_widget(scroll_view)
        
        self.add_widget(main_layout)
    
    def create_section_title(self, title):
        """Crea un título de sección con formato"""
        return Label(
            text=title,
            font_size=dp(18),
            halign='left',
            size_hint_y=None,
            height=dp(40),
            color=(0.2, 0.6, 0.8, 1)
        )
    
    def create_slider_section(self, options, min_value, max_value, default_value, callback):
        """Crea una sección con un slider y etiquetas de opciones"""
        layout = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(150))
        
        # Crear etiquetas para cada opción
        options_layout = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(30 * len(options)))
        for option in options:
            option_label = Label(
                text=option,
                halign='left',
                size_hint_y=None,
                height=dp(30),
                text_size=(Window.width - dp(40), dp(30))
            )
            options_layout.add_widget(option_label)
        layout.add_widget(options_layout)
        
        # Slider y valor actual
        slider_layout = BoxLayout(size_hint_y=None, height=dp(50))
        slider = Slider(min=min_value, max=max_value, value=default_value, step=1)
        slider.bind(value=callback)
        slider_layout.add_widget(slider)
        
        self.score_label = Label(text=str(default_value), size_hint_x=None, width=dp(50))
        slider_layout.add_widget(self.score_label)
        layout.add_widget(slider_layout)
        
        return layout
    
    def update_eye_score(self, instance, value):
        """Actualiza la puntuación de apertura de ojos"""
        self.eye_score = int(value)
        instance.parent.children[0].text = str(self.eye_score)
    
    def update_verbal_score(self, instance, value):
        """Actualiza la puntuación de respuesta verbal"""
        self.verbal_score = int(value)
        instance.parent.children[0].text = str(self.verbal_score)
    
    def update_motor_score(self, instance, value):
        """Actualiza la puntuación de respuesta motora"""
        self.motor_score = int(value)
        instance.parent.children[0].text = str(self.motor_score)
    
    def calculate_gcs(self, instance):
        """Calcula la puntuación total de GCS y muestra el resultado"""
        # Limpiar resultados anteriores
        self.result_layout.clear_widgets()
        
        # Calcular puntuación total
        total = self.eye_score + self.verbal_score + self.motor_score
        
        # Clasificar gravedad
        if total >= 13:
            severity = "Leve (Trauma craneal menor)"
            color = (0, 0.8, 0, 1)  # Verde
        elif total >= 9:
            severity = "Moderado (Requiere vigilancia)"
            color = (0.8, 0.8, 0, 1)  # Amarillo
        else:
            severity = "Grave (Estado crítico)"
            color = (0.8, 0, 0, 1)  # Rojo
        
        # Añadir resultados al layout
        self.add_result_row("Apertura de ojos:", f"{self.eye_score}/4")
        self.add_result_row("Respuesta verbal:", f"{self.verbal_score}/5")
        self.add_result_row("Respuesta motora:", f"{self.motor_score}/6")
        self.add_result_row("Puntuación total:", f"{total}/15", is_total=True)
        self.add_result_row("Clasificación:", severity, color=color)
        
        # Añadir advertencia si es grave
        if total <= 8:
            warning_label = Label(
                text="¡ADVERTENCIA! Puntuación indicativa de una lesión grave.\nSe requiere atención médica inmediata.",
                color=(0.8, 0, 0, 1),
                size_hint_y=None,
                height=dp(60),
                halign='center'
            )
            warning_label.text_size = (Window.width - dp(40), dp(60))
            self.result_layout.add_widget(warning_label)
            self.result_layout.add_widget(Label(text="", size_hint_y=None, height=dp(60)))
    
    def add_result_row(self, label_text, value_text, color=(0, 0, 0, 1), is_total=False):
        """Añade una fila de resultados al layout"""
        label = Label(
            text=label_text,
            halign='right',
            size_hint_y=None,
            height=dp(30)
        )
        label.text_size = (label.width, dp(30))
        
        value = Label(
            text=value_text,
            halign='left',
            size_hint_y=None,
            height=dp(30),
            color=color,
            bold=is_total
        )
        value.text_size = (value.width, dp(30))
        
        self.result_layout.add_widget(label)
        self.result_layout.add_widget(value)

class GCSApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(GCSCalculatorScreen(name='calculator'))
        return sm

if __name__ == '__main__':
    GCSApp().run()