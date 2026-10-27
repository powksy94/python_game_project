# importer random et time

# importer les classes character et monster depuis entities
# importer les collections characters et monsters depuis db_collections
# importer les outils du jeux depuis utils

# fonction créer une équipe
    # instancier une list de personnage
    # tableau équipe = vide par défault

    # boucle infinie tant que l'équipe n'a pas 3 personnages
        # fonction display_team
        # afficher (choisir un personnage (avec le nombre actuel de personnages choisi sur 3))
        # instancier la variable available avec l'appel de la fonction qui liste les personnages disponible
        # instancier la variable choix (en comptant les éléments de la liste available)
        # enlever le personnage choisi de la liste 
        # instancier player avec les paramètres de la classe Character
        # ajouter le joueur selectionné à l'équipe

# fonction d'attente entre chaque tour
    # variable d'attente 
        # appel de la fonction time pour attendre

# fonction de saut de ligne 
    # boucle for de 50 saut de ligne

# fonction de pause entre chaque tour
    # appel de la fonction d'attente
    # appel de la fonction saut de ligne

# fonction pour créer une liste qui va stocker les scores en cours de partie

# fonction de selection aléatoire d'un monstre
    # instancier variable monster_data avec appel de la fonction random en parcourant la liste des monstres avec find
    # renvoie la classe Monster avec chacun des paramètres du monstre

# fonction qui vérifie les survivants
    # renvoie les personnages survivants

# fonction du système d'attaque 
    # afficher (perso attaque perso)
    # si perso a un skill
        # affiche (perso utilise skill)

# fonction de combat
    # boucle infinie tant que partie en cours 
        # appel fonction système attaque
        # condition si l'ennemi est mort
            # renvoie TRUE
        # appel fonction pause

        # condition si le hero est mort
            # renvoie TRUE
        # appel fonction pause

# fonction fin de partie
    # afficher game over
        # pour chaque perso, compte de kill du perso
            # afficher le nom et son compte de monstres vaincus

# fonction de sauvegarde de la partie
    # inserer le joueur et ses scores dans la collection joueur

# fonction de gameplay 
    # score instancié à 0
    # variable kills appelant la fonction init kills de l'équipe

    # boucle tant que l'équipe a des survivants et que le score est inférieur au nombre de tours maximum
        # variable hero avec le premier de l'équipe en vie
        # variable ennemi avec appel de fonction random monstres

        # condition de combat (hero, enemy)
            # incrémenter score
            # incrémenter les kills avec nom du personnage
            # afficher le montre vaincu et le score actuel de la partie
            # appel fonction pause
    # appel fonction de la liste de score
    # sauvegarde de l'état de la partie
    # demande appuyer sur entrée
    # saut de ligne

# fonction afficher score 
    # recuperer score à partir de la base
        # ouvrir la base 
        # acceder à la collection score
            # find
            # convertir curseur en list
            # trier dans l'ordre décroissant du score
            # pour chaque élément, joueur => énumerer avec le paramètre classement et 1
                # afficher le score du joueur et son nombre de monstres vaincus
                # si le joueur contient un élement dans kills
                    # pour chaque nom de personnage, et son nombre dans la collection player paramètre kills
                        # afficher le nom du personnage et le nombre de monstres vaincus
            # demander appuyer sur entrée
            # appel fonction saut de ligne