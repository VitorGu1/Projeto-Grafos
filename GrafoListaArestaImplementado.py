
def criar_grafo():
    vertices = []
    arestas = []

    return vertices, arestas


def inserir_vertice(vertices, vertice):
    if vertice not in vertices:
        vertices.append(vertice)
        print("Vertice adicionado!")
    else:
        print("Esse vertice ja existe.")


def inserir_aresta(vertices, arestas, origem, destino, nao_direcionado=False):

    
    if origem not in vertices:
        inserir_vertice(vertices, origem)

    if destino not in vertices:
        inserir_vertice(vertices, destino)

    
    if [origem, destino] not in arestas:
        arestas.append([origem, destino])

   
    if nao_direcionado:
        if [destino, origem] not in arestas:
            arestas.append([destino, origem])


def remover_aresta(arestas, origem, destino, nao_direcionado=False):

    if [origem, destino] in arestas:
        arestas.remove([origem, destino])

    if nao_direcionado:
        if [destino, origem] in arestas:
            arestas.remove([destino, origem])


def remover_vertice(vertices, arestas, vertice):

    if vertice in vertices:
        vertices.remove(vertice)

        i = 0

        while i < len(arestas):
            if arestas[i][0] == vertice or arestas[i][1] == vertice:
                arestas.pop(i)
            else:
                i = i + 1

        print("Vertice removido!")
    else:
        print("Vertice nao encontrado.")


def existe_aresta(arestas, origem, destino):

    for aresta in arestas:
        if aresta == [origem, destino]:
            return True

    return False


def vizinhos(vertices, arestas, vertice):

    lista_vizinhos = []

    for aresta in arestas:
        origem = aresta[0]
        destino = aresta[1]

        if origem == vertice:
            if destino not in lista_vizinhos:
                lista_vizinhos.append(destino)

    return lista_vizinhos


def grau_vertices(vertices, arestas):

    graus = {}

    for vertice in vertices:
        graus[vertice] = {
            "entrada": 0,
            "saida": 0,
            "total": 0
        }

    for aresta in arestas:
        origem = aresta[0]
        destino = aresta[1]

        graus[origem]["saida"] = graus[origem]["saida"] + 1

        graus[destino]["entrada"] = graus[destino]["entrada"] + 1

    for vertice in vertices:
        entrada = graus[vertice]["entrada"]
        saida = graus[vertice]["saida"]

        graus[vertice]["total"] = entrada + saida

    return graus


def percurso_valido(arestas, caminho):

    for i in range(len(caminho) - 1):

        origem = caminho[i]
        destino = caminho[i + 1]

        if existe_aresta(arestas, origem, destino) == False:
            return False

    return True


def listar_vizinhos(vertices, arestas, vertice):

    lista = vizinhos(vertices, arestas, vertice)

    print("Vizinhos de", vertice, ":", lista)


def exibir_grafo(vertices, arestas):

    print("\nVertices:", vertices)

    print("\nArestas:")

    for aresta in arestas:
        origem = aresta[0]
        destino = aresta[1]

        print(origem, "->", destino)


def main():

    vertices, arestas = criar_grafo()

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
            inserir_vertice(vertices, vertice)

        elif opcao == "2":

            origem = input("Digite a origem: ")
            destino = input("Digite o destino: ")

            tipo = input("Nao direcionado? (s/n): ")

            if tipo == "s":
                inserir_aresta(vertices, arestas, origem, destino, True)
            else:
                inserir_aresta(vertices, arestas, origem, destino)

            print("Aresta adicionada!")

        elif opcao == "3":

            vertice = input("Digite o vertice que deseja remover: ")
            remover_vertice(vertices, arestas, vertice)

        elif opcao == "4":

            origem = input("Digite a origem: ")
            destino = input("Digite o destino: ")

            tipo = input("Nao direcionado? (s/n): ")

            if tipo == "s":
                remover_aresta(arestas, origem, destino, True)
            else:
                remover_aresta(arestas, origem, destino)

            print("Operacao realizada!")

        elif opcao == "5":

            origem = input("Digite a origem: ")
            destino = input("Digite o destino: ")

            if existe_aresta(arestas, origem, destino):
                print("A aresta existe!")
            else:
                print("A aresta nao existe.")

        elif opcao == "6":

            vertice = input("Digite o vertice: ")
            listar_vizinhos(vertices, arestas, vertice)

        elif opcao == "7":

            graus = grau_vertices(vertices, arestas)

            for vertice in graus:
                print("\nVertice:", vertice)
                print("Grau de entrada:", graus[vertice]["entrada"])
                print("Grau de saida:", graus[vertice]["saida"])
                print("Grau total:", graus[vertice]["total"])

        elif opcao == "8":

            caminho = input("Digite o percurso separado por virgula: ")

            caminho = caminho.split(",")

            if percurso_valido(arestas, caminho):
                print("O percurso e valido!")
            else:
                print("O percurso nao e valido.")

        elif opcao == "9":

            exibir_grafo(vertices, arestas)

        elif opcao == "0":

            print("Encerrando programa...")
            break

        else:
            print("Opcao invalida!")


if __name__ == "__main__":
    main()
