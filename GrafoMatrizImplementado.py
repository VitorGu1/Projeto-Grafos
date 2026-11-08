
def criar_grafo():

    matriz = []
    vertices = []

    return matriz, vertices


def inserir_vertice(matriz, vertices, vertice):

    if vertice not in vertices:

        vertices.append(vertice)

        
        for linha in matriz:
            linha.append(0)

        
        nova_linha = []

        for i in range(len(vertices)):
            nova_linha.append(0)

        matriz.append(nova_linha)

        print("Vertice adicionado!")

    else:
        print("Esse vertice ja existe.")


def inserir_aresta(matriz, vertices, origem, destino, nao_direcionado=False):

    if origem not in vertices:
        inserir_vertice(matriz, vertices, origem)

    if destino not in vertices:
        inserir_vertice(matriz, vertices, destino)

    i = vertices.index(origem)
    j = vertices.index(destino)

    matriz[i][j] = 1

    if nao_direcionado:
        matriz[j][i] = 1


def remover_vertice(matriz, vertices, vertice):

    if vertice in vertices:

        i = vertices.index(vertice)

        matriz.pop(i)

        for linha in matriz:
            linha.pop(i)

        vertices.remove(vertice)

        print("Vertice removido!")

    else:
        print("Vertice nao encontrado.")


def remover_aresta(matriz, vertices, origem, destino, nao_direcionado=False):

    if origem in vertices and destino in vertices:

        i = vertices.index(origem)
        j = vertices.index(destino)

        matriz[i][j] = 0

        if nao_direcionado:
            matriz[j][i] = 0

        print("Aresta removida!")

    else:
        print("Vertice nao encontrado.")


def existe_aresta(matriz, vertices, origem, destino):

    if origem in vertices and destino in vertices:

        i = vertices.index(origem)
        j = vertices.index(destino)

        if matriz[i][j] == 1:
            return True
        else:
            return False

    return False


def vizinhos(matriz, vertices, vertice):

    lista_vizinhos = []

    if vertice in vertices:

        i = vertices.index(vertice)

        for j in range(len(matriz[i])):

            if matriz[i][j] == 1:
                lista_vizinhos.append(vertices[j])

    return lista_vizinhos


def grau_vertices(matriz, vertices):

    graus = {}

    for i in range(len(vertices)):

        saida = 0
        entrada = 0

        for j in range(len(vertices)):
            saida = saida + matriz[i][j]

        for j in range(len(vertices)):
            entrada = entrada + matriz[j][i]

        total = entrada + saida

        graus[vertices[i]] = {
            "saida": saida,
            "entrada": entrada,
            "total": total
        }

    return graus


def percurso_valido(matriz, vertices, caminho):

    for i in range(len(caminho) - 1):

        origem = caminho[i]
        destino = caminho[i + 1]

        if existe_aresta(matriz, vertices, origem, destino) == False:
            return False

    return True


def listar_vizinhos(matriz, vertices, vertice):

    if vertice in vertices:

        lista = vizinhos(matriz, vertices, vertice)

        print("Vizinhos de", vertice, ":", lista)

    else:
        print("Vertice nao encontrado.")


def exibir_grafo(matriz, vertices):

    print("\nMATRIZ DE ADJACENCIA\n")

    print("   ", end="")

    for vertice in vertices:
        print(vertice, end=" ")

    print()

    for i in range(len(vertices)):

        print(vertices[i], end="  ")

        for j in range(len(vertices)):
            print(matriz[i][j], end=" ")

        print()


def main():

    matriz, vertices = criar_grafo()

    while True:

        print("\n========== MENU GRAFO ==========")
        print("1 - Inserir vertice")
        print("2 - Inserir aresta")
        print("3 - Remover vertice")
        print("4 - Remover aresta")
        print("5 - Verificar se existe aresta")
        print("6 - Listar vizinhos")
        print("7 - Mostrar graus dos vertices")
        print("8 - Verificar percurso")
        print("9 - Exibir grafo")
        print("0 - Sair")

        opcao = input("\nEscolha uma opcao: ")

        if opcao == "1":

            vertice = input("Digite o vertice: ")

            inserir_vertice(matriz, vertices, vertice)

        elif opcao == "2":

            origem = input("Digite a origem: ")
            destino = input("Digite o destino: ")

            tipo = input("Nao direcionado? (s/n): ")

            if tipo == "s":
                inserir_aresta(matriz, vertices, origem, destino, True)
            else:
                inserir_aresta(matriz, vertices, origem, destino)

            print("Aresta adicionada!")

        elif opcao == "3":

            vertice = input("Digite o vertice que deseja remover: ")

            remover_vertice(matriz, vertices, vertice)

        elif opcao == "4":

            origem = input("Digite a origem: ")
            destino = input("Digite o destino: ")

            tipo = input("Nao direcionado? (s/n): ")

            if tipo == "s":
                remover_aresta(matriz, vertices, origem, destino, True)
            else:
                remover_aresta(matriz, vertices, origem, destino)

        elif opcao == "5":

            origem = input("Digite a origem: ")
            destino = input("Digite o destino: ")

            if existe_aresta(matriz, vertices, origem, destino):
                print("A aresta existe!")
            else:
                print("A aresta nao existe.")

        elif opcao == "6":

            vertice = input("Digite o vertice: ")

            listar_vizinhos(matriz, vertices, vertice)

        elif opcao == "7":

            graus = grau_vertices(matriz, vertices)

            for vertice in graus:

                print("\nVertice:", vertice)
                print("Grau de saida:", graus[vertice]["saida"])
                print("Grau de entrada:", graus[vertice]["entrada"])
                print("Grau total:", graus[vertice]["total"])

        elif opcao == "8":

            caminho = input("Digite o percurso separado por virgula: ")

            caminho = caminho.split(",")

            if percurso_valido(matriz, vertices, caminho):
                print("O percurso e valido!")
            else:
                print("O percurso nao e valido.")

        elif opcao == "9":

            exibir_grafo(matriz, vertices)

        elif opcao == "0":

            print("Encerrando programa...")
            break

        else:
            print("Opcao invalida!")


if __name__ == "__main__":
    main()
