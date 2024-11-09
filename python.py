def rank (vitoria, derrota):
    saldo = vitoria - derrota

    if saldo <= 10:
        print("parabens pelas 10 vitórias! Seu Rank é: FERRO")
  
    elif saldo <= 20:
        print("parabens pelas vitórias! Seu Rank é: BRONZE")
  
    elif saldo <= 50:
        print("parabens pelas 50 vitórias! Seu Rank é: PRATA")
  
    elif saldo <= 80:
        print("parabens pelas 80 vitórias! Seu Rank é: OURO")
  
    elif saldo <= 90:
        print("parabens pelas 90 vitórias! Seu Rank é: DIAMANTE")
  
    elif saldo <= 100:
        print("parabens pelas 100 vitórias! Seu Rank é: LENDARIO")
       
    else:
        print("parabens por alcançar o ultimo estagio! Seu Rank é: IMORTAL")

vitoria = int(input("Quantas vitórias vc tem? "))
derrota = int(input("Quantas derrotas vc tem? "))
rank(vitoria, derrota)