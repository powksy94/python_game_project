# crée la classe Character 

    # definir les paramètres initaux de la classe characters
        # instancier les variables selon le paramètre self
        # instancier la variable name
        # instancier la variable attaque
        # instancier la variable defense
        # instancier la variable pv
        # instancier la variable atout
        # instancier la variable ultime
        # instancier la variable tour à 0

    # crée la fonction pour voir si un personnage est en vie
        # renvoyer le personnage ayant des points de vie

    # crée la fonction d'attaque 
        # incrémenter tour
        # instancier la variable damage avec comparer 1 et la valeur atk du personnage qui attaque moins la valeur de la defense de l'unité qui reçoit
        # instancier ma variable skill_used comme null

        # condition si la valeur de l'ultime  et le reste de la division de tour du perso par le "cooldown" de son ultime est de 0
            # instancier damage en appliquant l'effet(avec paramètre ultime, damage et target)
            # instancier la variable skill_used pour y attribuer la variable ultime
        # elif condition si la valeur de l'atout et le reste de la division de tour du perso par le "cooldown" de son ultime est de 0
            # instancier damage en appliquant l'effet(avec paramètre atout, damage et target)
            # instancier la variable skill_used pour y attribuer la variable atout

        # enlever les pv en comparant 0 et en fonction des dégâts reçus
        # renvoyer damage et skill_used 

    # crée la fonction pour appliquer un effet
        # instancier la variable effet 
        # instancier la variable valeur

        # condition effet sur boost d'attaque
            # augmenter dégâts
        #  elif condition effet sur boost defense
            # augmenter defense
        # elif condition effet sur heal
            # attribue à la variable pv une valeur qui est le minimum en comparant les pv maximum et les pv actuels + la valeur de soin
        # elif condition effet sur double_hit
            # double la valeur des dégâts

        # renvoyer damage

# crée la classe Monster héritée de la classe Character
    # pass pour remplir l'espace car classe héritée


