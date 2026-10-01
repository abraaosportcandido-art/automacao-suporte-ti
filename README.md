Markdown
# 🚀 Automador de Suporte Técnico & Infraestrutura (Python)

Projeto desenvolvido para automatizar tarefas repetitivas de suporte de TI, unindo auditoria de máquinas, salvaguarda de dados e gestão administrativa em um único fluxo em Python.

## 🛠️ Tecnologias Utilizadas
* **Python** (Bibliotecas nativas e externas: `os`, `shutil`, `psutil`, `csv`, `platform`, `datetime`).
* **Git & GitHub** para versionamento de código e portfólio.

## 📋 Funcionalidades Principais
1. **Auditoria de Máquina:** Coleta informações cruciais do sistema operacional, nome do host e espaço livre em disco, gerando relatórios automatizados (`.txt`).
2. **Rotina de Backup Seguro:** Compacta pastas indicadas pelo usuário em formato `.zip` com registro de logs detalhados de execução.
3. **Gestão de Usuários em Lote:** Processa cadastros de novos colaboradores através de planilhas estruturadas em CSV.

## 💻 Como Executar
1. Certifique-se de ter o Python instalado na sua máquina.
2. Instale a dependência de sistema necessária:
   ```bash
   pip install psutil
