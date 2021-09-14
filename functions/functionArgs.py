def func_args(*args):
    print(f'tipo: {type(args)} conteudo: {args}')

    for arg in args:
        print(f'tipo: {type(arg)} conteudo: {arg}')


func_args(1, 'A', {'valor': 10},2, 'B', {'valor': 22})


def func_kwargs(**kwargs):
    print(f'tipo: {type(kwargs)} conteudo: {kwargs}')

    for key,value  in kwargs.items():
        print(f'atributo; {key} valor: {value}')
        
parms = {
    'nome' : 'James',
    'sobrenome' : 'Lennister',
    'cargo' : 'Cavaleiro',
    'nome' : 'Alexander',
    'sobrenome' : 'The great',
    'cargo' : 'Imperator'
}
        
#func_kwargs(nome="Bill", sobrenome="O grande", cargo="pedreiro")
#func_kwargs(**parms)