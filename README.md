# BugScanX 🇦🇴
### Fork por Aurelhopedro — Adaptado para Angola

Ferramenta de análise de segurança de rede para identificar misconfigurações SNI em operadoras. Este fork foi adaptado para uso em Android (Termux) com foco na rede Unitel Angola.

---

## 📱 Instalação no Android (Termux)

```bash
# 1. Instalar Termux (F-Droid recomendado)
# 2. Clonar o repositório
pkg install git -y
git clone https://github.com/Aurelhopedro/BugScanX
cd BugScanX

# 3. Correr o script de setup
bash setup_termux.sh

# 4. Iniciar
python bugscanx.py
```

---

## 🚀 Funcionalidades

| Opção | Função |
|-------|--------|
| 1 | ⚡ Host Scanner |
| 2 | 🖥️ Scanner de Subdomínios |
| 3 | 📡 Scanner de IPs |
| 4 | 🌐 Encontrar Subdomínios |
| 5 | 🔍 Domínios no mesmo IP |
| 6 | ✂️ TXT Toolkit |
| 7 | 🔓 Verificar Portas Abertas |
| 8 | 📜 Registos DNS |
| 9 | 🔬 OSINT do Host |

---

## 🎯 Uso com Unitel Angola

Para análise da rede Unitel, usa o ficheiro incluído:

```bash
# No Host Scanner, quando pedir o ficheiro de hosts:
unitel_hosts.txt

# Modo recomendado para SNI:
ssl

# Threads recomendadas no Android:
10
```

---

## ⚠️ Aviso Legal

Esta ferramenta é para fins de **investigação de segurança e divulgação responsável** apenas. Os resultados devem ser reportados às operadoras para melhoria da sua infraestrutura.

---

## 👤 Autor do Fork

**Aurélio Machai** — Benguela, Angola  
GitHub: [@Aurelhopedro](https://github.com/Aurelhopedro)

Baseado em [pddung93/BugScanX](https://github.com/pddung93/BugScanX)
