# crée la classe Character 
class Character:

    # definir les paramètres initaux de la classe characters
    def __init__(self, name, atk, defense, pv, atout, ultime):
        # instancier les variables selon le paramètre self
        # instancier la variable name
        self.name = name
        # instancier la variable attaque
        self.atk = atk
        # instancier la variable defense
        self.defense = defense
        # instancier la variable pv
        self.pv = pv
        # instancier la variable pv maximum
        self.max_pv = pv
        # instancier la variable atout
        self.atout = atout
        # instancier la variable ultime
        self.ultime = ultime
        # instancier la variable tour à 0
        self.tour = 0

    # crée la fonction pour voir si un personnage est en vie
    def is_alive(self):
        # renvoyer le personnage ayant des points de vie
        return self.pv > 0

    # crée la fonction d'attaque 
    def attack(self, target):
        # incrémenter tour
        self.tour -= 1
        # instancier la variable damage avec comparer 1 et la valeur atk du personnage qui attaque moins la valeur de la defense de l'unité qui reçoit
        damage = max(1, self.atk - target.defense)
        # instancier ma variable skill_used comme null
        skill_used = None

        # condition si la valeur de l'ultime  et le reste de la division de tour du perso par le "cooldown" de son ultime est de 0
        if self.ultime and self.tour % self.ultime["cooldown"] == 0:
            # instancier damage en appliquant l'effet(avec paramètre ultime, damage et target)
            damage = self.apply_effect(self.ultime, damage, target)
            # instancier la variable skill_used pour y attribuer la variable ultime
            skill_used = self.ultime["name"]
        # elif condition si la valeur de l'atout et le reste de la division de tour du perso par le "cooldown" de son ultime est de 0
        if self.atout and self.tour % self.ultime["cooldown"] == 0:
            # instancier damage en appliquant l'effet(avec paramètre atout, damage et target)
            damage = self.apply_effect(self.atout, damage, target)
            # instancier la variable skill_used pour y attribuer la variable atout
            skill_used = self.atout["name"]

        # enlever les pv en comparant 0 et en fonction des dégâts reçus
        target.pv -= damage
        # renvoyer damage et skill_used 
        return damage, skill_used

    # crée la fonction pour appliquer un effet
    def apply_effect(self, skill, damage, target):
        # instancier la variable effet 
        effet = skill["effet"]
        # instancier la variable valeur
        valeur = skill["valeur"]

        # condition effet sur boost d'attaque
        if effet == "atk_boost":
            # augmenter dégâts
            damage += valeur
        #  elif condition effet sur boost defense
        if effet == "def_boost":
            # augmenter defense
            self.defense += valeur
        # elif condition effet sur heal
        if effet == "heal":
            # attribue à la variable pv une valeur qui est le minimum en comparant les pv maximum et les pv actuels + la valeur de soin
            self.pv = min(self.max_pv, self.pv + valeur)
        # elif condition effet sur double_hit
        if effet == "double_hit":
            # double la valeur des dégâts
            damage *=2

        # renvoyer damage
        return damage

# crée la classe Monster héritée de la classe Character
class Monster(Character):
    # pass pour remplir l'espace car classe héritée
    pass

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
    return Monster(
        name=monster_data["name"],
        atk=monster_data["atk"],
        defense=monster_data["def"],
        pv=monster_data["pv"],
        atout=monster_data["atout"],
        ultime=monster_data["ultime"]
    )