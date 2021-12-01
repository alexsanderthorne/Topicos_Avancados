class Exceptions:

    def func():
        raise ConnectionError

    try:
        func()
    except ConnectionError as exc:
        raise RuntimeError('Falha ao conectar com o banco de dados') from exc
