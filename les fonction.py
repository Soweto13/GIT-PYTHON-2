
###print("Bonjour à tous!")

##abs(-6) # Donne la valeur absolue d'un nombre 
##len([1,2,3,4,5]) # Donne le nombre d'élément dans une séquence 
##input ("Entrer le nombre:") # faire une demande 
##open("fichier.txt") # De part le nom d'un fichier ou le chemin l'ouvrir et lire le contenu
  

  ### CREER UNE FONCTION PYTHON 
## Paramètres et argument d'une fonction 
# 1 La definition du code de la fonction 
#def salutation(Prenom,nom,age):  #Usage de plusieurs paramètre une virgule doit les séparer 
  #print(Prenom)
  #print(f"Bonjour {Prenom} {nom} / {age}")
  #print("T'es Radieux Aujourd'hui!") 

  #Usage de la fonction 
#salutation("Kismath", "Amoussa",24)

# Avoir des valeurs par defaut dans le paramétrage de la fonction plutôt mettre 

def salutation(Prenom,nom,age=27):  #Usage de plusieurs paramètre une virgule doit les séparer 
  print(Prenom)
  print(f"Bonjour {Prenom} {nom}/{age}")
  print("T'es Radieux Aujourd'hui!") 

  #Usage de la fonction 
salutation(Prenom="Kismath",nom="Gnansounou") # Si je commence à mettre le paramètre puisl'argument je doit continuer jusqu'a la fin 
print("hey")
