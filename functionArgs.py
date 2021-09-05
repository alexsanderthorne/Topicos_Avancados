def function_Args(nome, *args, funcao='coraleiro', **kwargs):
    print(f'Nome : {nome}')
    print(f'Funcao: {funcao}')
    print(args)
    print(kwargs)


params = {
    'id': '9',
    'proxima_meta': "invadir a nasa"}

function_Args('Joe', 'Go', 'Away', **params)
