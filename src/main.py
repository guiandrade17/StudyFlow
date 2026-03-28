from src.core import calcular_proxima_revisao

def menu():
    while True:
        print("\n=== Study Flow ===")
        print("1 - Calcular próxima revisão")
        print("2 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                dias = int(input("Digite a quantidade de dias: "))
                resultado = calcular_proxima_revisao(dias)
                print(f"Próxima revisão: {resultado}")
            except ValueError as e:
                print(f"Erro: {e}")

        elif opcao == "2":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()