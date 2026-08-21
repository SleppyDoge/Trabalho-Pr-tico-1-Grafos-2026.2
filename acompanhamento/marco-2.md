# Marco 2 - Representação Computacional

## Representação

Para a resolução do problema, inicialmente existem 2 formas possíveis: Matriz e Lista de Adjacência.

Pelas informações do enunciado, existe a possibilidade de até $10^5$ vértices. Dado que a representação por matriz requer linhas e colunas com tamanho da quantidade de vértices, isso resultaria em uma matriz de tamanho $10^{10}$, o que é inviavel para uma resolução computacional.

Por conta desse fator, para a resolução do problema foi escolhida a **Lista de Adjacência**.

## Leitura da Entrada

Exemplo de entrada

````txt
7 1
1 0 1 1 0 0 0
1 2
1 3
2 4
2 5
3 6
3 7
````

A entrada do problema consiste em 3 partes principais:

**Preparação**: Consiste pelos termos `7 1`, representando respectivamente a quantidade de vértices e a "Tolerância de Gatos" de Kefa.

**Gatos**: Consiste da Lista `1 0 1 1 0 0 0`, representando se existe gatos na respectiva posição. No exemplo, existem gatos nas posições 1,3 e 4.

**Conexões**: Representam as conexões entre os vértices, então usando o primeiro termo como exemplo, existe um caminho entre o vértice 1 e o 2.

## Construção do Grafo

Como os vértices já são identificados por números simples (sendo os números 1 até n, em que n é o primeiro termo da "Preparação"), cria-se facilmente uma lista de adjacência, seguindo os seguintes passos:

1. Cria-se um dicionario em que cada `chave` corresponde a um vértice e o valor respectivo sendo uma lista vazia.
2. Para cada item de "Conexões", adiciona-se a cada uma das chaves o *outro* membro presente na linha. Então no caso da conexão `1 2`, adiciona-se o número 2 para a lista de valores do 1 e o número 1 para a lista de valores do 2.
3. Repetindo esse processo com todas as arestas fornecidas, monta-se a lista de adjacência como a presente abaixo:

````txt
1: 2, 3
2: 1, 4, 5
3: 1, 6, 7
4: 2
5: 2
6: 3
7: 3
````

## Medidas Estruturais Pertinentes

### Ordem

A Ordem representa a quantidade de vértices presentes na estrutura, podendo ser determinado pela quantidade de linhas presentes na lista de adjacência ou, alternativamente, pela leitura do primeiro termo da parte de "Preparação".

No exemplo selecionado, a ordem do Grafo é `7`.

### Tamanho

O Tamanho representa a quantidade de arestas presentes no gráfico. Esse valor pode ser determinado soma do tamanho de cada linha da lista de adjacência ou, alternativamente, dado que o grafo específicado é uma árvore, o número de arestas sempre será a `quantidade de vértices - 1`.

No exemplo selecionado, a quantidade de arestas é `6`.

### Grau

O grau em uma lista de adjacência (dado que o nosso grafo é não-direcionado) pode ser determinado pelo tamanho de uma linha. 

No exemplo selecionado, os graus dos vértices são:

````txt
1: 2
2: 3
3: 3
4: 1
5: 1
6: 1
7: 1
````

### Grau máximo

O grau máximo é determinado pelo maior grau presente, no caso da questão em específico: `3`

### Grau mínimo

O grau mínimo será o oposto, sendo o menor grau presente, no caso da questão em específico: `1`

### Grau médio

O grau médio é determinado pela soma de todos os graus, divididos pela quantidade de vértices presentes, logo:

$$\frac{2+3+3+1+1+1+1}{7} \approx 1.70 $$

### Densidade do Grafo

A densidade do Grafo é determinada pela quantida de arestas presentes (o valor do tamanho) dividido pela quantidade de arestas possíveis:

$$\frac{6}{\frac{(7 \times 6)}{2}} = \frac{2}{7} \approx 0.29$$

Nota-se que se for calculado utilizando as variáveis, utilizando-se do fato que em uma árvore as arestas são um a menos que os vértices, temos:

$$\rho = \frac{2|E|}{|V|(|V|-1)} = \frac{2(|V|-1)}{|V|(|V|-1)} = \frac{2}{|V|}$$

Dado que a densidade é da forma $\rho = O(1/|V|)$, então o grafo é classificado como **esparso**.