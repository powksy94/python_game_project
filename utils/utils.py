# fonction d'options du menu
def menu_options ():
    # lancer jeu
    print("1. Jouer au jeu MEDIEVAL GAME")
    # afficher score
    print("2. Afficher le classement")
    # quitter
    print("3. Quitter le jeu")

# fonction de choix des options du menu
def get_choices(max_options):
    # boucle sur tout element du menu
    while True:
        # choix (options, erreur)
        choice = input(" Ton choix : ")
        # demander d'entrer un nombre entre le premier element et le choix maximum d'options
        # condition pour vérifier si le nombre entré et compris entre 1 et le nombre maximum d'options
        if choice.isdigit() and 1 <= int(choice) <= max_options:
            # renvoie la valeur du choix
            return int(choice)
        # sinon afficher message d'erreur
        print(f"Veuillez entrer un nombre entre 1 et {max_options} !")
        # redemander

# fonction pour verifier le pseudo du joueur
def get_valid_name():
    # tant que True
    while True:
        # demander d'entrer un pseudo
        player_name = input("Ton pseudo : ")
        # variable name qui compte le nombre de caractères
        name = len(player_name)
        # condition si le nom a 3 caractères ou plus
        if name >= 3:
            # renvoie le nom
            return player_name
        # sinon afficher message pseudo trop court
        print("Pseudo trop court ! Veuillez insérer un pseudo d'au moins 3 caractères")

# fonction afficher équipe
def display_team(team):
    # condition si l'équipe est vide
    if len(team) == 0:
        # afficher équipe vide
        print("Equipe vide !")
    # sinon 
    else:
        # afficher ton équipe
        print("\n Ton équipe ")
        # pour chaque personnage de l'équipe
        for i, char in enumerate(team, 1):
            # afficher ses statistiques
            print(f"{i} . {char.name} . (ATK : {char.atk}) . (DEF: {char.defense}) . (PV: {char.pv}) ")

# fonction afficher personnages disponibles avec paramètre liste de personnage et équipe
def display_available_characters(char_list, team):
    # liste d'équipe avec chaque personnage de l'équipe
    team_names = [char.name for char in team]
    # liste des personnages disponibles initialement vide
    available = []
    # pour chaque personnage dans la liste de personnage
    for char in char_list:
        # si le nom du personnage n'est pas dans la liste de noms de l'équipe
        if char["name"] not in team_names:
        # ajouter à la liste des persos disponible 
            available.append(char)

    # pour chaque personnage disponible
    for i, char in enumerate(available, 1):
        # afficher ses stats
        print(f"{i} . {char["name"]} . (ATK : {char["atk"]}) . (DEF: {char["def"]}) . (PV: {char["pv"]}) ")
    # renvoyer la liste de disponibilité
    return available