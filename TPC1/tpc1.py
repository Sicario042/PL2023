def carregarInfo(fnome):
    dados = []
    f = open(fnome)
    f.readline()
    for linha in f:
        myReg = {}
        novaLinha = linha.replace("\n","")
        campos = novaLinha.split(",")
        myReg['idade'] = campos[0]
        myReg['sexo'] = campos[1]
        myReg['tensão'] = campos[2]
        myReg['colesterol'] = campos[3]
        myReg['batimento'] = campos[4]
        myReg['temDoença'] = campos[5]
        dados.append(myReg)
    return dados


def distribuicaoPorSexo(dados):
    res = {'Homem': {'com_doenca': 0, 'sem_doenca': 0},
           'Mulher': {'com_doenca': 0, 'sem_doenca': 0}}

    for pessoa in dados:
        if pessoa.get('temDoença') == '1':
            if pessoa['sexo'] == 'M':
                res['Homem']['com_doenca'] += 1
            elif pessoa['sexo'] == 'F':
                res['Mulher']['com_doenca'] += 1
        elif pessoa.get('temDoença') == '0':
            if pessoa['sexo'] == 'M':
                res['Homem']['sem_doenca'] += 1
            elif pessoa['sexo'] == 'F':
                res['Mulher']['sem_doenca'] += 1

    return res

def distribuicaoPorIdade(dados):
    idades=[]
    for pessoa in dados:
        idades.append(int(pessoa['idade']))
    idadeMax = max(idades)
    faixasEtarias = {}
    for a in range(30, idadeMax, 5):
        faixa = f"{a}-{a+4}"
        faixasEtarias[faixa] = {'com_doenca': 0, 'sem_doenca': 0}
        for pessoa in dados:
            idade = int(pessoa['idade'])
            temDoenca = pessoa['temDoença'] == '1'
            if a <= idade <= a+4:
                if temDoenca:
                    faixasEtarias[faixa]['com_doenca'] += 1
                else:
                    faixasEtarias[faixa]['sem_doenca'] += 1
    return faixasEtarias

def distribuicaoPorColesterol(dados):
    col=[]
    for pessoa in dados:
        col.append(int(pessoa['colesterol']))
    colMin=min(col)
    colMax=max(col)
    nivCol = {}
    for c in range(colMin, colMax, 10):
        faixa = f"{c}-{c+9}"
        nivCol[faixa] = {'com_doenca': 0, 'sem_doenca': 0}
        for pessoa in dados:
            colesterol = int(pessoa['colesterol'])
            temDoenca = pessoa['temDoença'] == '1'
            if c <= colesterol <= c+9:
                if temDoenca:
                    nivCol[faixa]['com_doenca'] += 1
                else:
                    nivCol[faixa]['sem_doenca'] += 1
    return nivCol

        
def imprimirDistSexo(dist):
    print("{:<10} {:<15} {:<15}".format('Sexo', 'Com Doença', 'Sem Doença'))
    for sexo, valores in dist.items():
        com_doenca = valores.get('com_doenca', 0)
        sem_doenca = valores.get('sem_doenca', 0)
        print("{:<10} {:<15} {:<15}".format(sexo, com_doenca, sem_doenca))
        
def imprimirDistIdades(dist):
    print("{:<10} {:<15} {:<15}".format('Faixa', 'Com Doença', 'Sem Doença'))
    for faixa, valores in dist.items():
        com_doenca = valores.get('com_doenca', 0)
        sem_doenca = valores.get('sem_doenca', 0)
        print("{:<10} {:<15} {:<15}".format(faixa, com_doenca, sem_doenca))
        
def imprimirDistColesterol(dist):
    print("{:<10} {:<15} {:<15}".format('Nivel', 'Com Doença', 'Sem Doença'))
    for nivel, valores in dist.items():
        com_doenca = valores.get('com_doenca', 0)
        sem_doenca = valores.get('sem_doenca', 0)
        print("{:<10} {:<15} {:<15}".format(nivel, com_doenca, sem_doenca))
        
def main():
    dados=carregarInfo("myheart.csv")
    r=input("Qual a distribuição que quer?\n1-Doença por sexo\n2-Doença por idades\n3-Doença por colesterol\n")
    if r=='1':
        imprimirDistSexo(distribuicaoPorSexo(dados))
    elif r=='2':
        imprimirDistIdades(distribuicaoPorIdade (dados))
    elif r=='3':
        imprimirDistColesterol(distribuicaoPorColesterol (dados))
    
main()
