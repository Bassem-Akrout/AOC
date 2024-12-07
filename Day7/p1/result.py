class Tree:
    def __init__(self):
        # self.nodes stocke : node -> {"value": <valeur associée>, "children": [liste_des_enfants]}
        self.nodes = {}
        # Ensemble pour stocker les feuilles (identifiants de nœuds)
        self.leaves = set()
        # Racine éventuelle
        self.root = None
    
    def add_node(self, node, value=None):
        """Ajoute un nœud sans enfant (initialement une feuille) avec une valeur."""
        if node not in self.nodes:
            self.nodes[node] = {"value": value, "children": []}
            self.leaves.add(node)
            if self.root is None:
                self.root = node
        else:
            # Le nœud existe déjà, on met à jour sa valeur
            self.nodes[node]["value"] = value

    def add_child(self, parent, child, value=None):
        """Ajoute un nœud enfant (avec une valeur) à un parent existant."""
        if parent not in self.nodes:
            raise ValueError("Le parent n'existe pas dans l'arbre.")
        
        # Ajouter l’enfant (nouvelle feuille)
        if child not in self.nodes:
            self.nodes[child] = {"value": value, "children": []}
            self.leaves.add(child)
        else:
            # Si le nœud existe déjà, on met à jour sa valeur
            self.nodes[child]["value"] = value

        # Mettre à jour la relation parent-enfant
        self.nodes[parent]["children"].append(child)

        # Le parent n’est plus une feuille s’il l’était
        if parent in self.leaves:
            self.leaves.remove(parent)

    def is_leaf(self, node):
        """Vérifie si un nœud est une feuille en O(1)."""
        return node in self.leaves

    def get_leaves(self):
        """Retourne un set des feuilles."""
        return self.leaves

    def pretty_print(self, node=None, level=0):
        """Affiche l'arbre de manière hiérarchique avec les valeurs."""
        if node is None:
            node = self.root
        if node is None:
            print("L'arbre est vide.")
            return
        value = self.nodes[node]["value"]
        print("  " * level + f"- {node} (val={value})")
        for child in self.nodes[node]["children"]:
            self.pretty_print(child, level + 1)

    def __repr__(self):
        return f"Arbre(nodes={self.nodes}, leaves={self.leaves}, root={self.root})"


def parse_input_to_matrix(input_file):
    matrix = []
    with open(input_file, 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            left_number = int(parts[0])  # Nombre avant ':'
            right_numbers = list(map(int, parts[1].strip().split()))  # Nombres après ':'
            matrix.append([left_number] + right_numbers)
    return matrix


def check_combin(lst):
    result = lst[0]
    numbers = lst[1:]
    if not numbers:
        # S’il n’y a pas de nombres pour tenter de parvenir à "result"
        return False

    root = Tree()
    node_counter = 0
    def new_node_name():
        nonlocal node_counter
        name = f"node{node_counter}"
        node_counter += 1
        return name

    # Créer le nœud racine
    root_node = new_node_name()
    root.add_node(root_node, value=numbers[0])

    # Pour chaque nombre suivant, générer de nouveaux enfants pour chaque feuille
    for depth in range(1, len(numbers)):
        current_number = numbers[depth]
        # On copie la liste des feuilles actuelle car on va en ajouter pendant l'itération
        current_leaves = list(root.get_leaves())
        for leaf in current_leaves:
            leaf_value = root.nodes[leaf]["value"]
            # Ajouter enfant (addition)
            add_child_node = new_node_name()
            root.add_child(leaf, add_child_node, value=leaf_value + current_number)
            # Ajouter enfant (multiplication)
            mul_child_node = new_node_name()
            root.add_child(leaf, mul_child_node, value=leaf_value * current_number)
            
    
    # Vérifier si une feuille possède la valeur "result"
    for leaf in root.get_leaves():
        if root.nodes[leaf]["value"] == result:
            return True
    return False


def main():
    matrix = parse_input_to_matrix("input.txt")
    total_sum = 0
    for lst in matrix:
        if check_combin(lst):
            total_sum += lst[0]
    print("Somme totale :", total_sum)


if __name__ == "__main__":
    main()
