# importer les éléments des fichiers collection de la database game et utils
import sys

from database.db_collections import characters, seed_db
from utils.utils import menu_options, get_choices, get_valid_name
from game import create_team, play, display_ranking

# remplir la base de données
seed_db()

# Afficher Menu
while True:
    # recuperer le tableau de choix à partir du utils
    menu_options()
    choice = get_choices(3)
    # si lancer jeu choisi 
    if choice == 1:
        # demander d'entrer le pseudo
        player_name = get_valid_name()
            # verifier si le pseudo est accepté
            # appel de la fonction de création d'équipe en parcourant le tableau des personnages
        team = create_team([], list(characters.find()))
        # lancer jeu avec function play
        play(player_name, team)

    # si afficher score choisi
    elif choice == 2:
        # lancer la fonction afficher score
        display_ranking()
        # afficher le score
    # si quitter choisi 
    elif choice == 3:
    # Quitter
        sys.exit()
    # sys.exit()