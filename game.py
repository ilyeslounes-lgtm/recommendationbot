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
    {"Name": "Portal 2", "genre": "Puzzle, Adventure", "platform": "PC", "mood": "fun", "difficulty": "medium", "year": 2011}
]
#lista på alla spelen med genre mood svårighets grad och utgivningsdatum 
while True:
    genre = input("Vilken genre gillar du? (skriv 'exit' för att avsluta) ")
    
    if genre == "exit":
        break
    #En while loop där koden körs så länge vilkoret är sant eller om användaren skriver exit
        
       

    mood = input("Vilken stamning vill du ha? ")
    #Frågar användaren vilken mood hen vill ha
    best_score = 0
    #bästa poängen hittils
    best_game 
    #vilket spel som ska vara det bästa
    for game in games:
        score = 0
        # går igenom alla spel tror jag idk
        if genre in game["genre"] :
            score += 2
            #Om nyckelordet t.ex Action finns i användarens input så kommer spelet få 2 poäng
        if mood == game["mood"] :
            score += 1
            #om nyckelordet t.ex serious finns i användarnens input så kommer spelet få 1 poäng
        if score > best_score:
            best_score = score
            best_game = game["Name"]
            #om bästa poängen är större än det urspurnglia så kommer det vara det bästa spelet
            
            print("Vi rekommenderar:", best_game)
    
    #de rekommenderar spelet med det högsta poäng




