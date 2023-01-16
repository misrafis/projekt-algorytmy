import math
import math


class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None

    def insert_value(self, value):
        # Jeśli węzeł nie ma wartości wstawiamy podaną wartość
        if not self.value:
            self.value = value
            return

        # Jeśli wartość węzła jest równa podanej wartości, nic nie robimy
        if self.value == value:
            return

        '''Jeśli wstawiana wartość jest mniejsza od aktualnej wartości węzła oraz węzeł posiada lewe dziecko wywołujemy
        rekurencyjnie metodę wstawiania na lewym dziecku. Jeśli węzeł nie ma lewego dziecka, ustawiamy jego wartość
        na węzeł z wstawianą wartością'''
        if value < self.value:
            if self.left_child:
                self.left_child.insert_value(value)
                self.left_child.parent = Node(self.value)
                return
            self.left_child = Node(value)
            self.left_child.parent = Node(self.value)
            return
        '''Jeśli wstawiana wartość jest większa od aktualnej wartości węzła oraz węzeł posiada prawe dziecko wywołujemy
        rekurencyjnie metodę wstawiania na prawym dziecku. Jeśli węzeł nie ma prawego dziecka, ustawiamy jego wartość
        na węzeł z wstawianą wartością'''

        if self.right_child:
            self.right_child.insert_value(value)
            self.right_child.parent = Node(self.value)
            return
        self.right_child = Node(value)
        self.right_child.parent = Node(self.value)
        return

    # Dopóki aktualny węzeł posiada lewe dziecko rekurencyjnie ustawiamy wartość na jego lewe dziecko.
    def get_min_value(self):
        current_node = self
        while current_node.left_child:
            current_node = current_node.left_child
        return current_node.value

    # Dopóki aktualny węzeł posiada prawe dziecko rekurencyjnie ustawiamy wartość na jego prawe dziecko.
    def get_max_value(self):
        current_node = self
        while current_node.right_child:
            current_node = current_node.right_child
        return current_node.value

    '''Jeśli węzeł nie ma wartości (puste drzewo) zwracamy 0, jeśli ma wartość zliczamy od 1 (liczymy korzeń).
    Jeśli jest lewe dziecko do licznika rekurencyjnie dodajemy wywoływaną na nim metodę zliczania..
    Jeśli jest prawe dziecko do licznika rekurencyjnie dodajemy wywoływaną na nim metodę zliczania.
    Na końcu zwracamy licznik.'''
    def get_node_count(self):
        if not self.value:
            return 0

        counter = 1
        if self.left_child:
            counter += self.left_child.get_node_count()
        if self.right_child:
            counter += self.right_child.get_node_count()
        return counter

    '''Jeśli wartość aktualnego węzła jest równa szukanej wartości zwracamy jego wartość.
    Jeśli szukana wartość jest mniejsza sprawdzamy czy istnieje lewe dziecko,
    jeśli nie, to szukanej wartości nie ma w drzewie,
    Jeśli lewe dziecko istnieje to rekurencyjnie wywołujemy na nim metodę szukania.
    Jeśli szukana wartość jest większa sprawdzamy czy istnieje prawe dziecko,
    jeśli nie, to szukanej wartości nie ma w drzewie,
    jeśli prawe dziecko istnieje to rekurencyjnie wywołujemy na nim metodę szukania.'''
    def find_value(self, value):
        if not self.value:
            return False

        if self.value == value:
            return True

        if value < self.value:
            if not self.left_child:
                return False
            return self.left_child.find_value(value)

        if not self.right_child:
            return False
        return self.right_child.find_value(value)

    def delete_value(self, value):
        if not self:
            return self

        if self.value < value:
            self.right_child = self.right_child.delete_value(value)
            return self

        if self.value > value:
            self.left_child = self.left_child.delete_value(value)
            return self

        if not self.left_child:
            return self.right_child

        if not self.right_child:
            return self.left_child

        min_value = self.right_child.get_min_value()

        self.value = min_value
        self.right_child = self.right_child.delete_value(min_value)
        return self

    def display(self):
        pass

    def display_preorder(self):
        if not self.parent:
            print("Preorder: ", end='')
        if self.value:
            print(self.value, end=' ')
        if self.left_child:
            self.left_child.display_preorder()
        if self.right_child:
            self.right_child.display_preorder()

    def display_inorder(self):
        if not self.parent:
            print("Inorder: ", end='')
        if self.left_child:
            self.left_child.display_inorder()
        if self.value:
            print(self.value, end=' ')
        if self.right_child:
            self.right_child.display_inorder()

    def display_postorder(self):
        if not self.parent:
            print("Postorder: ", end='')
        if self.left_child:
            self.left_child.display_postorder()
        if self.right_child:
            self.right_child.display_postorder()
        if self.value:
            print(self.value, end=' ')

    def get_height(self):
        pass
