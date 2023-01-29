# Exerciții Bonus (may need google) .
# 1. Joc ghicit zarul
# Caută pe net și vezi cum se generează un număr random
# Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
# Ia numărul ghicit de la utilizator
# Verifică și afișează dacă utilizatorul a ghicit
# Vei avea 3 opțiuni
# ● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
# ● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
# ● Ai ghicit. Felicitări! Ai ales x si zarul a fost y.
import random
dice_roll = random.randint(1,6)
number_guessed = int(input("Alege un numar de la 1 la 6: \n"))
if number_guessed < dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {number_guessed} dar a fost {dice_roll}.')
elif number_guessed > dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {number_guessed} dar a fost {dice_roll}.')
elif number_guessed == dice_roll:
    print(f'Ai ghicit. Felicitări! Ai ales {number_guessed} si zarul a fost {dice_roll}.')