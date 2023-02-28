import sys

def somaDigitos(linha):
    total = 0
    n = ''
    for char in linha:
        if char.isdigit():
            n += char
        else:
            if n:
                total += int(n)
                n = ''
        if char.lower() == 'o' and linha.lower().startswith('off'):
            return None
        elif char.lower() == 'o' and linha.lower().startswith('on'):
            return total
    if n:
        total += int(n)
    return total

def main():
    somar = True
    for linha in sys.stdin:
        linha = linha.strip()
        if linha.lower() == 'off':
            somar = False
        elif linha.lower() == 'on':
            somar = True
        elif '=' in linha and somar:
            r = somaDigitos(linha)
            if r is not None:
                print(r)

main()
