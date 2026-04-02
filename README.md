# TF05 - Sistema de Monitoramento e Automação

## 👨‍🎓 Aluno

* **Nome:** Diogo Vieira Amorim
* **RA:** 6324639
* **Curso:** Análise e Desenvolvimento de Sistemas

---

## 🚀 Funcionalidades

* Healthchecks inteligentes (HTTP, TCP, Database)
* Dashboard de monitoramento em tempo real
* Sistema de alertas (simulado via script)
* Automação completa de deploy
* Rollback automático
* Scripts de manutenção
* Backup automatizado

---

## ⚙️ Como Executar

### 📋 Pré-requisitos

* Docker
* Docker Compose
* Bash (Linux/Ubuntu)

---

### ▶️ Execução Completa

```bash
git clone https://github.com/vieira-dih/TF05-Automacao-Avancada-Healthchecks.git
cd TF05-Automacao-Avancada-Healthchecks

# Dar permissão aos scripts
chmod +x scripts/*.sh

# Build automatizado
./scripts/build.sh

# Deploy automatizado
./scripts/deploy.sh
```

---

## 🌐 Acessar o Sistema

* Dashboard: http://localhost:3000
* API Métricas: http://localhost:5000/metrics
* Health Check: http://localhost:5000/health

---

## 🧪 Scripts Disponíveis

```bash
./scripts/build.sh          # Build automatizado
./scripts/deploy.sh         # Deploy da aplicação
./scripts/rollback.sh       # Rollback da aplicação
./scripts/backup.sh         # Backup dos dados
./scripts/cleanup.sh        # Limpeza de recursos Docker
./scripts/health-monitor.sh # Monitoramento manual
```

---

## 🔧 Configuração

Arquivos localizados em:

* `config/healthchecks.yml` → Configuração dos healthchecks
* `config/alerts.yml` → Configuração de alertas
* `config/thresholds.yml` → Limites de métricas

---

## 📊 Monitoramento

```bash
# Verificar status manual
./scripts/health-monitor.sh
```

---

## 🌳 Estrutura do Projeto

```
TF05-Automacao-Avancada-Healthchecks/
├── LICENSE
├── README.md
├── docker-compose.yml
│
├── api/
│   ├── Dockerfile
│   ├── app.py
│   ├── models/
│   │   ├── metrics.py
│   │   └── alerts.py
│   └── healthchecks/
│       ├── http_check.py
│       ├── db_check.py
│       └── custom_check.py
│
├── dashboard/
│   ├── Dockerfile
│   ├── index.html
│   ├── js/
│   │   ├── dashboard.js
│   │   └── charts.js
│   └── css/
│       └── dashboard.css
│
├── database/
│   ├── init.sql
│   └── migrations/
│
├── scripts/
│   ├── build.sh
│   ├── deploy.sh
│   ├── rollback.sh
│   ├── backup.sh
│   ├── cleanup.sh
│   └── health-monitor.sh
│
├── config/
│   ├── healthchecks.yml
│   ├── alerts.yml
│   └── thresholds.yml
│
└── docs/
    ├── automation.md
    ├── healthchecks.md
    └── maintenance.md
```

---

## 🛠️ Tecnologias Utilizadas

* Python (Flask)
* Docker & Docker Compose
* Nginx (Dashboard)
* Bash (Automação)
* JavaScript (Frontend)

---

## 📌 Observações

* O sistema realiza monitoramento básico de saúde da API
* Métricas são armazenadas em memória (modelo didático)
* Alertas são simulados via scripts

---

## 👨‍💻 Autor

Desenvolvido por **Diogo Vieira Amorim**
