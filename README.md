# Intro    
Op zich leek de opdracht redelijk behapbaar en al grotendeels uitgevoerd middels de oefeningen in de module.
Alleen om dit te vertalen en de oefeningen op de juiste manier en volgorde te implementeren was toch een behoorlijke uitdaging.
Met name omdat het toch een heel nieuw terein was en elke afwijking toch het nodige speurwerk op internet vergde.
Maar door alles in brokken werkend te krijgen en daarna aan elkaar te koppelen is het toch uiteindelijk gelukt.

# werking website op VPS
Door het verwijzen naar de juiste service in de NGINX configuratie wordt er een verbinding gemaakt middels Gunicorn met de Flask app. Welk op zijn beurt weer zichtbaar is op het ip adres.

# Workflow
Na een aanpassing in de code wordt automatisch de workflow gestart in Github Actions:
```sh
on: push
```
Hierna wordt de code gecontroleerd op fouten middels pytest:
```sh
name: Run tests
run: python -m pytest
```
Als er aan de voorwaarde is voldaan kan de volgende job gestart worden waarin de code uitgerold kan worden:
```sh
jobs:
  needs: run-tests
```
# SSH
Om verbinding te maken tussen Github en de server, zodat de nieuwe code geupload kan worden, moeten de inloggegevens vastgelegd worden in Github.
Je wil geen wachtwoorden vastleggen, dus maak je verbinding middels SSH key.
Door onderstaande variabelen, die gehaald worden uit de settings van Github, kan er verbinding gelegd worden naar server:
```sh
uses: appleboy/ssh-action@v0.1.10
        with:
          host: ${{ secrets.HOSTNAME }}
          username: ${{ secrets.USERNAME }}
          key: ${{ secrets.KEY }}
          command_timeout: 30m
```

# .SH file
Aan het einde van de workflow wordt onderstaand script aangeroepen die bash commando's uitvoert:
```sh
script: ./pull.sh
```
Hierin worden de bestanden opgehaald waarin code is aangepast.
En ten slotte de service herstart zodat online de aangepaste code zichtbaar is!!
```sh
cd CD
git pull
systemctl restart CD.service
```








