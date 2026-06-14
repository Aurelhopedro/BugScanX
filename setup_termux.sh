#!/data/data/com.termux/files/usr/bin/bash

echo ""
echo "╔══════════════════════════════════════╗"
echo "║     BugScanX — Setup para Termux     ║"
echo "║     Por: Aurelhopedro (Angola)       ║"
echo "╚══════════════════════════════════════╝"
echo ""

# Atualizar pacotes
echo "📦 A atualizar pacotes..."
pkg update -y && pkg upgrade -y

# Instalar dependências base
echo "🐍 A instalar Python..."
pkg install python -y

echo "📡 A instalar dependências de rede..."
pkg install nmap -y
pkg install dnsutils -y

# Instalar dependências Python
echo "🔧 A instalar bibliotecas Python..."
pip install --upgrade pip
pip install requests colorama pyfiglet beautifulsoup4 dnspython loguru multithreading

echo ""
echo "✅ Instalação concluída!"
echo ""
echo "▶️  Para iniciar o BugScanX:"
echo "    python bugscanx.py"
echo ""
echo "🇦🇴 Bom trabalho!"
