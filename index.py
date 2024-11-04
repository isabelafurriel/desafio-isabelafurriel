#Indicando qual o nome do herói e a quantidade de experiência (XP)
nome_heroi = input("Informe o nome do herói: ")
xp = int(input("Informe a quantidade de XP do herói: "))

# Classificando o nível do herói com base no XP
if xp < 1000:
    nivel = "Ferro"
elif 1001 <= xp <= 2000:
    nivel = "Bronze"
elif 2001 <= xp <= 5000:
    nivel = "Prata"
elif 5001 <= xp <= 7000:
    nivel = "Ouro"
elif 7001 <= xp <= 8000:
    nivel = "Platina"
elif 8001 <= xp <= 9000:
    nivel = "Ascendente"
elif 9001 <= xp <= 10000:
    nivel = "Imortal"
else:
    nivel = "Radiante"
# Exibindo a mensagem final
print(f"O Herói {nome_heroi} está no nível de {nivel}")