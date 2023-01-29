# Exerciții Opționale - grad de dificultate: Mediu spre greu (may need Google)
# 1. Ne imaginăm o echipă de fotbal pt teren sintetic.
# 3 Schimbări maxime admise:
# ● Declară o Listă cu 5 jucători
# ● Schimbari_efectuate = te joci tu cu valori diferite
# ● Schimbari_max = 3
# Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
# - Efectuează schimbarea
# - Șterge jucătorul scos din listă
# - Adaugă jucătorul intrat
# - Afișază a intrat x, a ieșit y, mai ai z schimbări
# Dacă jucătorul nu e în teren:
# - Afișază ‘nu se poate efectua schimbarea deoarece jucătorul x nu e în
# teren’
# - Afișază ‘mai ai z schimbări’
# Testează codul cu diferite valori
#
# Google search hint
# “how to check if item is în list python”
print(20 * '-','Exercitiu optional',20 * '-')

players_in_field = ["Mohamed Salah", "Karim Benzema", "Sadio Mane", "Cristiano Ronaldo","Harry Kane"]
changes_made = 0
max_changes = 3


print('The game starts with next players: ')
for i in range(len(players_in_field)):
    print(players_in_field[i])
remaining_changes = max_changes - changes_made
player_replaced = input('Who should take a break? \n')
if player_replaced == ' ' and changes_made <= 0:
    print('At some point you will have to change a player, perhaps you should think about it!')
    exit(0)
if player_replaced not in players_in_field:
    print(f'This player is not on the field, you have to choose someone else!')
    player_replaced = input('Who should take a break? \n')
    if player_replaced == ' ' and changes_made <= 0:
        print('At some point you will have to change a player, perhaps you should think about it!')
        exit(0)

for x in players_in_field:
    if x == player_replaced:
        break
print(players_in_field)

if (max_changes - changes_made) < 0:
    print('You achieve the maximum number of changes allowed!')
    exit(0)

replace = input('Who dou you want to get into game? \n')
players_check = players_in_field.count(replace)
if players_check == 1 and (max_changes >= changes_made >= 0):
    changes_made += 1
print(f'{replace} entered in game, {player_replaced} got out, you have {max_changes - changes_made} changes to make.')


players_in_field.remove(player_replaced)
players_in_field.append(replace)
print(players_in_field)

