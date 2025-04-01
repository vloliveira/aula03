time1 = input("Digite o nome do primeiro time: ")
gol1 = int(input(f"Quantos gols o {time1} fez? "))
time2 = input("Digite o nome do segundo time: ")
gol2 = int(input(f"Quantos gols o {time2} fez? "))
if gol1 > gol2:
    print(f"O {time1} venceu a partida!")
else:
    if gol2 > gol1:
        print(f"O {time2} venceu a partida!")
    else:
        print("A partida terminou empatada!")
