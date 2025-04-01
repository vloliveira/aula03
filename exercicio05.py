n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))

media = (n1+n2+n3)/3

if media >= 7:
    print(f"O aluno foi aprovado com {media:.2f}!")
else:
    if media < 4:
        print(f"O aluno foi reprovado com média {media:.2f}!")
    else:
        print(f"O aluno está de recuperação com média {media:.2f}!")


