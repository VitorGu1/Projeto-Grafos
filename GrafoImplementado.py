def criar_grafo():
    return{}


def inserir_vertice(grafo, vertice):
    
    if vertice in grafo:
        print('ja existe no grafo')
    else:
            
        grafo[vertice] = []
    pass    


def inserir_aresta(grafo, origem, destino, nao_direcionado=False):
    if origem not in grafo:
        grafo[origem] = []
    if destino not in grafo:
        grafo[destino] = []
    grafo[origem].append(destino)
    if nao_direcionado:
        grafo[destino].append(origem)
    pass

def vizinhos(grafo, vertice):
    if vertice in grafo:
        return grafo[vertice]
    else:
        print("esse Verticie não esta no grafo")
    
    pass

def listar_vizinhos(grafo, vertice):
    if vertice in grafo:
       print(grafo[vertice])
    else:
        print("esse Verticie não esta no grafo")
        
    pass

def exibir_grafo(grafo):
    for vertice in grafo:
        print(f"{vertice} -> {grafo[vertice]}")
   
    pass

def remover_aresta(grafo, origem, destino, nao_direcionado=False):
    if origem in grafo and destino in grafo[origem]:
            grafo[origem].remove(destino)
    
    if nao_direcionado:
        if destino in grafo and origem in grafo[destino]:
            grafo[destino].remove(origem)
    pass


def remover_vertice(grafo, vertice, nao_direcionado=True):

    if vertice in grafo:
        for vert in list(grafo.keys()):
            lista = listar_vizinhos(grafo,vert)
            if vertice in lista:
                grafo[vert].remove(vertice)

        del grafo[vertice]
    else:
        print("verticie não existe no grafo")
    pass


def existe_aresta(grafo, origem, destino):
    if origem in grafo and destino in grafo[origem]:
        return True

    else:
        return False
    

def grau_vertices(grafo):
    base = {}
    for i in grafo:
        base[i]={'out':0,'in':0,"total":0}
    for i in grafo:
        base[i]['out'] = len(grafo[i])
        for j in grafo:
            if i in grafo[j]:
                base [i]['in'] += 1
        base[i]['total'] = base[i]['out'] + base[i]['in']


    resultado = {}
    for i in grafo:
        resultado[i] = (base[i]['out'],base[i]['in'],base[i]['total'])

    return resultado
    


def percurso_valido(grafo, caminho):
    if len(caminho) < 2:
        return True
        
    for i in range(len(caminho) - 1):
        origem = caminho[i]
        destino = caminho[i + 1]
        
        if origem not in grafo or destino not in grafo[origem]:
            return False
            
    return True
    



def main():
    grafo = criar_grafo()
    
    while True:
        print("\n================ MENU GRAFO ================")
        print("1 - Mostrar o Grafo")
        print("2 - Inserir vértice")
        print("3 - Inserir aresta")
        print("4 - Remover vértice")
        print("5 - Remover aresta")
        print("6 - Listar vizinhos")
        print("7 - Calcular graus dos vértices")
        print("8 - Verificar percurso válido")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            exibir_grafo(grafo)
            
        elif opcao == '2':
            v = input("Digite o nome do vértice: ").strip()
            inserir_vertice(grafo, v)
            print(f"Vértice '{v}' inserido com sucesso!")
            
        elif opcao == '3':
            origem = input("Vértice de origem: ").strip()
            destino = input("Vértice de destino: ").strip()
            nd = input("O grafo é não direcionado? (s/n): ").strip().lower() == 's'
            inserir_aresta(grafo, origem, destino, nao_direcionado=nd)
            print("Aresta inserida com sucesso!")
            
        elif opcao == '4':
            v = input("Digite o vértice a ser removido: ").strip()
            if remover_vertice(grafo, v):
                print(f"Vértice '{v}' removido com sucesso!")
            else:
                print(f"Vértice '{v}' não encontrado.")
                
        elif opcao == '5':
            origem = input("Vértice de origem: ").strip()
            destino = input("Vértice de destino: ").strip()
            nd = input("O grafo é não direcionado? (s/n): ").strip().lower() == 's'
            remover_aresta(grafo, origem, destino, nao_direcionado=nd)
            print("Tentativa de remoção de aresta concluída.")
            
        elif opcao == '6':
            v = input("Digite o vértice para ver os vizinhos: ").strip()
            listar_vizinhos(grafo, v)
            
        elif opcao == '7':
            graus = grau_vertices(grafo)
            print("\n--- Graus dos Vértices (Out, In, Total) ---")
            for vertice, valores in graus.items():
                print(f"Vértice {vertice} -> Saída: {valores[0]}, Entrada: {valores[1]}, Total: {valores[2]}")
            print("------------------------------------------")
            
        elif opcao == '8':
            caminho_str = input("Digite o caminho separado por espaços (ex: A B C): ").strip()
            if caminho_str:
                caminho = caminho_str.split()
                valido = percurso_valido(grafo, caminho)
                if valido:
                    print("O percurso é VÁLIDO!")
                else:
                    print("O percurso é INVÁLIDO!")
            else:
                print("Caminho vazio.")
                
        elif opcao == '0':
            print("A encerramentar o programa. Até breve!")
            break
        else:
            print("Opção inválida! Tente novamente.")


main()
