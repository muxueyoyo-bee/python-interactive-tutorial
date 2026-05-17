heroes = [
    {"name":"战士", "atk":180, "def":120, "hp":5000},
    {"name":"法师", "atk":280, "def":50, "hp":3000},
    {"name":"射手", "atk":220, "def":80, "hp":3500},
    {"name":"坦克", "atk":80, "def":250, "hp":8000},
    {"name":"刺客", "atk":300, "def":40, "hp":2500},
]

ranked = sorted(heroes, key=lambda h: h["atk"] + h["def"] + h["hp"]/100, reverse=True)
for i, h in enumerate(ranked, 1):
    print(f"{i}. {h['name']} (战力:{h["atk"]+h["def"]+h["hp"]//100})")
