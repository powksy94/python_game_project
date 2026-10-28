# importer random et time
import random, time

# importer les classes character et monster depuis entities
from database.entities import Character, Monster
# importer les collections characters et monsters depuis db_collections
from database.db_collections import monsters, players
# importer les outils du jeux depuis utils
from utils.utils import display_team, get_choices, display_available_characters

# fonction créer une équipe
def initiate_team(display_characters):
    # instancier une list de personnage
    char_list = list(display_characters)
    # tableau équipe = vide par défault
    team = []

    # instancier la variable create_team avec team et char_list en paramètres
    create_team(team, char_list)
    return team

def select_character(char_list, team):
     # fonction display_team
        display_team(team)
        # afficher (choisir un personnage (avec le nombre actuel de personnages choisi sur 3))
        print(f" Choisir un personnage ({len(team)}/3) ")
        # instancier la variable available avec l'appel de la fonction qui liste les personnages disponible
        available = display_available_characters(char_list, team)
        # instancier la variable choix (en comptant les éléments de la liste available)
        choice = get_choices(len(available))
        # enlever le personnage choisi de la liste 
        return available[choice - 1]

def build_character(char_data):
    # instancier player avec les paramètres de la classe Character
    return Character(
        char_data["name"],
        char_data["atk"],
        char_data["def"],
        char_data["pv"],
        char_data["atout"],
        char_data["ultime"],
    )

def build_monster(monster_data):
    # instancier monster avec les paramètres de la classe Monster
    return Monster(
        name=monster_data["name"],
        atk=monster_data["atk"],
        defense=monster_data["def"],
        pv=monster_data["pv"],
        atout=monster_data["atout"],
        ultime=monster_data["ultime"]
    )

def create_team(team, char_list):

    # boucle infinie tant que l'équipe n'a pas 3 personnages
    while len(team) < 3:
        # attribuer à la variable char_data la méthode select_character
        char_data = select_character(char_list, team)
        # attribuer à la variable player la méthode build_character
        player = build_character(char_data)
        # ajouter le joueur selectionné à l'équipe
        team.append(player)

    print("Equipe complète")
    display_team(team)
    return team

# instancier la variable nombre maximum de tour à 10
MAX_ROUNDS = 10

# fonction d'attente entre chaque tour
def time_between_rounds():
    # variable d'attente 
    wait = 1.5
    print(" Prochain tour")
    # appel de la fonction time pour attendre
    time.sleep(wait)

# fonction de saut de ligne 
def line_break():
    # boucle for de 50 saut de ligne
    print("\n" * 50)

# fonction de pause entre chaque tour
def pause_between_rounds():
    # appel de la fonction d'attente
    time_between_rounds()
    # appel de la fonction saut de ligne
    line_break()

# fonction pour créer une liste qui va stocker les scores en cours de partie
def init_kills(team):
    return {char.name: 0 for char in team}

# fonction de selection aléatoire d'un monstre
def spawn_random_monster():
    # instancier variable monster_data avec appel de la fonction random en parcourant la liste des monstres avec find
    monster_data = random.choice(list(monsters.find()))
    # renvoie la classe Monster avec chacun des paramètres du monstre
    return build_monster(monster_data)

# fonction qui vérifie les survivants
def has_survivors(team):
    # renvoie les personnages survivants
    return any(char.is_alive() for char in team)

# fonction qui renvoie le premier perso vivant de l'équipe
def get_first_alive(team):
    return next((char for char in team if char.is_alive()), None)

# fonction du système d'attaque 
def perform_attack(attacker, defender):
    # attribuer dmg et skill au personnage attaquant
    dmg, skill = attacker.attack(defender)
    # afficher (perso attaque perso)
    print(f" {attacker.name} inflige {dmg} dégâts à {defender.name}")
    # si perso a un skill
    if skill:
        # affiche (perso utilise skill)
        print(f" + {attacker.name} utilise [{skill}] !")

# fonction de combat
def fight(hero, enemy):
    # afficher combat en cours
    print(f"\nCombat : {hero.name} VS {enemy.name}")
    # boucle infinie tant que partie en cours 
    while True:
        # appel fonction système attaque
        perform_attack(hero, enemy)
        # condition si l'ennemi est mort
        if not enemy.is_alive():
            # renvoie TRUE
            return True
        # appel fonction pause
        pause_between_rounds()

        perform_attack(enemy, hero)
        # condition si le hero est mort
        if not hero.is_alive():
            # afficher la mort du héros
            print(f"{hero.name} est tombé dans les ténèbres !")
            line_break()
            # renvoie FALSE
            return False
        # appel fonction pause
        pause_between_rounds()

# fonction fin de partie
def display_results(player_name, score, kills):
    # afficher game over
    print(f"\n Game Over ! {player_name}, ton score: {score} monstres vaincus !")
        # pour chaque perso, compte de kill du perso
    for name, count in kills.items():
        # afficher le nom et son compte de monstres vaincus
        print(f" - {name} - {count} monstres vaincus !")


# fonction de sauvegarde de la partie
def save_game(player_name, score,  kills):
    # inserer le joueur et ses scores dans la collection joueur
    players.insert_one({"name": player_name, "score": score, "kills": kills})

# fonction de gameplay 
def play(player_name, team):
    # score instancié à 0
    score = 0
    # variable kills appelant la fonction init kills de l'équipe
    kills = init_kills(team)

    # boucle tant que l'équipe a des survivants et que le score est inférieur au nombre de tours maximum
    while has_survivors(team) and score < MAX_ROUNDS:
        # variable hero avec le premier de l'équipe en vie
        hero = get_first_alive(team)
        # variable ennemi avec appel de fonction random monstres
        enemy = spawn_random_monster()

        # condition de combat (hero, enemy)
        if fight(hero, enemy):
            # incrémenter score
            score += 1
            # incrémenter les kills avec nom du personnage
            kills[hero.name] += 1
            # afficher le montre vaincu et le score actuel de la partie
            print(f"{enemy.name} est vaincu ! (Score = {score})")
            # appel fonction pause
            pause_between_rounds()

    # appel fonction de la liste de score
    display_results(player_name, score, kills)
    # sauvegarde de l'état de la partie
    save_game(player_name, score, kills)
    # demande appuyer sur entrée
    input("Appuyez sur entrée")
    # saut de ligne
    line_break()

# fonction afficher score 
def display_ranking():
    # Afficher titre classement
    print("\n Classement ")
    # recuperer score à partir de la base
    # ouvrir la base 
    # instancier la variable ranking qui parcours players et trie dans l'ordre décroissant
    ranking = players.find().sort("score", -1)
    # pour chaque élément, joueur => énumerer avec le paramètre classement et 1
    for i, player in enumerate(ranking, 1):
        # afficher le score du joueur et son nombre de monstres vaincus
        print(f"{i}. {player['name']} - {player['score']} monstres vaincus")
        # si le joueur contient un élement dans kills
        if "kills" in player:
            # pour chaque nom de personnage, et son nombre dans la collection player paramètre kills
            for char_name, count in player["kills"].items():
                # afficher le nom du personnage et le nombre de monstres vaincus
                print(f"    - {char_name} : {count} montres vaincus")
    # demander appuyer sur entrée
    input("Appuyez sur entrée")
    # appel fonction saut de ligne
    line_break()