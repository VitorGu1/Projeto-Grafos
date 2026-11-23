def busca_profundidade(grafo, vertice):
    visitados = []
    pilha = [vertice]

    while pilha:
        atual = pilha.pop()

        if atual not in visitados:
            visitados.append(atual)

            for vizinho in grafo.get(atual, []):
                if vizinho not in visitados:
                    pilha.append(vizinho)

    return visitados



def detectar_ciclo(grafo, vertice):
    visitados = []
    pilha = [(vertice, None)]

    while pilha:
        atual, pai = pilha.pop()

        if atual not in visitados:
            visitados.append(atual)

            for vizinho in grafo.get(atual, []):
                if vizinho == atual:
                    return True

                if vizinho not in visitados:
                    pilha.append((vizinho, atual))

                elif vizinho != pai:
                    return True

    return False






grafo = {
    'v1': ['v1', 'v2', 'v6'],
    'v2': ['v1', 'v3', 'v4', 'v3', 'v7'],
    'v3': ['v1', 'v2'],
    'v4': ['v2', 'v5'],
    'v5': ['v4', 'v6', 'v8'],
    'v6': ['v1', 'v5', 'v7'],
    'v7': ['v2', 'v6', 'v8'],
    'v8': ['v5', 'v7']
}

vertice = list(grafo.keys())[0]


print(busca_profundidade(grafo, vertice))



if detectar_ciclo(grafo, vertice):
    print("O grafo possui ciclo")
else:
    print("O grafo não possui ciclo")
