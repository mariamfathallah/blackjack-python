import random

def paquet() : 
    """on génére une paquet de 52 cartes"""
    paquets =[]
    carte1 =["As","Roi","Dame","Valet"]
    type1 = ["coeur","carreau","pique","trèfle"]
    for x in range(0,4) :
        for i in range(0,4) :
            paquets.append(carte1[i] + " de " + type1[x])
        for i in range(2,11) :
            paquets.append(str(i) + " de " + type1[x])
    return paquets   


def valeurCarte(carte) : 
    """on calcule la valeur de carte piochée"""
    val = 0
    if "As" in carte :
        valAs = int(input("Une carte AS a été tirée , choisissez entre 1 ou 11 points? "))
        if valAs == 1 :
            return 1
        elif valAs == 11 :
            return 11
    elif ("Roi" in carte)  or ("Dame" in carte) or ("Valet" in carte) or ("10" in carte) :
        val = 10
    else :
        rang = carte.split(" ")[0]
        val = int(rang)
        
    return val

def initPioche(n) : 
    """on a généré une pioche de n paquets (52 cartes) et on l'a mélangé, n est le nombre du joeueurs"""
    import random
    pioche = n * paquet()
    random.shuffle(pioche)
    return pioche


def piocheCarte(p, x=1) : 
    """cette fonction nous permet de piocher une ou des cartes du paquet, selon nos besoins, et les renvoyer dans une liste"""
    cartesPiochées = []
    j = 1
    while j <= x:
        pc = p.pop(0)
        cartesPiochées.append(pc)
        j += 1
    return cartesPiochées

def initJoueurs(n) : 
    """dans cette fonction on demande chaque joueur d'entrer son nom, et on l'a ajouté dans une liste"""
    i = 1
    joueurs = []
    while i <= n:
        print("Entrez le nom du joueur", i, ": ")
        nom = input()
        joueurs.append(nom)
        i += 1 
    return joueurs


def initScores(joueurs, v=0) : 
    """on construit un dictionnaire avec les noms des joueurs et leurs score(0 par défaut) """
    scores = {}
    i = 0
    while i < len(joueurs) :
        scores[joueurs[i]] = v
        i += 1
    return scores

def premierTour(joueurs): 
    """dans cette fonction le jeu commence par piocher 2 cartes pour chaque joueur et calculer ses valeurs en les ajoutant dans le dictionnaire des scores"""
    scores = initScores(joueurs, v=0) 
    c = 0    
    while c < len(joueurs) :
        print(joueurs[c], "vos cartes : ")
        i = 1
        while i <= 2:
            carte = piocheCarte(p)
            print(carte)
            carte_val = 0
            for cart in carte :
                carte_val += valeurCarte(cart)
            scores[joueurs[c]] += carte_val
            i += 1
        print()
        c += 1
    return scores


def gagnant(scores): 
    """cette fonction nous permet de savoir le gagnant et son score"""
    diff_dict = {}
    max_1 = 21
    max_joueur = None
    for k,v in scores.items():
        if v <= 21 and 21-v <= max_1:
            max_1 = 21-v
            max_joueur = k
    if max_joueur == None:
        return 'personne',0
    else:
        return max_joueur,scores[max_joueur]


def Continue(play):
    if play.upper() == 'OUI' :
        return True
    elif play.upper() == 'NON' :
        return False
    else:
        play = input("Réponse attendu 'Oui/Non'. Veuillez ressayer ")
        return Continue(play)


def tourJoueur(j,scores,joueurs) : 
    """cette fonction nous permet de faire un autre tour pour le joueur"""
    numero_du_tour = 2
    print("Numéro du tour = ", numero_du_tour)
    print("Nom du joueur : ", j)
    print("Total de la partie courante :", scores.get(j))
    play = input("Veux-tu continuer? Oui/Non ")
    while Continue(play):
        if scores.get(j) < 21:
            carte = piocheCarte(p)
            carte_val = 0
            for cart in carte:
                carte_val += valeurCarte(cart)
            scores[j] += carte_val
            print("Total de la partie courante :", scores.get(j))
            if scores.get(j) == 21:
                return joueurs
            elif scores.get(j) > 21:
                joueurs.remove(j)
                return joueurs
            else:
                play = input("Veux-tu continuer? Oui/Non ")
    joueurs.remove(j)
    return joueurs

def tourComplet(j,scores,joueurs) : 
    """cette fonction nous permet de faire un autre tour pour chaque joueur"""
    joueurs = tourJoueur(j,scores,joueurs)
    return joueurs

def partieFinie(scores,joueurs): 
    """ici on test si le jeu est terminé ou non"""
    if 21 in scores.values():
        return True
    if len(joueurs) == 0:
        return True
    else:
        t_counter = 0
        loss_counter = 0
        for s in scores.values():
            if s == 21:
                t_counter+=1
            if s > 21:
                loss_counter+=1
        if t_counter == len(joueurs):
            return True
        elif loss_counter == len(joueurs)-1:
            return False
        else:
            return False

def partieComplete(joueurs,victoire,scores): 
    """après etre sur que le jeu est terminé on renvoie le vainqueur"""
    for k in joueurs:
        victoire[k] = 0
   
    n = len(joueurs)
    numero_du_tour = 3
    while partieFinie(scores,joueurs) == False :  
        joueurs = tourComplet(joueurs[0],scores,joueurs)
        numero_du_tour += 1
    
    max_joueur,max_joueur_score = gagnant(scores)
    if max_joueur !='personne':
        victoire[max_joueur]+=1
    return victoire 



def mise(joueurs) :  
    """on demande au joueur de choisir combien ils veulent miser selon le nombre de kopecs disponible """
    i = 0
    mise = []
    while i < len(joueurs) :
        print(joueurs[i] , ", Votre mise? ")
        mise_1 = int(input())
        while mise_1 > 100 :
            mise_1 = int(input("Solde insuffisante , vous n'avez que 100 kopecs. Veuillez ressayer : "))
        mise.append(mise_1)    
        i+=1
    print("Chaque joueur recoit 2 Cartes !" )
    print("C'est le tour du Croupier")
    print()   # pour faire des espaces (aerer)
    return mise 

def croupier(p, mise) :
    mise_cr = 20
    mise.append(mise_cr)
    scores_croupier =[]
    i = 0

    carte1 = p[i]
    if 'As' in carte1 :
        carte1_val = 11
    else :
        carte1_val = valeurCarte(carte1)
    scores_croupier.append(carte1_val)
    print("premiere carte du croupier : ",carte1)
    print("Le score de Croupier  est ", carte1_val)
    print()
    p.remove(carte1)

    carte2 = p[i]
    if 'As' in carte2 :
        carte2_val = 1
    else :
        carte2_val = valeurCarte(carte2)
    scores_croupier.append(carte2_val)
    p.remove(carte2)

    return scores_croupier

def ecart(scores_croupier):
    while sum(scores_croupier) < 17:
        carte = piocheCarte(p)  # pioche 1 carte (retourne une liste)
        carte_val = 0
        for cart in carte:
            carte_val += valeurCarte(cart)
        scores_croupier.append(carte_val)
    return scores_croupier

def total(scores) :
    i = 0
    max_joueur,max_joueur_score = gagnant(scores)
    
    if scores[max_joueur] == sum(scores_croupier) and scores[max_joueur] != 21:
        print()
        print('Personne gagne !!!! ')
    elif sum(scores_croupier) < 21 and scores[max_joueur] < 21 and scores[max_joueur] < sum(scores_croupier):
        print()
        print("Croupier de score  ",sum(scores_croupier), " est superieur a vous")
        print("Croupier Gagne!!")
    elif sum(scores_croupier) < 21 and scores[max_joueur] < 21 and scores[max_joueur] > sum(scores_croupier):
            print()
            print("Vous etes superieur avec",scores[max_joueur] - sum(scores_croupier)," à ", sum(scores_croupier))
            print("Vous gagnez,", sum(mise), "kopecs")
            
    elif sum(scores_croupier) > 21:
            print('Croupier PERD , Vous gagnez!')
    elif scores[max_joueur] > 21 :
            print('Vous depassez 21 , vous perdez !')
            print("Croupier remporte la partie")
    
    if scores[max_joueur]== 21 :
        print()
        print('Blackjack!',max_joueur  , 'a remporter la partie, voici votre argent : ' , sum(mise), "kopecs" )
        
    
    if sum(scores_croupier) == 21 :
        print()
        print('Blackjack!, Le Croupier remporte la partie ! et vous perdez ')


paquet()
print("Bienvenue à BlackJack")
n = int(input("Entrez le nombre du joueur : "))
while n < 2 :
    n=int(input("nombre insuffisant de joueur. Veuillez entrer un autre nombre. "))

while n > 7 :
     n=int(input("nombre de joueur dépasse la limite. Veuillez entrer un autre nombre. "))
    
p = initPioche(n)
joueurs = initJoueurs(n)
players = list(joueurs)
mise = mise(joueurs)
scores_croupier = croupier(p, mise)
scores = premierTour(joueurs)
scores_croupier = ecart(scores_croupier)
i = 0
j = joueurs[i]
victoire = partieComplete(joueurs,{},scores)
total(scores)
