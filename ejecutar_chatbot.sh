#!/bin/bash
# Script para ejecutar el chatbot básico
# Uso: ./ejecutar_chatbot.sh

echo "Iniciando Chatbot Básico..."
echo "========================================="

# Verificar que Python esté instalado
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 no está instalado."
    echo "Por favor instala Python 3 para usar este chatbot."
    exit 1
fi

# Ejecutar el chatbot
python3 chatbot.py