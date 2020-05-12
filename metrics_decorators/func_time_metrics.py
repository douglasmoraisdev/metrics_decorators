from datetime import datetime
import functools

def get_len(obj):
    if (type(obj) is int) or (type(obj) is float):
        # int - retorna o inteiro
        return obj
    elif '__len__' in dir(obj):
        # listas, dataframes, etc - retorna o tamanho do objeto
        return len(obj)
    else:
        return 0

def log_func_time(applog, tuple_qtd_index=0, qtd_label=''):
    '''
    Loga a funcao marcando tempo de execucao
    - param-> applog(obrigatório): objeto de log
    - param-> tuple_qtd_index(opcional): informa  o indice da tupla de retorno usada para ser totalizador.
        ex.: Se uma função retorna a tupla (item_1, item_2, item_3), e tuple_qtd_index = 2, entao o item_2 será
        usado como totalizador
    - param-> qtd_name(opcional): label do totalizador exibido no log
    '''

    def _is_quantitative_method(result, tuple_qtd_index=0):
        '''
            Avalia se uma variavel é quantitativa e retorna seu valor
        '''
        # se for uma tupla pega o tamanho do indice informado
        if tuple_qtd_index > 0:
            #verifica se é uma tupla
            assert type(result) is tuple

            # verifica se o indice existe na tupla
            tuple_qtd_index -= 1
            assert len(result) >= tuple_qtd_index

            item = result[tuple_qtd_index]
            return get_len(item)

        return get_len(result)


    def decorator_log_func_time(func):
        '''
         Source do decorator
        '''
        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            # Marca o tempo de execucao da funcao monitorada
            start = datetime.now()
            result = func(*args, **kwargs)
            end = datetime.now()

            # verifica se é uma funcao quantitativa
            qtd = _is_quantitative_method(result, tuple_qtd_index)

            applog.time_metric(
                        message=f"Executando {func.__name__}", 
                        func_name=f"{func.__module__}.{func.__name__}", 
                        total_time=str(end-start),
                        total_items=qtd,
                        total_label=qtd_label
            )
            return result

        return wrapper
    return decorator_log_func_time
