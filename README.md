# TF05 - Sistema de Monitoramento e Automação

## Aluno

* **Nome:** Diogo Vieira Amorim
* **RA:** 6324639
* **Curso:** Análise e Desenvolvimento de Sistemas

---

## Funcionalidades

* Healthchecks inteligentes (HTTP, TCP, Database)
* Dashboard de monitoramento em tempo real
* Sistema de alertas (simulado via script)
* Automação completa de deploy
* Rollback automático
* Scripts de manutenção
* Backup automatizado

---

## Como Executar

### Pré-requisitos

* Docker
* Docker Compose
* Bash (Linux/Ubuntu)

---

### Execução Completa

```bash
git clone https://github.com/SEU_USUARIO/tfsImplantacaoSistemas2026.git
```
```bash
cd TF05_2026
```

# Permissões dos scripts
```bash
chmod +x scripts/*.sh
```
# Build automatizado
```bash
./scripts/build.sh
```
# Deploy automatizado
```bash
./scripts/deploy.sh
```

---

### Acessar o Sistema

* Dashboard: http://localhost:3000
* API Métricas: http://localhost:5000/metrics
* Health Check: http://localhost:5000/health

---

## Scripts Disponíveis

```bash
./scripts/build.sh          # Build automatizado
```
```bash
./scripts/deploy.sh         # Deploy da aplicação
```
```bash
./scripts/rollback.sh       # Rollback da aplicação
```
```bash
./scripts/backup.sh         # Backup dos dados
```
```bash
./scripts/cleanup.sh        # Limpeza de recursos Docker
```
```bash
./scripts/health-monitor.sh # Monitoramento manual
```

---

## Configuração

Arquivos localizados em:

* Healthchecks: `config/healthchecks.yml`
* Alertas: `config/alerts.yml`
* Thresholds: `config/thresholds.yml`

---

## Monitoramento

# Verificar status manual
```bash
./scripts/health-monitor.sh
```

---

## Estrutura do Projeto

```
TF05/
├── api/
├── dashboard/
├── database/
├── scripts/
├── config/
├── docs/
├── docker-compose.yml
└── README.md
```

---

## Tecnologias Utilizadas

* Python (Flask)
* Docker & Docker Compose
* Nginx (Dashboard)
* Bash (Automação)
* JavaScript (Frontend)

---

## Observações

* O sistema realiza monitoramento básico de saúde da API
* Métricas são armazenadas em memória para fins didáticos
* Alertas são simulados via scripts

---

## Autor

Desenvolvido por Diogo Vieira Amorim
