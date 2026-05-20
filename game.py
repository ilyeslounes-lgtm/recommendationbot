 = [
    {"Name": "Minecraft", "genre": "Sandbox", "platform": "all", "mood": "happy", "difficulty": "easy", "year": 2009},
    {"Name": "Half-Life 2", "genre": "FPS", "platform": "PC", "mood": "happy", "difficulty": "medium", "year": 2004},
    {"Name": "GTA IV", "genre": "Action, Open World", "platform": "all", "mood": "serious", "difficulty": "medium", "year": 2008},
    {"Name": "Red Dead Redemption 2", "genre": "Action, Open World", "platform": "all", "mood": "calm", "difficulty": "medium", "year": 2018},
    {"Name": "GTA V", "genre": "Action", "platform": "all", "mood": "fun", "difficulty": "medium", "year": 2013},
    {"Name": "Batman: Arkham Asylum", "genre": "Action", "platform": "all", "mood": "dark", "difficulty": "medium", "year": 2009},
    {"Name": "Elden Ring", "genre": "Open World, Fight", "platform": "all", "mood": "epic", "difficulty": "hard", "year": 2022},
    {"Name": "Batman: Arkham Knight", "genre": "Open World, Fight", "platform": "all", "mood": "dark", "difficulty": "medium", "year": 2015},
    {"Name": "Marvel's Spider-Man", "genre": "Action, Adventure", "platform": "PlayStation", "mood": "heroic", "difficulty": "medium", "year": 2019},
    {"Name": "Portal 2", "genre": "Puzzle, Adventure", "platform": "PC", "mood": "fun", "difficulty": "medium", "year": 2011}
]

while True:
    genre = input("Vilken genre gillar du? (skriv 'exit' for att avsluta) ")

    if genre == "exit":
        break
    #En while loop dar koden kors sa lange vilkoret er sant eller om anvandaren skriver exit

    mood = input("Vilken stamning vill du ha? ")
    #Fragar anvandaren vilken mood hen vill ha

    platform = input("Vilken platform vill du ha? ")

    difficulty = input("Vilken difficulty vill du ha? ")

    recommendations = []

    best_score = 0
    #basta poangen hittils

    best_game = ""
    #vilket spel som ska vara det basta

    for game in games:
        score = 0
        #Gar igenom alla spel

        if genre in game["genre"]:
            score += 2
            #Om nyckelordet t.ex Action finns i anvandarens input sa kommer spelet fa 2 poang

        if mood == game["mood"]:
            score += 1
            #Om nyckelordet t.ex serious finns i anvandarens input sa kommer spelet fa 1 poang

        if platform == game["platform"]:
            score += 1
            #Om platformen matchar far spelet 1 poang

        if difficulty == game["difficulty"]:
            score += 1
            #Om difficulty matchar far spelet 1 poang

        if score > best_score:
            best_score = score
            best_game = game["Name"]
            #Om basta poangen ar storre an den gamla sa blir det det basta spelet

        recommendations.append((score, game["Name"]))

    recommendations.sort(reverse=True)

    print("\nVi rekommenderar:")

    for score, name in recommendations[:3]:
        print("-", name, "(Poang:", score, ")")

    print("Basta spelet for dig ar:", best_game)




