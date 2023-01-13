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
                self.left_child.insert(value)
                return
            self.left_child = Node(value)
            return

        '''Jeśli wstawiana wartośc jest większa od aktualnej wartości węzła
            oraz węzeł posiada prawe dziecko wywołujemy rekurencyjnie metodę wstawiania
            na prawym dziecku. Jeśli węzeł nie ma prawego dziecka, ustawiamy jego wartość
            na węzeł z wstawianą wartością'''
        if self.right_child:
            self.right_child.insert(value)
            return
        self.right_child = Node(value)
        return

    # Dopóki aktualny węzeł posiada lewe dziecko rekurencyjnie ustawiamy wartość na jego lewe dziecko
    def get_min_value(self):
        current_value = self
        while current_value.left_child is not None:
            current_value = current_value.left_child
        return current_value

    # Dopóki aktualny węzeł posiada prawe dziecko rekurencyjnie ustawiamy wartość na jego prawe dziecko
    def get_max_value(self):
        current_value = self
        while current_value.right_child is not None:
            current_value = current_value.right_child
        return current_value

    def find_value(self, value):
        pass

    def delete_value(self, value):
        pass
