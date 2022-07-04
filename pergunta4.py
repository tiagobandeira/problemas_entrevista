import json
with open("faturamento.json", encoding='utf-8') as file:
    dados = json.load(file)

faturamento_total = 0
for i in dados:
    faturamento_total += int(i["faturamento"])

print("Faturamento da Distribuidora (% do faturamento total em reais)")
for i in dados:
    percuntural = (float(i["faturamento"])/faturamento_total)*100
    print(i["estado"] , " - ", "%.2f %%" %percuntural)
file.close()