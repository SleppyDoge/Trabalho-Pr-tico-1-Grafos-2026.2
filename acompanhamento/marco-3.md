# Marco 3 - Aplicação Básica do DFS

## Execução Manual

Para demonstrar o uso do DFS, consideremos o seguinte grafo problema:

**Grafo**
````mermaid
flowchart TD

    A((1))
    B((2))
    C((3))
    D((4))
    E((5))
    F((6))
    G((7))

    A --- B
    A --- C
    B --- D
    B --- E
    C --- F
    C --- G

    classDef normal fill:#2d68ad,stroke:#2d68ad,stroke-width:12px
    classDef cat fill:#dd0c19,stroke:#dd0c19, stroke-width: 12px

    class A,C,D cat
    class B,E,F,G normal
````

**Lista de Adjacência**
|Vértices| Adjacêntes|
|:--:|:--:|
|1|2, 3|
|2|1, 4, 5|
|3|1, 6, 7|
|4|2|
|5|2|
|6|3|
|7|3|



**Marked + Edge_to (inicialmente)**
| Vértice | Marked | Edge_to|
|:---:|:---:|:---:|
|1|F| Null |
|2|F| Null |
|3|F| Null |
|4|F| Null |
|5|F| Null |
|6|F| Null |
|7|F| Null |

**Pré e Pós Ordem**
|Tipo|Valores|
|:--:|:--|
|Pré-Ordem||
|Pós-Ordem||

Começando do Vértice 1, marcamos ele como visitado e atribuimos -1 ao edge_to (Não veio de nenhum vértice em particular, começamos dele), proseguimos para o próximo vértice não marcado, sendo esse o 2:

**Marked + Edge_to**
| Vértice | Marked | Edge_to|
|:---:|:---:|:---:|
|1|T| -1 |
|2|F| Null |
|3|F| Null |
|4|F| Null |
|5|F| Null |
|6|F| Null |
|7|F| Null |

**Pré e Pós Ordem**
|Tipo|Valores|
|:--:|:--|
|Pré-Ordem|1|
|Pós-Ordem||

Por termos visitado o vértice 2 a partir do vértice 1, marquemos ele como visitado e o edge_to como 1. Também adcionemos ele a pré-ordem.

**Marked + Edge_to**
| Vértice | Marked | Edge_to|
|:---:|:---:|:---:|
|1|T| -1 |
|2|T| 1 |
|3|F| Null |
|4|F| Null |
|5|F| Null |
|6|F| Null |
|7|F| Null |

**Pré e Pós Ordem**
|Tipo|Valores|
|:--:|:--|
|Pré-Ordem|1, 2|
|Pós-Ordem||

Agora, por já termos visitado o 1, podemos desconsidera-lo. Logo, o próximo vértice não visitado é o 4. Percorrendo ele, modifiquemos o valor de marcado e adicionemos o vértice 2 no edge_to e o valor de 4 na pré ordem.

**Marked + Edge_to**
| Vértice | Marked | Edge_to|
|:---:|:---:|:---:|
|1|T| -1 |
|2|T| 1 |
|3|F| Null |
|4|T| 2 |
|5|F| Null |
|6|F| Null |
|7|F| Null |

**Pré e Pós Ordem**
|Tipo|Valores|
|:--:|:--|
|Pré-Ordem|1, 2, 4|
|Pós-Ordem||

Por conta do vértice 4 não possuir nenhum outro vértice que não foi visitado, adicionaremos ele a pós ordem e retornemos para o vértice que ele foi indicado por, continuando a busca. Seguindo o processo, o próximo vértice a ser visitado é o 5, logo modifiquemos o estado de marcado, o valor de edge_to e a lista de pré ordem.

**Marked + Edge_to**
| Vértice | Marked | Edge_to|
|:---:|:---:|:---:|
|1|T| -1 |
|2|T| 1 |
|3|F| Null |
|4|T| 2 |
|5|T| 2 |
|6|F| Null |
|7|F| Null |

**Pré e Pós Ordem**
|Tipo|Valores|
|:--:|:--|
|Pré-Ordem|1, 2, 4|
|Pós-Ordem|4, |

O 5 não possui nenhum outro vértice que ainda não foi visitado, e o mesmo é verdade para o 2, logo adicionaremos ambos a lista de pós ordem. Então, voltando para o vértice 1 e seguindo para o vértice 3, visitando-o, adicionando ao edge_to e na lista de pré ordem.

**Marked + Edge_to**
| Vértice | Marked | Edge_to|
|:---:|:---:|:---:|
|1|T| -1 |
|2|T| 1 |
|3|T| 1 |
|4|T| 2 |
|5|T| 2 |
|6|F| Null |
|7|F| Null |

**Pré e Pós Ordem**
|Tipo|Valores|
|:--:|:--|
|Pré-Ordem|1, 2, 4, 5, 3|
|Pós-Ordem|4, 5, 2, |

Do 3, visitaremos o vértice 6, lembrando de adicionar o valor no edge_to e pré ordem.

**Marked + Edge_to**
| Vértice | Marked | Edge_to|
|:---:|:---:|:---:|
|1|T| -1 |
|2|T| 1 |
|3|T| 1 |
|4|T| 2 |
|5|T| 2 |
|6|T| 3 |
|7|F| Null |

**Pré e Pós Ordem**
|Tipo|Valores|
|:--:|:--|
|Pré-Ordem|1, 2, 4, 5, 3, 6|
|Pós-Ordem|4, 5, 2, |

Como o 6 não possui mais vértices que não foram visitados, adicionemos ele a lista de pós ordem, voltemos para a lista do vértice 3 e seguimos em frente, verificando agora o vértice 7, visitando-o, adicionando-o ao edge_to e a lista de pré ordem.

**Marked + Edge_to**
| Vértice | Marked | Edge_to|
|:---:|:---:|:---:|
|1|T| -1 |
|2|T| 1 |
|3|T| 1 |
|4|T| 2 |
|5|T| 2 |
|6|T| 3 |
|7|T| 3 |

**Pré e Pós Ordem**
|Tipo|Valores|
|:--:|:--|
|Pré-Ordem|1, 2, 4, 5, 3, 6, 7|
|Pós-Ordem|4, 5, 2, 6, |

Como o vértice 7 não possui outros vértices não visitados, voltemos para o vértice 3 e verifiquemos que ele também não possui vértices não visitados para, emfim, voltarmos para o vértice 1, não possuindo vértices que não estão marcados. Logo, adicionemos os 3 valores a lista de pós ordem, concluindo assim a busda em profundidade.

**Marked + Edge_to**
| Vértice | Marked | Edge_to|
|:---:|:---:|:---:|
|1|T| -1 |
|2|T| 1 |
|3|T| 1 |
|4|T| 2 |
|5|T| 2 |
|6|T| 3 |
|7|T| 3 |

**Pré e Pós Ordem**
|Tipo|Valores|
|:--:|:--|
|Pré-Ordem|1, 2, 4, 5, 3, 6, 7|
|Pós-Ordem|4, 5, 2, 6, 7, 3, 1|

## Árvore de Busca

Pelo fato do grafo do problema ser em sí uma árvore, a árvore de busca é identica ao grafo do problema

## Tempos de descoberta e término

Os tempos de descoberta e término registram, respectivamente, os momentos em que um vértice entra na pré ordem e pós ordem, logo:

### Descoberta

| Vértice | Tempo de Descoberta|
|:--:|:--:|
| 1 | 1 |
| 2 | 2 |
| 3 | 8 |
| 4 | 3 |
| 5 | 5 |
| 6 | 8 |
| 7 | 10 |

### Término

|Vértice|Tempo de Término|
|:--:|:--:|
| 1 | 14 |
| 2 | 6 |
| 3 | 13 |
| 4 | 4 |
| 5 | 6 |
| 6 | 9 |
| 7 | 11 |

## Alcançabilidade e predecessores

### Alcançabilidade

Pela natureza do grafo ser uma árvore, é possível alcançar de um dado vértice qualquer outro, sendo completamente alcançável. Esse fato também é confirmado pelo verificação que o "vetor" booleano de marcado/visitado está preenchido com valores True.

### Predecessores

Predecessores são os valores pelo qual um vértice é visitado por, sendo computacionalmente determinados pelo edge_to que já foi preenchido.

### Aplicabilidade ao problema

Devido a estrutura de árvore e a dependência do problema de conseguir determinar quantos gatos consecutivos, sendo esse fator facilmente determinado pela recursão de busca em profundidade, foram encontrados até chegar aos nós folhas, o uso de DFS resolve de forma satisfatoria o problema.
