nome = input("Digite seu nome: ")
idade = int (input("Digite sua idade: "))
salario = float (input("Digite seu salário: "))
porcentagem = float (input("Digite a % de aumento do seu salário: "))

aumento = (salario * porcentagem)/100
novoSalario = salario + aumento


print (f"Seu nome é {nome}, você tem {idade} anos e seu salário é de R${salario:.2f}, com o aumento de R${aumento:.2f}, será de R${novoSalario:.2f}")
