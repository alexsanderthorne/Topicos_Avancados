
numeros = [0, 1, 2, 3, 4, 5, 6]
j, k, *r = numeros

print(r)

*r, j, k = numeros

print(r)

j, *r, k = numeros
print(r)


def maior(n1, n2):
    if n1 > n2:
        return n1
    return n2


n = [4, 9]
maiorNumero = maior(*n)
#print(maiorNumero)

def escreveMensagem(mensagem, nome):
    print(f'{mensagem},{nome}')

mensagem = {'mensagem': 'Hello', 'nome': 'joe ok'}

escreveMensagem(**mensagem)

moovies = {'Nome': 'zombie', 'Ano': '1993', 'Nome': 'swat',
           'Ano': '2013', 'Nome': 'transcedence', 'Ano': '2024'}


def functionMoovies(**extra):
    for key, value in extra.items():
        print(f' {key} : {value}')


#functionMoovies(**moovies)
