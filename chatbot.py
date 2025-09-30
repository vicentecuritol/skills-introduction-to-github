#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chatbot Básico - Un chatbot simple que requiere pocos recursos
Autor: Creado para el repositorio skills-introduction-to-github
"""

import sys
import random
import datetime

class ChatbotBasico:
    def __init__(self):
        """Inicializa el chatbot con respuestas predefinidas"""
        self.nombre = "ChatBot Básico"
        self.version = "1.0"
        
        # Respuestas predefinidas para ahorrar recursos
        self.saludos = [
            "¡Hola! ¿Cómo estás?",
            "¡Saludos! ¿En qué puedo ayudarte?",
            "¡Hola! Es un placer hablar contigo.",
            "¡Buenos días! ¿Cómo te encuentras?"
        ]
        
        self.despedidas = [
            "¡Hasta luego! Que tengas un buen día.",
            "¡Adiós! Espero haberte ayudado.",
            "¡Nos vemos! Cuídate mucho.",
            "¡Hasta pronto! Ha sido un placer."
        ]
        
        self.respuestas_genericas = [
            "Eso es interesante. Cuéntame más.",
            "Entiendo lo que dices.",
            "Es una perspectiva interesante.",
            "Me parece bien lo que comentas.",
            "¿Podrías darme más detalles?",
            "Eso suena bien."
        ]
        
        self.palabras_clave = {
            'hola': self.saludos,
            'buenos': self.saludos,
            'buenas': self.saludos,
            'saludo': self.saludos,
            'adiós': self.despedidas,
            'adios': self.despedidas,
            'chau': self.despedidas,
            'hasta': self.despedidas,
            'bye': self.despedidas,
            'tiempo': ["Hoy es " + datetime.datetime.now().strftime("%d/%m/%Y")],
            'fecha': ["La fecha actual es " + datetime.datetime.now().strftime("%d/%m/%Y")],
            'hora': ["Son las " + datetime.datetime.now().strftime("%H:%M")],
            'nombre': [f"Mi nombre es {self.nombre}"],
            'version': [f"Soy la versión {self.version}"],
            'ayuda': [
                "Puedo responder saludos, despedidas, y charlar contigo.",
                "Intenta preguntarme sobre la hora, fecha, o simplemente conversa conmigo.",
                "Escribe 'salir' para terminar la conversación."
            ]
        }
    
    def procesar_mensaje(self, mensaje):
        """Procesa un mensaje y devuelve una respuesta"""
        mensaje = mensaje.lower().strip()
        
        # Comando especial para salir
        if mensaje in ['salir', 'exit', 'quit']:
            return None
        
        # Buscar palabras clave en el mensaje
        for palabra, respuestas in self.palabras_clave.items():
            if palabra in mensaje:
                return random.choice(respuestas)
        
        # Si no encuentra palabras clave, usar respuesta genérica
        return random.choice(self.respuestas_genericas)
    
    def iniciar_conversacion(self):
        """Inicia la conversación con el usuario"""
        print(f"\n=== {self.nombre} v{self.version} ===")
        print("¡Hola! Soy un chatbot básico y eficiente.")
        print("Puedes conversar conmigo o escribir 'ayuda' para más información.")
        print("Escribe 'salir' para terminar.\n")
        
        while True:
            try:
                # Obtener entrada del usuario
                entrada = input("Tú: ").strip()
                
                if not entrada:
                    continue
                
                # Procesar el mensaje
                respuesta = self.procesar_mensaje(entrada)
                
                # Si la respuesta es None, es momento de salir
                if respuesta is None:
                    print(f"{self.nombre}: " + random.choice(self.despedidas))
                    break
                
                # Mostrar la respuesta
                print(f"{self.nombre}: {respuesta}")
                
            except KeyboardInterrupt:
                print(f"\n{self.nombre}: " + random.choice(self.despedidas))
                break
            except EOFError:
                print(f"\n{self.nombre}: " + random.choice(self.despedidas))
                break

def main():
    """Función principal"""
    chatbot = ChatbotBasico()
    chatbot.iniciar_conversacion()

if __name__ == "__main__":
    main()