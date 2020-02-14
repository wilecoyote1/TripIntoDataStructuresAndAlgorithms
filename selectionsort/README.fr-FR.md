# tri par sélection

le tri par sélection est sans doute l'algorithme de tri le plus simple ou en tout cas un des premiers exemples qui vienne à l'esprit lorsque l'on cherche à créer un algorithme de tri.

## description
Sur un tableau de n éléments (numérotés de 1 à n), le principe du tri par sélection est le suivant :

* rechercher le plus petit élément du tableau, et l'échanger avec l'élément d'indice 1 ;
* rechercher le second plus petit élément du tableau, et l'échanger avec l'élément d'indice 2 ;
* continuer de cette façon jusqu'à ce que le tableau soit entièrement trié.

## complexité
Dans tous les cas, pour trier n éléments, le tri par sélection effectue n(n-1)/2 comparaisons. Sa complexité est donc Θ(n2). De ce point de vue, il est inefficace puisque les meilleurs algorithmes1 s'exécutent en temps {\displaystyle O(n\,\log n)} O(n\,\log n). Il est même moins bon que le tri par insertion ou le tri à bulles, qui sont aussi quadratiques dans le pire cas mais peuvent être plus rapides sur certaines entrées particulières.

## sources
*SelectionSort.java* algorithme de tri par sélection en Java
*SelectionSortDemo.java* Démonstration du tri par sélection en Java. Pour utiliser cet exemple, exécuter la commande
```
javac SelectionSortDemo.java
java SelectionSortDemo
```


*selectionsort.py* algorithme de tri par insertion en python
v*selectionsort_demo.py* exemple d'utilisation du tri par sélection. Pour utiliser cet exemple, exécuter la commande
```
python3 selectionsort_demo.py
```

## Références

[Wikipédia](https://fr.wikipedia.org/wiki/Tri_par_s%C3%A9lection)