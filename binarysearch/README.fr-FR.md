# recherche dichotomique (biarysearch)

## principe en une ligne

pour rechercher un élément dans une liste triée, prendre le milieu de la liste et regarder si la valeur du milieu est la valeur recherchée ou alors est inférieure ou supérieure. Si c'est le cas, continuer la recherche sur la moitié de la liste qui incadre la valeur.

## description

Sur un tableau de n éléments trié par ordre croissant, je cherche la valeur v:

* prendre la valeur du milieu de la liste.
* si la valeur correspond à la valeur du milieu, on a trouvé la bonne valeur. Retourner l'indice
* si la valeur recherchée est inférieure au milieu, prendre comme nouveau tableau de recherche l'encadrement du début de la liste et le mileu
* si la valeur recherchée est supérieure au milieu, prendre comme nouveau tableau de recherche l'encadrement du milieu et de la fin de la liste
* si le tableau est vide, retourner -1 (la valeur n'a pas été trouvée)


## complexité
Le nombre maximale de recherche est log2n. Dans un tableau de 8 valeur, il faut 3 essai maximum (log3) pour trouver la valeur (8->4->2->1). Dans un tableau de 1024, il faut 10 essais (log10) (1024->512->256->128->64->32->16->8->4->2->1).

## sources
*binarysearch.py* algorithme de recherche dichotomique en python
*binarysearch_demo.py* exemple d'utilisation de la recherche dichotomique. Pour utiliser cet exemple, exécuter la commande
```
python3 binarysearch_demo.py
```

## Références

[Wikipédia](https://fr.wikipedia.org/wiki/Recherche_dichotomique)