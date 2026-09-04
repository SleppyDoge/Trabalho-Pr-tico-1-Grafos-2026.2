# Marco 4 - Aplicação básica de BFS e conclusão

## Execução manual

## Comparação DFS e BFS

## Escolha Justificada

Para solucionar o problema específico, é necessário identificar os valores para cada vértice de quantos gatos consecutivos ocorram até ele, necessitando portanto de uma identificação clara dos pais. Entre as duas abordagens de busca a que melhor realiza essa condição é a **Busca em profundidade (DFS)**.

## Adaptação

As principais adaptações feitas ao problema envolvem:
- Criação de variáveis e vetores para armazenar as informações relacionadas a gatos: *cat_tolerance, is_cat, consec_cats*
- Criação do contador *leafs_reached* para armazenar o que será a solução do problema.
- O dfs recebe além dos valores de G e v (O grafo e o vértice a ser pesquisado), um valor que indica o pai. Esse valor é utilizado para que possa ser realizado a contagem de gatos consecutivos.
- Um caso de parada caso os gatos consecutivos em um vértice ultrapassem a tolerância
- Uma verificação se um vértice é folha e, se for, adicionada ao *leafs_reached*.
- Devido a limitações específicas do python relacionadas a recursão em muitas chamadas, utiliza-se mudanças no limite de recursão e aumento no tamanho da stack.

## Testes

Para a realização de testes, deve ser realizado o seguinte passo a passo:
1. Copie os dados presentes em ``dados/teste1.txt`` ou ``dados/teste2.txt`` (dependendo de qual caso deseja ser testado) para a área de transferência (Ctrl+C)
2. Dentro da pasta ``src``, rode o arquivo ``main.py`` (preferêncialmente, com ``uv run main.py``)
3. Cole o dado de teste
4. Execute um EOF no terminal, sendo ``Ctrl+Z`` no Windows ou ``Ctrl+D`` em Linux e sistemas Unix.
5. O resultado do problema aparecerá na linha seguinte.

## Complexidade

O algoritimo apenas precisa percorrer cada vértice da árvore apenas uma vez, inclusive com casos em que não é necessário percorrer vértices e seus filhos (no caso de ultrapassagem da tolerância de gatos). Sendo assim, temos que a complexidade do algoritimo é expressa em **O(V + E)**.

## Submissão

![alt text](../evidencias/image.png)