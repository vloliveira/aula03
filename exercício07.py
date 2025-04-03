tipoCombustivel = input("Digite G para gasolina e E para etanol: ")
litros = float(input("Quantos litros? "))

etanol = 4.90
gasolina = 5.80

if tipoCombustivel == "E" or tipoCombustivel == "e":
    valor = etanol*litros
    print(f"O valor do combustível é de R${valor}")
else:
    if tipoCombustivel == "G" or tipoCombustivel == "g":
        valor = gasolina * litros
        print(f"O valor do combustível é de R${valor}")
    else:
        print("Tente novamente e digite G para gasolina e E para etanol ")