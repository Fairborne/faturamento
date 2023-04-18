import json

with open(r'C:\Users\lsall\OneDrive\Documents\Projetos Python\dados.json') as arquivo:
    dados = json.load(arquivo)

faturamento_diario = []

for dia in dados:
    if dia['valor'] != 0:
        faturamento_diario.append(dia['valor'])

soma_faturamento = sum(faturamento_diario)
dias_vendas = len(faturamento_diario)

media_mensal = soma_faturamento / dias_vendas

maior_faturamento = max(faturamento_diario)
menor_faturamento = min(faturamento_diario)

dias_acima_media = sum(1 for faturamento in faturamento_diario if faturamento > media_mensal)
print(f"Menor valor de faturamento em um dia: R$ {menor_faturamento:.2f}.")
print(f"Maior valor de faturamento em um dia: R$ {maior_faturamento:.2f}.")
print(f"Número de dias em que o valor de faturamento diário foi superior à média mensal: {dias_acima_media:.2f}.")
