#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demo del Chatbot Básico - Muestra las capacidades del chatbot
"""

from chatbot import ChatbotBasico
import time

def demo_automatico():
    """Ejecuta una demostración automática del chatbot"""
    print("=== DEMOSTRACIÓN AUTOMÁTICA DEL CHATBOT ===\n")
    
    # Crear instancia del chatbot
    bot = ChatbotBasico()
    
    # Lista de mensajes de prueba
    mensajes_prueba = [
        "hola",
        "¿cuál es tu nombre?",
        "¿qué hora es?",
        "ayuda",
        "¿cómo estás?",
        "adiós"
    ]
    
    print(f"Iniciando demostración con {bot.nombre} v{bot.version}\n")
    
    for mensaje in mensajes_prueba:
        print(f"Usuario: {mensaje}")
        
        # Procesar mensaje (excepto el último que es de despedida)
        if mensaje == "adiós":
            respuesta = bot.procesar_mensaje(mensaje)
        else:
            respuesta = bot.procesar_mensaje(mensaje)
        
        print(f"{bot.nombre}: {respuesta}")
        print("-" * 50)
        time.sleep(1)  # Pausa para hacer más legible la demo
    
    print("\n=== FIN DE LA DEMOSTRACIÓN ===")
    print("Para usar el chatbot interactivamente, ejecuta: python3 chatbot.py")

if __name__ == "__main__":
    demo_automatico()