# Chatbot Básico

Un chatbot simple y eficiente que requiere pocos recursos del sistema.

## Descripción

Este es un chatbot básico desarrollado en Python que utiliza únicamente la biblioteca estándar, lo que significa que no requiere instalaciones adicionales ni consume muchos recursos del sistema. Es perfecto para sistemas con recursos limitados o para aprender los conceptos básicos de un chatbot.

## Características

- **Recursos mínimos**: Solo usa la biblioteca estándar de Python
- **Interfaz simple**: Funciona por línea de comandos
- **Respuestas inteligentes**: Reconoce palabras clave y responde apropiadamente
- **Multiidioma**: Diseñado para español pero fácil de modificar
- **Funciones útiles**: Puede mostrar fecha, hora y dar información básica

## Requisitos del Sistema

- Python 3.6 o superior
- Aproximadamente 50KB de espacio en disco
- Mínimo uso de RAM (menos de 10MB)

## Instalación

1. Clona este repositorio o descarga los archivos
2. No necesitas instalar dependencias adicionales

## Uso

### Opción 1: Ejecutar directamente
```bash
python3 chatbot.py
```

### Opción 2: Usar el script de ejecución
```bash
./ejecutar_chatbot.sh
```

## Comandos Disponibles

El chatbot reconoce las siguientes palabras clave:

- **Saludos**: "hola", "buenos", "buenas", "saludo"
- **Despedidas**: "adiós", "adios", "chau", "hasta", "bye"
- **Información**: "tiempo", "fecha", "hora", "nombre", "version"
- **Ayuda**: "ayuda"
- **Salir**: "salir", "exit", "quit"

## Ejemplos de Conversación

```
Tú: hola
ChatBot Básico: ¡Hola! ¿Cómo estás?

Tú: ¿cuál es tu nombre?
ChatBot Básico: Mi nombre es ChatBot Básico

Tú: ¿qué hora es?
ChatBot Básico: Son las 14:30

Tú: ayuda
ChatBot Básico: Puedo responder saludos, despedidas, y charlar contigo.

Tú: salir
ChatBot Básico: ¡Hasta luego! Que tengas un buen día.
```

## Personalización

Puedes personalizar el chatbot modificando el archivo `chatbot.py`:

1. **Agregar nuevas respuestas**: Modifica las listas `saludos`, `despedidas`, etc.
2. **Añadir palabras clave**: Agrega entradas al diccionario `palabras_clave`
3. **Cambiar el nombre**: Modifica la variable `self.nombre`

## Ventajas

- **Ligero**: Consume muy pocos recursos
- **Rápido**: Respuestas inmediatas
- **Simple**: Fácil de entender y modificar
- **Portable**: Funciona en cualquier sistema con Python
- **Sin dependencias**: No requiere instalaciones adicionales

## Limitaciones

- Respuestas predefinidas (no usa IA)
- No aprende de las conversaciones
- Reconocimiento básico de palabras clave
- Interfaz solo por línea de comandos

## Mejoras Futuras Posibles

- Interfaz gráfica simple
- Más palabras clave y respuestas
- Guardado de conversaciones
- Personalización de usuario
- Integración con servicios web básicos

## Contribución

Este es un proyecto educativo simple. Siéntete libre de hacer mejoras manteniendo la filosofía de usar pocos recursos.

## Licencia

Proyecto educativo - Uso libre para aprendizaje.