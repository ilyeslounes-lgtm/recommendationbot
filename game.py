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
genre = input("Vilken genre gillar du? ")
mood = input("Vilken stamning vill du ha? ")
best_score = 0
best_game = ""

for game in games :
    score = 0
    if game["genre"] == genre: 
        score += 2
    if game [ "mood" ] == mood: 
        score += 1
    if score > best_score:
        best_score = score
        best_game = game["Name"]

print("Vi rekommenderar:", best_game)




