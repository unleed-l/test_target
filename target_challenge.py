import json


def readInt():
    option = None
    while(option is None):
        try:
            option = int(input())
            if option < 0: raise ''
        except:
            print('Entrada inválida. Por favor, digite um número inteiro positivo.')
            continue
    return option
    
def fibonacci():
    # primeiros números da sequência
    x,y = 0, 1

    # Leitura do número
    print('Informe o número a ser verificado:')
    value = readInt()
    sequence = []
    contains = False

    while x <= value:
        sequence.append(x)
        if x == value:
            contains = True
        x,y = y, x + y

    print(', '.join(map(str, sequence)))
    print(f'O número {'' if contains else 'não '}pertence à sequência de Fibonacci')

def faturamento():
    # Leitura de json de dados
    data = None
    try:
        with open('dados.json', 'r') as arquivo:
            data = json.load(arquivo)
        if data is None: return print('Não foi possível ler o arquivo dados.json')
    except:
        return print('Não foi possível ler o arquivo dados.json')
    
    # Inicialização de dados
    menor_valor = data[0]
    maior_valor = menor_valor
    soma = menor_valor['valor']
    dias_nao_zerados = 0

    # Obtenção de dados
    for d in data:
        soma += d['valor']
        if d['valor'] > 0: dias_nao_zerados += 1
        if d['valor'] < menor_valor['valor']: menor_valor = d
        if d['valor'] > maior_valor['valor']: maior_valor = d

    # Impressão de resultados
    print(f'O dia {menor_valor['dia']} foi o dia com menor faturamento ({menor_valor['valor']:.2f})')
    print(f'O dia {maior_valor['dia']} foi o dia com maior faturamento ({maior_valor['valor']:.2f})')
    media = soma / dias_nao_zerados
    print(f'Dias com faturamento acima da média ({media:.2f}):')
    for d in data:
        if(d['valor'] > media): print(f'Dia {d['dia']}: {d['valor']:.2f}')

def faturamentoMensal():
    data = [
        {
            'state': 'SP',
            'value': 67836.43,
            'percent': None,
        },
        {
            'state': 'RJ',
            'value': 36678.66,
            'percent': None,
        },
        {
            'state': 'MG',
            'value': 29229.88,
            'percent': None,
        },
        {
            'state': 'ES',
            'value': 27165.48,
            'percent': None,
        },
        {
            'state': 'Outros',
            'value': 19849.53,
            'percent': None,
        },
    ]
    tot = 0
    for d in data:
        tot += d['value']
    print('Percentuais:')
    for d in data:
        d['percent'] = d['value'] / tot * 100
        print(f'{d['state']}: {d['percent']:.2f}%')
    
def invertStr():
    print('Informe a string a ser invertida:')
    string = input()
    length = len(string)
    reversed = ''
    for i in range(length - 1, -1, -1):
        reversed += string[i]
    print('String invertida:')
    print(reversed)

def main():
    while True:
        print('Escolha uma opção:')
        print('1 - Questão 2')
        print('2 - Questão 3')
        print('3 - Questão 4')
        print('4 - Questão 5')
        print('0 - Sair')

        option = readInt()

        if option == 1:
            fibonacci()
            break
        elif option == 2:
            faturamento()
            break
        elif option == 3:
            faturamentoMensal()
            break
        elif option == 4:
            invertStr()
            break
        elif option == 0:
            print('Saindo...')
            break
        else:
            print('Opção inválida. Por favor, escolha um número entre 0 e 4.')

if __name__ == '__main__':
    main()