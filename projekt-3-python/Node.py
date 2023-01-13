class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_value(self, value):
        # Jeśli węzeł nie ma wartości wstawiamy podaną wartość
        if not self.value:
            self.value = value
            return

        # Jeśli wartość węzła jest równa podanej wartości, nic nie robimy
        if self.value == value:
            return

        '''Jeśli wstawiana wartość jest mniejsza od aktualnej wartości węzła
            oraz węzeł posiada lewe dziecko wywołujemy rekurencyjnie metodę wstawiania
            na lewym dziecku. Jeśli węzeł nie ma lewego dziecka, ustawiamy jego wartość
            na węzeł z wstawianą wartością'''
        if value < self.value:
            if self.left_child:
                self.left_child.insert_value(value)
                return
            self.left_child = Node(value)
            return

        '''Jeśli wstawiana wartośc jest większa od aktualnej wartości węzła
            oraz węzeł posiada prawe dziecko wywołujemy rekurencyjnie metodę wstawiania
            na prawym dziecku. Jeśli węzeł nie ma prawego dziecka, ustawiamy jego wartość
            na węzeł z wstawianą wartością'''
        if self.right_child:
            self.right_child.insert_value(value)
            return
        self.right_child = Node(value)
        return

    # Dopóki aktualny węzeł posiada lewe dziecko rekurencyjnie ustawiamy wartość na jego lewe dziecko
    def get_min_value(self):
        current_node = self
        while current_node.left_child is not None:
            current_node = current_node.left_child
        return current_node.value

    # Dopóki aktualny węzeł posiada prawe dziecko rekurencyjnie ustawiamy wartość na jego prawe dziecko
    def get_max_value(self):
        current_node = self
        while current_node.right_child is not None:
            current_node = current_node.right_child
        return current_node.value

    '''Jeśli wartość aktualnego węzła jest równa szukanej wartości zwracamy jego wartość.
        Jeśli szukana wartość jest mniejsza sprawdzamy czy istnieje lewe dziecko,
        jeśli nie, to szukanej wartości nie ma w drzewie,
        Jeśli lewe dziecko istnieje to rekurencyjnie wywołujemy na nim metodę szukania.
        Jeśli szukana wartość jest większa sprawdzamy czy istnieje prawe dziecko,
        jeśli nie, to szukanej wartości nie ma w drzewie,
        jeśli prawe dziecko istnieje to rekurencyjnie wywołujemy na nim metodę szukania.'''
    def find_value(self, value):
        if self.value == value:
            return value

        if value < self.value:
            if self.left_child is None:
                return None
            return self.left_child.find_value(value)

        if self.right_child is None:
            return None
        return self.right_child.find_value(value)

    def delete_value(self, value):
        pass
