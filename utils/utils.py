# tableau d'options du menu
    # lancer jeu
    # afficher score
    # quitter

# fonction de choix des options du menu
    # boucle sur tout element du menu
        # choix (options, erreur)
        # demander d'entrer un nombre entre le premier element et le choix maximum d'options
        # condition pour vérifier si le nombre entré et compris entre 1 et le nombre maximum d'options
            # renvoie la valeur du choix
        # sinon afficher message d'erreur
        # redemander

# fonction pour verifier le pseudo du joueur
    # tant que True
        # demander d'entrer un pseudo
        # variable name qui compte le nombre de caractères
        # condition si le nom a 3 caractères ou plus
            # renvoie le nom
        # sinon afficher message pseudo trop court

# fonction afficher équipe
    # condition si l'équipe est vide
        # afficher équipe vide
    # sinon 
        # afficher ton équipe
        # pour chaque personnage de l'équipe
            # afficher ses statistiques

# fonction afficher personnages disponibles avec paramètre liste de personnage et équipe
    # liste d'équipe avec chaque personnage de l'équipe
    # liste des personnages disponibles initialement vide
    # pour chaque personnage dans la liste de personnage
        # si le nom du personnage n'est pas dans la liste de noms de l'équipe
        # ajouter à la liste des persos disponible 

    # pour chaque personnage disponible
        # afficher ses stats
    # renvoyer la liste de disponibilité
