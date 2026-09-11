# Trabalho Prático 1

## Introdução

Esse repositório é dedicado para o acompanhamento e solução do Trabalho 1 da Cadeira de **Resolução de Problemas com Grafos**.

## Problema

### Enunciado

Kefa decidiu celebrar o seu primero grande salário indo a um restaurante.

Ele vive em um parque incomum. O parque é uma árvore enraizada consistindo de n vértices com a raiz no vértice 1, que também contém a casa de Kefa. No parque também existem gatos e Kefa já sabe em quais vértices eles estão.

Os vértices folhas do parque contém restaurantes. Kefa quer escolher um restaurante para ir, mas infelizmente ele possui muito medo de gatos, então ele não irá para um restaurante se o caminho do restaurante para a sua casa conter mais de _m_ vértices com gatos **consecutivos**.

Sua tarefa é ajudar a Kefa contar o número de restaurantes em que ele consegue ir.

### Entrada

A primeira linha contém dois inteiros _n_ e _m_, ($2 \leq n \leq 10^{5}, 1 \leq m \leq n$), representando o número de vértices e o número máximo do vértices com gatos consecutivos que Kefa consegue tolerar.

A segunda linha contem _n_ inteiros a<sub>1</sub>, a<sub>2</sub>, ... , a<sub>n</sub>, em que cada a<sub>i</sub> é 0(o vértice _i_ não possui um gato) ou 1(o vértice _i_ possui um gato).

As próximas n-1 linhas contém as arestas da árvore no formato "x<sub>i</sub> y<sub>i</sub>" ($1 \leq x_{i},y_{i} \leq n, x_{i} \neq y_{i}$) em que x<sub>i</sub> e y<sub>i</sub> são os vértices da árvore, conectados por uma aresta.

É garantido que o conjuto de arestas fornecidos forma uma árvore.

### Saída

A saída deve ser um único inteiro, representando o número de vértices folhas (restaurantes) com até _m_ vértices com gatos consecutivos no caminho do vértice raiz até o vértice folha.

## Integrantes

- **Professor**: Prof. Ricardo Carubbi
- **Membros**:
  - Vitor Dantas de Almeida Mattos
  - Miguel Colares dos Santos Linard

## Linguagem

Para a resolução do problema, foi utilizada a linguagem _python_, mais especificamente pelo gerenciador de versões e bibliotecas **uv**.

## Execução

Na pasta `src` existem dois arquivos que podem ser executados.

O `main_files.py` representa o código de terminal que pode ser facilmente executado no terminal. Para a execução é recomendado o uso do `uv`, com o seguinte comando:

```bash
uv run main_files.py [CAMINHO_RELATIVO_PARA_TXT]
```

O `main.py` representa o código que resulta na solução do problema na plataforma **Codeforces** e, apesar de não ser recomendado, pode ser executado ao seguir os passos descrito no `marco-4.md`

## Modelagem

### Restrições

- Os caminhos devem ter, obrigatoriamente, como ponto de partida o vertíce 1, que é casa da Kefa.

- Como já dito no enunciado, Kefa tem medo de gatos. Então, os caminhos para os restaurantes válidos ficam restringidos de acordo com o número de vértices consecutivos com gatos que podem ter.

### Vértices

- O vértice 1 (raiz) representa a casa da Kefa, ponto de partida de todos os caminhos que deverá ser trilhado.

- Os vértices-folhas representam os restaurantes, que devem ser os pontos de chegada finais de cada caminho.

- O restante dos vértices, que não sejam raíz ou folhas, representam apenas referenciais para trilhar o caminho até os restaurantes (vértices-folhas).

> É importante relembrar que nem todos os vértices que representam restaurantes são iguais. Alguns possuem gatos e outros não (a diferenciação é feita na segunda linha da entrada da questão).

### Arestas

As arestas representam os caminhos/as conexões entre os vértices da árvore.

## Representação

Representando graficamente temos que o teste1 e teste2 representam as seguintes árvores respectivamente:

````txt
4 1
1 1 0 0
1 2
1 3
1 4
````

````mermaid
flowchart TD
    A((1))
    B((2))
    C((3))
    D((4))

    A --- B
    A --- C
    A --- D

    classDef normal fill:#2d68ad,stroke:#2d68ad,stroke-width:12px
    classDef cat fill:#dd0c19,stroke:#dd0c19, stroke-width: 12px

    class A,B cat
    class C,D normal
````

````text
7 1
1 0 1 1 0 0 0
1 2
1 3
2 4
2 5
3 6
3 7
````

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

## Algorítimo

> Para a explicação do algorítimo será utilizada a versão presente em `main.py`, a que é enviada para o Codeforces.

### Entrada de dados

Usando stdin para receber a entrada do Codeforces, todo o texto é lido e separa-se todos os números.

```py
def read_data():
    data = sys.stdin.read().split()
    return data
```

### Formatação

O primeiro número presente é a quantidade de vértices, o segundo é a quantidade máxima de vértices com gatos consecutivos que Kefa suporta, sendo chamada de "Tolerancia de gatos".

Como é informado que em seguida existem n vértices (representado por vertices_size, raw_data[0]) então o cat_positions consegue os valores do indice 2 (após a quantidade de vértices e a tolerancia) por n vértices.

Em edges, o processo é, de forma bruta, equivalente a esse pseudo-código:

```
termosEsquerda = raw_data[start=2 + n, step=2]
termosDireita = raw_data[start=2 + n + 1, step=2]
paresOrdenadosArestas = zip(termosEsquerda, termosDireita)
for par in paresOrdenadosArestas:
  paresInteiros <- int(par)
```

```py
def parse_data(raw_data: list[str]):
    results = {
        "vertices_size": int(raw_data[0]),
        "cat_tolerance": int(raw_data[1]),
        "cat_positions": [int(y) for y in raw_data[2: 2 + int(raw_data[0])]],
        "edges": [(int(z),int(y)) for z,y in zip(raw_data[2 + int(raw_data[0]):: 2 ], raw_data[2 + int(raw_data[0]) + 1:: 2 ])]
    } 
    return results
```

### DFS

Inicialmente, são adicionados as novas variaveis para armazenar os valores específicos do Kefa, sendo eles:

- a tolerancia de gatos
- a lista dos vértices que possuem gato
- A lista que armazena quantos gatos consecutivos existem da raiz até o vértice
- Uma variável que armazena quantos restaurantes(vértices folhas) foram alcançados

Além do grafo e do vértice da busca, o método de dfs foi modificado para receber o indice do vértice pai, que é utilizado em seguida para consultar quantos gatos consecutivos existiram até o pai e, se o vértice que atual da busca possuir um gato, somar os gatos consecutivos. Se o vértice não possuir um gato, então os gatos consecutivos são resetados para 0.

Se na pesquisa acontecer de os gatos consecutivos até o vértice da pesquisa ultrapassarem a tolerancia, então a recursão é interrompida.

Caso não seja interrompida, e durante a busca em momento algum teve algum vértice adjacente não marcado, isso significa que o vértice é um restaurante (vértice folha) e é adicionado na variável `leafs_reached`.

```py
class DepthFirstSearch:

    def __init__(self, G, s, cat_tolerance, is_cat):
        #kefa
        self.cat_tolerance = cat_tolerance
        self.is_cat = is_cat
        self.consec_cats = [0 for _ in range(G.V)]
        self.leafs_reached = 0

        #basic
        self.marked = [False for _ in range(G.V)]
        self.edge_to = [-1 for _ in range(G.V)]
        self.count = 0
        self.dfs(G, s)

    def dfs(self, G, v, father=None):
        
        self.edge_to[v] = father
        if father is None:
            self.edge_to[v] = 0
        
        self.consec_cats[v] = self.consec_cats[self.edge_to[v]] + 1 if self.is_cat[v] == 1 else 0
        
        self.marked[v] = True
        self.count += 1
        
        if self.consec_cats[v] > self.cat_tolerance:
            return
        
        any_sons = False
        for w in G.adj[v]:
            if not self.marked[w]:
                any_sons = True
                self.dfs(G, w, v)
        if not any_sons:
            self.leafs_reached += 1
```

### Execução

Os passos executados pelo programa são:

1. Ler os dados
2. Formatar os dados no dicionário
3. Cria o grafo e adiciona as arestas (removendo 1 de cada aresta pois o problema conta a partir do 1)
4. Realiza a pesquisa dfs, enviando o grafo, vertice de começo (0), a tolerancia de gatos e os vértices com gatos.
5. Após a busca, imprime quantos restaurantes(vértices folha) foram alcançados.

No trecho \_\_main\_\_, o limite de recursão e de stack é aumentado (pois a solução é recursiva e python possui limite) e a função main é executada.

```py
def main():
    # read input
    raw_data = read_data()
    parsed_data = parse_data(raw_data)
    
    # generate graph and relevent
    graph = Graph(parsed_data["vertices_size"])
    for v,u in parsed_data["edges"]:
        graph.add_edge(v - 1, u - 1)
    
    search = DepthFirstSearch(graph, 0, parsed_data["cat_tolerance"], parsed_data["cat_positions"])
    
    # solving
    output_result(search.leafs_reached)

if __name__ == "__main__":
    sys.setrecursionlimit(1 << 25)
    threading.stack_size(1 << 27)
    thread = threading.Thread(target=main)
    thread.start()
    thread.join()
```

## Implementação de Referência

Para a implementação básica de Node, Iterator, Bag, Graph e DepthFirstSearch, foi utilizado o código fornecido pelo professor baseado no livro de [Algorithms, 4ed](https://algs4.cs.princeton.edu/home/).

## Alterações

As alterações principais feitas no algorítimo foram:

- Transmição de valores pai na função recursiva
- Fim de recursão caso os gatos consecutivos ultrapassarem um limite
- Verificação de se um nó é folha.
- Aumento de limite de recursão e stack.

## Justificativas

Para conseguir impedir a pesquisa a depender da quantidade de gatos consecutivos, pesquisar de forma de "pai-filho" para determinar a quantidade de gatos da raiz até um determinado vértice é algo valioso. Por conta disso a forma de busca em profundidade feita pelo **dfs** se torna extremamente valiosa, sendo por tanto o algoritimo usado.

## Complexidade

Em sua execução, cada vértice é percorrida apenas uma vez, resultando em:
$$
O(V + E) = O(n + (n + 1)) \equiv O(n)
$$

## Testes

Utilizando os dados presentes no repositório na pasta `dados`, temos os dois casos de teste:

```bash
uv run main_files.py ../dados/teste1.txt
uv run main_files.py ../dados/teste2.txt
```

## Evidência

![Resultado Aceitado](./evidencias/image.png)

## Uso de IA

Ferramentas de geração de texto foram utilizadas minimamente apenas para correção e formatação de texto, não sendo utilizadas de qualquer forma nos códigos.
