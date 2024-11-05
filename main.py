from datetime import datetime, timedelta


# Função para calcular a tabela SAC
def gerar_tabela_sac(valor_contrato, taxa_juros, num_parcelas, data_inicio):
    # Conversão da taxa de juros anual para mensal
    taxa_juros_mensal = taxa_juros / 100 / 12

    # Amortização constante
    amortizacao = valor_contrato / num_parcelas

    # Lista para armazenar os dados da tabela
    tabela = []

    saldo_devedor = valor_contrato
    data_pagamento = datetime.strptime(data_inicio, "%d/%m/%Y")

    for mes in range(1, num_parcelas + 1):
        # Cálculo dos juros do mês
        juros = saldo_devedor * taxa_juros_mensal

        # Valor da parcela (amortização + juros)
        parcela_total = amortizacao + juros

        # Atualização do saldo devedor
        saldo_devedor -= amortizacao

        # Armazenando os dados para cada mês
        tabela.append({
            "Mês": mes,
            "Data de Pagamento": data_pagamento.strftime("%d/%m/%Y"),
            "Amortização": round(amortizacao, 2),
            "Juros": round(juros, 2),
            "Parcela Total": round(parcela_total, 2),
            "Saldo Devedor": round(saldo_devedor, 2)
        })

        # Avançando para o próximo mês
        data_pagamento += timedelta(days=30)

    # Exibindo a tabela sem pandas
    print(
        f"{'Mês':<4} {'Data de Pagamento':<15} {'Amortização':<12} {'Juros':<8} {'Parcela Total':<14} {'Saldo Devedor'}")
    print("-" * 70)
    for row in tabela:
        print(
            f"{row['Mês']:<4} {row['Data de Pagamento']:<15} {row['Amortização']:<12} {row['Juros']:<8} {row['Parcela Total']:<14} {row['Saldo Devedor']}")


# Função principal
def main():
    # Entrada de dados
    valor_contrato = float(input("Digite o valor do contrato (ex: 10000): "))
    taxa_juros = float(input("Digite a taxa de juros anual (em %): "))
    num_parcelas = int(input("Digite o número de parcelas: "))
    data_inicio = input("Digite a data de início do pagamento (formato DD/MM/AAAA): ")

    # Gerar a tabela SAC
    gerar_tabela_sac(valor_contrato, taxa_juros, num_parcelas, data_inicio)


# Executar o programa
if __name__ == "__main__":
    main()
