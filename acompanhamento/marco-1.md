# Marco 1 - Modelagem

## Enunciado

## Entrada

## Saída

## Restrições

## Vértices

## Arestas

## Tipo de Grafo

O grafo determinado pelo problema é uma [**árvore enraizada**](#ref-root), sendo determinada por: </br>
Definição de [árvore](#ref-tree):
> G é uma árvore se G for um grafo acíclico conexo.


Definição de árvore enraizada:
> Uma árvore enraizada é uma árvore, em que se pode distinguir um determinado vértice chamado raiz.

## Instância Pequena

Nos seguintes exemplos, vértices normais tem cor azul e vértices que possuem gato tem cor vermelha.

Para o primeiro caso, analisemos o grafo gerado pela entrada:
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

Para o segundo caso, analisemos o grafo gerado pela entrada:
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

## Resultado Esperado

Para o primeiro caso, nota-se que com a "tolerância de gato" em 1, então Kefa consegue ver no máximo 1 gato de forma consecutiva em um caminho e ainda proseguir por ele. Sendo assim, como existe um gato no nó raiz 1, ele não irá para o restaurante no nó 2 (que também possui um gato), podendo apenas prosseguir para os nós 3 e 4. Sendo assim, o resultado esperado é 2

Para o segundo caso, novamente temos a "tolerância de gato" em 1. Por novamente existir um gato no nó raiz Kefa não pode ir para o vértice 3, bloqueando assim a possibilidade de visitar os restaurantes 6 e 7. Por não haver nenhum gato no vértice 2 ele pode visitar os restaurantes 4 e 5. Note que ele consegue sim visitar o nó 4 mesmo possuindo um gato, pois ele não está de forma consecutiva a raiz 1. Sendo assim, o resultado esperado é 2

## Hipótese Inicial de Solução

> [!NOTE]: Uma pequena consideração a ser feita nessa solução é:
> - Vértices/Nós **pais** são vértices que possuem 1 ou mais outros vértices com distância da raiz maior que ele ligados a ele.
> - Vértices/Nós **filhos** são vértices que estão ligados a um vértice que possui uma distância da raiz menor que ele.

A hipótese inicial de como solucionar esse problema é:

1. Cada vértice deve possuir a seguintes informações
   - Existencia de gato nele.
   - Contador de quantos gatos consecutivos foram vistos para chegar até ele.
2. A partir da raiz, incluindo ela, percorresse os nós somando o contador de gatos(para o valor do contador do pai + 1) se o pai possuir um gato ou resetando senão.
3. Repete-se o passo 2 até todos os vértices serem visitados.
4. Após terminado de "calcular" os contadores dos vértices. Criasse um contador para quantos nós folhas são alcançaveis
5. Percorresse a árvore novamente a partir da raiz, apenas progredindo se o nó possuir um contador menor ou igual ao limite.
6. Para cada nó folha, some o contador de vértices alcançaveis
7. Repita o processo até percorrer todo os vértices possíveis para a solução completa

## Referencia Bibliografica

- <spam id="ref-root">DIESTEL, Reinhard. Graph Theory. 5. ed. Berlin: Springer Nature, 2017. 15 p. ISBN 978-3-662-53621-6. </spam>
- <spam id="ref-tree">NICOLETTI, Maria do Carmo; HRUSCHKA JUNIOR, Estevam R. Fundamentos da teoria dos grafos para computação. 3. ed. Rio de Janeiro: LTC, 2017. 117 p. ISBN 978-85-216-3446-1. </spam>
