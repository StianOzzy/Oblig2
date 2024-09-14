# Starter en loop av programmet, slik at man kan teste flere ulike verdier, uten å måtte restarte programmet.
while True:

    # Tar imot brukers input, og gjør lagrer verdien som en integer
    user_input = int(input("Hva er svaret på det ultimate spørsmålet om livet, universet og alle ting? Hint: Det er et tall.\n"))

    # Sjekker om verdien stemmer overens med det ønskede svaret.
    if user_input == 42:
        # Hvis verdien stemmer, så printes melding under, og programmet avsluttes.
        print("Det stemmer, meningen med livet er 42!\n")
        break
    # Hvis svaret ikke stemmmer, så printer programmet at svaret er feil
    else:
        print("FEIL!\n")