# 💰 Controle Financeiro em Python

Um sistema simples de **controle financeiro** feito em **Python**, onde é possível registrar **receitas** e **despesas**, visualizar transações, consultar saldo total e gerar um **relatório mensal**.

Este projeto foi desenvolvido com foco em prática de lógica de programação, estruturas de dados, manipulação de arquivos JSON e criação de menus interativos no terminal.

---

## 🚀 Funcionalidades

✅ Adicionar receitas  
✅ Adicionar despesas  
✅ Listar todas as transações registradas  
✅ Calcular saldo total automaticamente  
✅ Gerar relatório mensal (receitas, despesas e saldo do mês)  
✅ Salvamento automático em arquivo JSON  
✅ Data registrada automaticamente em cada transação  

---

## 🛠️ Tecnologias utilizadas

- Python 3
- JSON (armazenamento de dados)
- Biblioteca `datetime`

---

## 📋 Como funciona

Ao rodar o programa, um menu aparece no terminal:

=== CONTROLE FINANCEIRO ===
- 1 - Adicionar Receita
- 2 - Adicionar Despesa
- 3 - Listar Transações
- 4 - Ver Saldo Total
- 5 - Relatório Mensal
- 6 - Sair


Basta escolher a opção desejada e seguir as instruções.

## 📊 Relatório Mensal

O relatório mensal permite consultar transações de um mês específico, exibindo:

- 📌 Total de receitas
- 📌 Total de despesas
- 📌 Saldo do mês
- 📌 Lista completa das transações filtradas

Exemplo:

📊 RELATÓRIO MENSAL
- Mês/Ano: 02/2026
- Total de Receitas: R$ 2000.00
- Total de Despesas: R$ 650.00
- Saldo do mês: R$ 1350.00

## 💾 Salvamento automático

Todas as transações são salvas automaticamente em um arquivo chamado:

📌 transacoes.json

Isso permite que os dados permaneçam salvos mesmo após fechar o programa.
