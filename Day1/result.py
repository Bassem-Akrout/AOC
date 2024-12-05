# Lecture et parsing avec tri en une seule passe
import heapq

# Ouvrir le fichier et lire les lignes
with open('input1.txt', 'r') as fichier:
    # Initialiser les heaps (tas) pour les deux colonnes
    colonne1 = []
    colonne2 = []

    # Lire et ajouter chaque valeur dans le heap correspondant
    for ligne in fichier:
        valeurs = ligne.strip().split()
        heapq.heappush(colonne1, int(valeurs[0]))
        heapq.heappush(colonne2, int(valeurs[1]))
    left_heap=colonne1.copy()
    right_heap=colonne2.copy()
# Apparier les plus petits éléments et calculer la différence
differences = []
while colonne1 and colonne2:
    min1 = heapq.heappop(colonne1)  # Plus petit élément de colonne1
    min2 = heapq.heappop(colonne2)  # Plus petit élément de colonne2
    differences.append(abs(min1 - min2))


# Afficher les résultats
#print("Différences:", differences)
print("Somme des distances:", sum(differences))



from collections import Counter

# Transformer les heaps en dictionnaires d'occurrences
def heap_to_counter(heap):
    counter = Counter()
    while heap:
        num = heapq.heappop(heap)
        counter[num] += 1
    return counter

# Compter les occurrences
left_counts = heap_to_counter(left_heap)
right_counts = heap_to_counter(right_heap)

# Calculer le score de similarité
similarity_score = 0
for num, count in left_counts.items():
    similarity_score += num * count * right_counts.get(num, 0)

# Résultat
print("Score de similarité :", similarity_score)