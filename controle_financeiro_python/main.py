import json
from datetime import datetime

def salvar_transacoes(transacoes):
    with open("transacoes.json", "w", encoding="utf-8") as arquivo:
        json.dump(transacoes, arquivo, ensure_ascii=False, indent=4)

def carregar_transacoes():
    try:
        with open("transacoes.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
transacoes = carregar_transacoes()

while True:
    print("\n=== CONTROLE FINANCEIRO ===")
    print("1 - Adicionar Receita")
    print("2 - Adicionar Despesa")
    print("3 - Listar Transações")
    print("4 - Ver Saldo")
    print("5 - Relatório Mensal")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    # 1 - Receita
    if opcao == "1":
        descricao = input("Descrição de sua receita: ")
        valor = float(input("Valor: R$ "))

        data = datetime.now().strftime("%Y-%m-%d")

        transacao = {"tipo": "receita", "descricao": descricao, "valor": valor, "data": data}

        transacoes.append(transacao)
        salvar_transacoes(transacoes)

        print("Receita adcionada com sucesso!")

    # 2 - Despesa
    elif opcao == "2":
        descricao = input("Descrição da despesa: ")
        valor = float(input("Valor: R$ ")) 
        data = datetime.now().strftime("%Y-%m-%d")

        transacao = {"tipo": "despesa", "descricao": descricao, "valor": valor, "data": data}  
        transacoes.append(transacao)
        salvar_transacoes(transacoes)

        print("Despesa adcionada com sucesso!")

    # 3 - Listar transações
    elif opcao == "3":
        if len(transacoes) == "0":
            print("Nenhuma transação registrada!")
        else: 
            print("\n--- Transações ---")
            for i, t in enumerate(transacoes):
                print(f"{i+1} - {t['data']} | {t['tipo'].upper()} | {t['descricao']} | R$ {t['valor']:.2f}")

    # 4 - Saldo total
    elif opcao == "4":
        saldo = 0

        for t in transacoes:
            if t["tipo"] == "receita":
                saldo += t["valor"]
            else:
                saldo -= t["valor"]

        print(f"\n💰 Saldo atual: R$ {saldo:.2f}")

    # 5 - Relatório mensal
    elif opcao == "5":
        mes = input("Digite o mês (01 a 12): ")
        ano = input("Digite o ano (ex: 2026): ")

        filtro = f"{ano} - {mes}"

        total_receitas = 0
        total_despesas = 0

        print("\n--- Transações do mês ---")

        encontrou = False

        for t in transacoes:
            if t ["data"].startswith(filtro):
                encontrou = True
                print(f"{t['data']} | {t['tipo'].upper()} | {t['descricao']} | R$ {t['valor']:.2f}")

                if t["tipo"] == "receita":
                    total_receitas += t["valor"]
                else:
                    total_despesas += t["valor"]
        if not encontrou:
            print("Nenhuma tansação encontrada nesse mês!")
        else:
            saldo_mes = total_receitas - total_despesas

            print("\n📊 RELATÓRIO MENSAL")
            print(f"Mês/Ano: {mes}/{ano}")
            print(f"Total de Receitas: R$ {total_receitas:.2f}")
            print(f"Total de Despesas: R$ {total_despesas:.2f}")
            print(f"Saldo do mês: R$ {saldo_mes:.2f}")

    elif opcao == "6":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")