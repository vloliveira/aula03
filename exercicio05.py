n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))

media = (n1+n2+n3)/3

if media >= 7:
    print(f"O aluno foi aprovado {media}!")
else:
    print(f"O aluno foi reprovado com média {media}!")