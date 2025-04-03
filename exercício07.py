tipoCombustivel = input("Digite G para gasolina e E para etanol: ")
litros = float(input("Quantos litros? "))

etanol = 4.90
gasolina = 5.80

if tipoCombustivel == "E":
    valor = etanol*litros
    print(f"O valor do combustível é de R${valor}")
else:
    if tipoCombustivel == "G":
        valor = gasolina * litros
        print(f"O valor do combustível é de R${valor}")
    else:
        print("Tente novamente e gigite G para gasolina e E para etanol ")