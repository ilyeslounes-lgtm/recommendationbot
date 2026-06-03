games = [
    {"Name": "Minecraft", "genre": "Sandbox", "platform": "all", "mood": "happy", "difficulty": "easy", "year": 2009},
    {"Name": "Half-Life 2", "genre": "FPS", "platform": "PC", "mood": "happy", "difficulty": "medium", "year": 2004},
    {"Name": "GTA IV", "genre": "Action, Open World", "platform": "all", "mood": "serious", "difficulty": "medium", "year": 2008},
    {"Name": "Red Dead Redemption 2", "genre": "Action, Open World", "platform": "all", "mood": "calm", "difficulty": "medium", "year": 2018},
    {"Name": "GTA V", "genre": "Action", "platform": "all", "mood": "fun", "difficulty": "medium", "year": 2013},
    {"Name": "Batman: Arkham Asylum", "genre": "Action", "platform": "all", "mood": "dark", "difficulty": "medium", "year": 2009},
    {"Name": "Elden Ring", "genre": "Open World, Fight", "platform": "all", "mood": "epic", "difficulty": "hard", "year": 2022},
    {"Name": "Batman: Arkham Knight", "genre": "Open World, Fight", "platform": "all", "mood": "dark", "difficulty": "medium", "year": 2015},
    {"Name": "Marvel's Spider-Man", "genre": "Action, Adventure", "platform": "PlayStation", "mood": "heroic", "difficulty": "medium", "year": 2019},
    {"Name": "Portal 2", "genre": "Puzzle, Adventure", "platform": "PC", "mood": "fun", "difficulty": "medium", "year": 2011},
    {"Name": "Dishonored", "genre": "Action, stealth, immersive", "platform": "all", "mood": "dystopia", "difficulty": "medium", "year": 2012} ,
    {"Name": "The Witcher 3: Wild Hunt", "genre": "RPG, Open World", "platform": "all", "mood": "epic", "difficulty": "medium", "year": 2015},
    {"Name": "Hades", "genre": "Roguelike, Action", "platform": "all", "mood": "fast", "difficulty": "hard", "year": 2020},
    {"Name": "Subnautica", "genre": "Survival, Exploration", "platform": "all", "mood": "calm", "difficulty": "medium", "year": 2018},
    {"Name": "Stardew Valley", "genre": "Farming, Simulation", "platform": "all", "mood": "relaxing", "difficulty": "easy", "year": 2016},
    {"Name": "Sekiro: Shadows Die Twice", "genre": "Action, Soulslike", "platform": "all", "mood": "intense", "difficulty": "hard", "year": 2019},
    {"Name": "Hollow Knight", "genre": "Metroidvania", "platform": "all", "mood": "mysterious", "difficulty": "hard", "year": 2017},
    {"Name": "Titanfall 2", "genre": "FPS", "platform": "PC", "mood": "exciting", "difficulty": "medium", "year": 2016},
    {"Name": "Terraria", "genre": "Sandbox, Survival", "platform": "all", "mood": "creative", "difficulty": "medium", "year": 2011},
    {"Name": "Control", "genre": "Action, Adventure", "platform": "all", "mood": "strange", "difficulty": "medium", "year": 2019},
    {"Name": "Death Stranding", "genre": "Adventure, Open World", "platform": "all", "mood": "atmospheric", "difficulty": "medium", "year": 2019}
]
#frågade AI för 10 random spel för jag inte visste om så många spel
#En databas full av alla spel som rekommendationen kan rekommendera 
# fortsatta tills anvansdren skriver exit
while True:

    # vill veta vilken genre anvandaren vill ha
    genre = input("Vilken genre gillar du? (skriv 'exit' for att avsluta) ")

    # programmet kommer sluta om anvandaren skriver exit
    if genre == "exit":
        break

    # Fragar efter stamning
    mood = input("Vilken stamning vill du ha? ")

    # Fragar efter platform
    platform = input("Vilken platform vill du ha? ")

    # Fragar efter svarighetsgrad
    difficulty = input("Vilken difficulty vill du ha? ")

    # Lista for rekommendationer
    recommendations = []

    # Sparar hogsta poang
    best_score = 0

    # Sparar basta spelet
    best_game = ""

    # gar igenom alla spel i listan
    for game in games:

        # startar fran 0
        score = 0

        # 2 poang om genre passar
        if genre in game["genre"]:
            score += 2

        # 1 poang om stamning passar
        if mood == game["mood"]:
            score += 1

        #  1 poang om platform passar
        if platform == game["platform"]:
            score += 1

        #  1 poang om svarighetsgrad passar
        if difficulty == game["difficulty"]:
            score += 1

        # Sparar spelet med hogst poang
        if score > best_score:
            best_score = score
            best_game = game["Name"]

        # Lagger till spel och poang i listan
        recommendations.append((score, game["Name"]))

    # Sorterar listan efter hogst poang
    recommendations.sort(reverse=True)
    #fick hjalp av AI lite har
    print("\nVi rekommenderar:")
    #"/nVi gor so att dem skriver sakerna dar nere och en separat rad fick hjalp av AI hur
    # Skriver ut topp 3 spel
    for score, name in recommendations[:3]:
        print("-", name, "(Poang:", score, ")")

    # Skriver ut basta spelet
    print("Basta spelet for dig ar:", best_game)

    # Fragar om rekommendationerna var bra
    feedback = input("Var nagon av rekommendationerna bra? (ja/nej) ")

    if feedback == "ja":

        print("Kul! Jag kommer rekommendera liknande spel nasta gang.")

        # Uppdaterar spelets data baserat pa anvandarens val
        for game in games:

            if game["Name"] == best_game:
                game["difficulty"] = difficulty
                game["mood"] = mood

    elif feedback == "nej":

        print("Okej, jag forsoker battre nasta gang.")



