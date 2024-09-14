Programmering 

Oppgave 1 - If og else

1. Ta et tall fra brukeren på følgende måte: input("Hva er svaret på det ultimate spørsmålet om livet, universet og alle ting? Hint: Det er et tall."). Konverter inputen til int og lag en if-test som sjekker om verdien er lik 42. Hvis dette er tilfellet, skriv ut "Det stemmer, meningen med livet er 42!", hvis ikke; skriv ut "FEIL!".
2. 2.Legge til én ekstra sjekk i denne if-testen som sjekker om input-tallet er mellom 30 og 50, altså større enn 30 og mindre enn 50 på samme tid (hint: logiske operatorer). Hvis dette er tilfellet, skriv ut "Nærme, men feil." 

 

Oppgave 2 - Løkker 

Skriv et program som skriver ut alle oddetall fra og med 9 til 101. Lag to alternativer for programmet; en hvor du benytter en for-løkke og hvor du benytter en while-løkke. 

 

Oppgave 3 - Lister 

Opprett en liste med Tolkien sine bøker: 

    The Hobbit 
    Farmer Giles of Ham  
    The Fellowship of the Ring 
    The Two Towers 
    The Return of the King 
    The Adventures of Tom Bombadil  
    Tree and Leaf 

     Skriv ut de to første og de to siste bøkene i listen.
    Legg til to av bøkene som ble utgitt etter hans død: 
        The Silmarillion 
        Unfinished Tales  
    Gjør endringer på de tre bøkene i Lord of the Rings trilogien og legg til "Lord of the Rings: " foran hver av dem. (hvis dere ikke vet hvilke dette er, vet Google) 
    Sorter lista og skriv den ut. 

 

Oppgave 4 - Iterere gjennom en liste 

Opprett en tom liste. Gå gjennom listen med bøker fra Oppgave 3 og legg dem til i den tomme listen hvis de er i Lord of the Rings-trilogien. Skriv så ut innholdet i den nye lista ved hjelp av en for-løkke. Det er flere måter man kan skrive en for-løkke på, forsøk å demonstrere et par forskjellige i denne oppgaven. 

 

Oppgave 5 - for-løkke(r) - Dart 

    I denne oppgaven skal du simulere et dartspill. Det skal kastes 3 piler. Hvert kast gir mellom 0 og 60 poeng. Du kan bruke randrange(<fra>, <til>) for å generere en tilfeldig score for hvert kast. For mer info angående randrange, se her 

    Links to an external site.. Skriv ut sluttscoren. 
    Utvid oppgaven til å ta som input hvor mange spillere som skal spille. Hver spiller skal kaste 3 piler hver. Spilleren skal kaste alle 3 pilene før neste spiller skal kaste. Skriv ut resultat for hver spiller når spilleren er ferdig med å kaste. 

 

Oppgave 6 – Pakkeliste 

Du skal lage et lite program som gjør det mulig å lage en pakkeliste for når du skal ut og reise. Programmet skal først skrive ut hvilke valg brukeren har for listeoperasjoner, i form av kommandoer: En for å legge til noe, en for å slette noe, og en for å skrive ut hele listen. Brukeren skal deretter kunne skrive en input for å velge hvilken kommando som skal tas i bruk. Programmet skal gå i en evig løkke frem til brukeren avslutter det med en egen kommando for dette. Du velger selv hva kommandoene skal være (F.eks. enkeltbokstaver eller ord).

  
Bonusoppgaver

Bonusoppgavene er frivillige og typisk vanskeligere enn hovedoppgavene av en oblig. Disse er fine å gjennomføre for å ytterligere teste kompetansen din, noe som kan være lurt for å forberede seg på eksamen.

Bonusoppgave 1 – Dart 2.0 

Vi her skal forbedre dartoppgaven.  

     Utvid programmet til å ta imot antall piler og antall runder hver spiller skal kaste. 
     Fremfor et tilfeldig tall mellom 0 og 60, så skal du benytte de lovlige poengene man kan få med et kast. Som er 0p, 1-20p (samt dobbel og trippel av disse), 25p (outer bullseye) og 50p (inner bullseye). 

 

Bonusoppgave 2 – Dart 3.0 

Lag et nytt program og bruk det du har lært i de tidligere dartoppgavene (du kan kopiere med deg kode du ønsker å gjenbruke).  
Du skal nå implementere reglene for 301. 
"Du begynner på 301 poeng og målet er å være første mann som får 0 poeng. (Du får minuspoeng fremfor pluss) 
Du trenger en treff i hvilken som helst dobbel for å starte. Ingen piler teller poeng før du har truffet en dobbel. 
Videre er det første mann til å nå nøyaktig 0 poeng ved hjelp av dobbel ut. Hvis et gitt kast fører til mindre enn 0 poeng, vil dette kastet ikke gjelde og poengene vil forbli de samme som før kastet. 
Enkelt fortalt, i 301 starter du og avslutter med dobbel."
