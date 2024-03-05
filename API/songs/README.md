# DESAFIO API músicas 🥇

## 1. Objetivo da API

Api de músicas, onde é possível: adiconar novas canções, consultar todas canções disponíveis, consultar uma canção individual, editar canções existentes e também excluir músicas existentes.

## 2. URL base da API

O url base `localhost` na porta `5000`

``` bash
http://localhost:5000
```

## 3. Estrutura de cada canção

* Lista de dicionários, que contem id, canção e estilo

``` py
{
    "id": 1,
    "cancao": "I drink wine",
    "estilo": "pop"
}
```

## 4. Endpoints

* Criar nova canção
* Consultar :
  * Todas as canções
  * Especificamente pelo id
* Editar uma canção
* Excluir uma canção

### 4.1.  URLs completos para cada endpoint

* POST <http://localhost:5000/cancoes>
* GET <http://localhost:5000/cancoes>
* GET <http://localhost:5000/cancoes/1>
* PUT <http://localhost:5000/cancoes/1>
* DELETE <http://localhost:5000/cancoes/1>
