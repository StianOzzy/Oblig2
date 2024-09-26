import random
player_count = int(input("How many players?\n\n> "))
player_number = 0


# Starten av loopen
for i in range (player_count):


    # Starter spillernavn-intervallen, og skriver ut navnet på spilleren
    player_number = player_number + 1

    player_throws = int(input(f"\nHow many throws should Player #{player_number} throw?\n"))
    print(f"\nPlayer #{player_number}:")

    # Kast med definerin
    for i in range(player_throws):


        throw_value = (random.randint(0,20))

        if throw_value == 0:
            print(f"Player {player_number} throws {throw_value}")
        if throw_value > 0 and throw_value <= 20:
            multiplier_value = (random.randint(0,3))
            if multiplier_value <= 1:
                throw_value = throw_value * 1
                print(f"Player {player_number} throws {throw_value}")
            elif multiplier_value == 2:
                throw_value_m = throw_value * 2
                print(f"Player {player_number} throws {throw_value_m} ({throw_value} with a {multiplier_value}x-multiplier)")
            elif multiplier_value == 3:
                throw_value_m = throw_value * 3
                print(f"Player {player_number} throws {throw_value_m} ({throw_value} with a {multiplier_value}x-multiplier)")
        elif throw_value == 21:
            throw_value = 25
            print(f"Player {player_number} throws 25")
        elif throw_value == 22:
            throw_value = 50
            print(f"Player {player_number} throws 50")
        else:
            print("Error Code: RNG faulty")