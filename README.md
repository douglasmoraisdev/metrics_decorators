# metrics_decorators
Python package de Decorators para auxiliar no log de metricas usando [json_log](https://github.com/douglasmoraisdev/json_log)


## Instalação

No arquivo `requeriments.txt` do projeto a ser usado, adicionar a linha:
```
git+https://github.com/douglasmoraisdev/metrics_decorators#egg=metrics_decorators
```

Ou manualmente, usando PIP:
```sh
$ pip install git+https://github.com/douglasmoraisdev/metrics_decorators#egg=metrics_decorators
```


## Exemplo de importação e uso:

```python
from json_log import applog # dependencia obrigatoria
from metrics_decorators.func_time_metrics import log_func_time

if __name__ == '__main__':

    # Adicionar o decorator a nivel funcao
    @log_func_time(applog)
    def funcao_teste(param):
        '''
           Algum algoritimo de processamento que deseje cronometrar
        '''
        return result

    # ao chamar a funcao em qualquer ponto, o decorator irá ser usado
    funcao_teste(2)
```
## Decorators

### `log_func_time`
Loga o tempo total de execução de uma função em nível `INFO` adicionando a tag `metrics` no log.

#### params:
* applog(required): Objeto AppLog([json_log](https://github.com/douglasmoraisdev/json_log)), utilizado para logar.

* qtd_label(optional): Label usado para identificar a quantidade processada no log.
Ex.: 'qtd_label=quantidade_processos_atualizados' ou 'qtd_label=total_linhas_retornadas'

* tuple_qtd_index(optional): Indice da tupla de retorno da função para ser usado como quantidade.
Ex.: Uma função pode retornar uma tupla de itens com 3 elementos, caso deseje usar o `tamanho` de algum desses elementos como quantidade, basta informar o indice dessa tupla neste parametro.

### Exemplos:
Uso em funções com retorno não quantitativo:

```python
    @log_func_time(applog)
    def funcao_teste(param):
        '''
            Alguma funcao sem retorno de quantidade (quantitativa)
        '''
        return True
```
Vai logar:
```json
{
    "@timestamp": "2020-05-12 12:15:55,218",
    "appname": "teste_log",
    "loglevel": "INFO",
    "run_id": "2cc04541-c53c-4832-9937-ffb6676773f4",
    "total_items": 0,
    "total_label": "",
    "message": "Executando funcao_teste",
    "total_time": "0:00:03.000411",
    "function_name": "__main__.funcao_teste",
    "tags": [
        "metrics"
    ]
}
```

Uso em funções com retorno quantitativo:

Sem label:
```python
    @log_func_time(applog)
    def funcao_teste(param):
        '''
            Alguma funcao que retorne quantidade (quantitativa)
        '''
        qtd_linhas_processadas = algum_resultado_quantitativo
        return qtd_linhas_processadas
```
Vai logar (note o nó total_itens):
```json
{
    "@timestamp": "2020-05-12 12:21:44,652",
    "appname": "teste_log",
    "loglevel": "INFO",
    "run_id": "1da11fc7-ea76-4dc8-8036-a2840691a7f5",
    "total_items": 4,
    "total_label": "",
    "message": "Executando funcao_teste",
    "total_time": "0:00:00.000012",
    "function_name": "__main__.funcao_teste",
    "tags": [
        "metrics"
    ]
}
```


Com label:
```python
    @log_func_time(applog, qtd_label='total_de_registros')
    def funcao_teste(param):
        '''
            Alguma funcao que retorne quantidade (quantitativa)
        '''
        qtd_linhas_processadas = algum_resultado_quantitativo
        return qtd_linhas_processadas
```
Vai logar (note o nó total_label):
```json
{
    "@timestamp": "2020-05-12 12:23:13,590",
    "appname": "teste_log",
    "loglevel": "INFO",
    "run_id": "e9371309-8c9d-459c-8572-43b7acc89b2d",
    "total_items": 4,
    "total_label": "total_de_registros",
    "message": "Executando funcao_teste",
    "total_time": "0:00:00.000013",
    "function_name": "__main__.funcao_teste",
    "tags": [
        "metrics"
    ]
}
```

Com Tuple Index:
```python
    @log_func_time(applog, qtd_label='total_dataframe_qtd_2', tuple_qtd_index=2)
    def funcao_teste(param):
        qtd_1 = [1,2,3,4]
        qtd_2 = [{'a': 1, 'b': 2, 'x': 3}]
        return qtd_1, qtd_2
```
Vai logar (note o nó total_items, utilizou o tamanho do qtd_2 do retorno):
```json
{
    "@timestamp": "2020-05-12 12:24:13,890",
    "appname": "teste_log",
    "loglevel": "INFO",
    "run_id": "e9371309-8c9d-459c-8575-43b7acc89b3d",
    "total_items": 3,
    "total_label": "total_dataframe_qtd_2",
    "message": "Executando funcao_teste",
    "total_time": "0:00:00.000013",
    "function_name": "__main__.funcao_teste",
    "tags": [
        "metrics"
    ]
}
```