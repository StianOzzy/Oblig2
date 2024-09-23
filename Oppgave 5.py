import random
player_count = int(input("How many players? "))
player_number = 0

# Starten av loopen
for i in range (player_count):

    # Starter spillernavn-intervallen, og skriver ut navnet på spilleren
    player_number = player_number + 1
    print(f"\nPlayer Number #{player_number}")

    # Kast
    throw_1 = (random.randrange(0,60))
    print(f"Throw 1: {throw_1}")
    throw_2 = (random.randrange(0,60))
    print(f"Throw 2: {throw_2}")
    throw_3 = (random.randrange(0,60))
    print(f"Throw 3: {throw_3}")

    # Sammenlegging av total score
    score = (throw_1 + throw_2 + throw_3)
    print(f"Total Score: {score}")
