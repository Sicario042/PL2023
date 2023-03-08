import re

frequencia_por_ano = {}

with open('processos.txt', 'r') as arquivo:
    for linha in arquivo:
        ano = re.search(r'^\d+::(\d{4})', linha)
        if ano:
            frequencia_por_ano[ano.group(1)] = frequencia_por_ano.get(ano.group(1), 0) + 1

for ano, frequencia in frequencia_por_ano.items():
    print(f'Ano {ano}: {frequencia} processos')