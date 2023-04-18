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
print(f"Menor valor de faturamento em um dia: R$ {round(menor_faturamento, 2)}.")
print(f"Maior valor de faturamento em um dia: R$ {round(maior_faturamento, 2)}.")
print(f"Número de dias em que o valor de faturamento diário foi superior à média mensal: {round(dias_acima_media, 2)}.")
