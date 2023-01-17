class Node:
    # Konstruktor klasy
    def __init__(self, value=None):
        self.value = value
        self.left_son = None
        self.right_son = None
        self.parent = None

    # Metoda wstawiania wartości do drzewa
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
            if self.left_son:
                self.left_son.insert_value(value)
                self.left_son.parent = Node(self.value)
                return
            self.left_son = Node(value)
            self.left_son.parent = Node(self.value)
            return
        '''Jeśli wstawiana wartość jest większa od aktualnej wartości węzła oraz węzeł posiada prawe dziecko wywołujemy
        rekurencyjnie metodę wstawiania na prawym dziecku. Jeśli węzeł nie ma prawego dziecka, ustawiamy jego wartość
        na węzeł z wstawianą wartością'''

        if self.right_son:
            self.right_son.insert_value(value)
            self.right_son.parent = Node(self.value)
            return
        self.right_son = Node(value)
        self.right_son.parent = Node(self.value)
        return

    # Metoda zwracania najmniejszej wartości
    # Dopóki aktualny węzeł posiada lewe dziecko rekurencyjnie ustawiamy wartość na jego lewe dziecko.
    def get_min_value(self):
        current_node = self
        while current_node.left_son:
            current_node = current_node.left_son
        return current_node.value

    # Metoda zwracania maksymalnej wartości
    # Dopóki aktualny węzeł posiada prawe dziecko rekurencyjnie ustawiamy wartość na jego prawe dziecko.
    def get_max_value(self):
        current_node = self
        while current_node.right_son:
            current_node = current_node.right_son
        return current_node.value

    # Metoda zwracania ilości węzłów
    '''Jeśli węzeł nie ma wartości (puste drzewo) zwracamy 0, jeśli ma wartość zliczamy od 1 (liczymy korzeń).
    Jeśli jest lewe dziecko do licznika rekurencyjnie dodajemy wywoływaną na nim metodę zliczania..
    Jeśli jest prawe dziecko do licznika rekurencyjnie dodajemy wywoływaną na nim metodę zliczania.
    Na końcu zwracamy licznik.'''
    def get_node_count(self):
        if not self.value:
            return 0

        counter = 1
        if self.left_son:
            counter += self.left_son.get_node_count()
        if self.right_son:
            counter += self.right_son.get_node_count()
        return counter

    # Metoda szukania wartości w drzewie
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
            if not self.left_son:
                return False
            return self.left_son.find_value(value)

        if not self.right_son:
            return False
        return self.right_son.find_value(value)

    # Metoda usuwania wartości z drzewa
    '''Jeśli w drzewie nie ma wartości, którą chcemy usunąć, wypisujemy, że jej nie ma i zwracamy.
    Jeśli węzęł nie ma wartości zwracamy go. Jeśli wartość aktualnego węzła jest mniejsza od wartości do usunięcia,
    jako prawe dziecko ustawiamy prawe dziecko, na którym wykonujemy metodę usuwania.
    Jeśli wartość aktualnego węzła jest większa robimy to samo tylko na lewym dziecku.
    Jeśli węzeł nie ma dziecka zwracamy prawe dziecko. Jeśli węzeł nie ma prawego dziecka zwracamy lewe dziecko.
    Jako wartość minimalna ustawiamy najmniejszą wartość z prawego poddrzewa i przypisujemy ją jako wartość węzłą.
    Jako prawe dziecko ustawiamy prawe dziecko, na którym wykonujemy metodę usuwania wartości z wartością minimalną
    jako argumeny. Zwracamy węzęł.'''
    def delete_value(self, value):
        if not self.find_value(value):
            print("Number doesn't exist in Tree")
            return
        else:
            if not self.value:
                return self

            if self.value < value:
                self.right_son = self.right_son.delete_value(value)
                return self

            if self.value > value:
                self.left_son = self.left_son.delete_value(value)
                return self

            if not self.left_son:
                return self.right_son

            if not self.right_son:
                return self.left_son

            min_value = self.right_son.get_min_value()
            self.value = min_value
            self.right_son = self.right_son.delete_value(min_value)
            return self

    # Metoda wyświetlania drzewa w 2d
    '''Jeśli węzeł nie ma wartości zwracamy. Do zmiennej dystans dodajemy wysokość. Jeśli prawe dziecko istnieje
    wykonujemy na nim metodę wyświetlania. Dopóki wysokość jest większa od dystansu w każdej iteracji wyświetlamy spację
    i do wysokości dodajemy 1. Wypisujemy wartość węzła. Jeśli lewy syn istnieje wykonujemy na nim metodę
    wyświetlania.'''
    def display(self, distance=0, height=10):
        if not self.value:
            return

        distance += height
        if self.right_son:
            self.right_son.display(distance, height)

        while height < distance:
            print("", end=' ')
            height += 1

        print(self.value)

        if self.left_son:
            self.left_son.display(distance, height)

    # Metoda wyświetlania drzewa preorder
    '''Wypisujemy wartość aktualnego węzła. Jeśli węzeł ma lewego syna wykonujemy na nim metodę rekurencyjnie.
    Jeśli węzeł ma prawego syna wykonujemy na nim metodę rekurencyjnie."'''
    def display_preorder(self):
        if not self.parent:
            print("Preorder: ", end='')
        if self.value:
            print(self.value, end=' ')
        if self.left_son:
            self.left_son.display_preorder()
        if self.right_son:
            self.right_son.display_preorder()

    # Metoda wyświetlania drzewa inorder
    '''Jeśli węzeł ma lewego syna wykonujemy na nim metodę rekurencyjnie. Wypisujemy wartość aktualnego węzła.
    Jeśli węzeł ma prawego syna wykonujemy na nim metodę rekurencyjnie.'''
    def display_inorder(self):
        if not self.parent:
            print("Inorder: ", end='')
        if self.left_son:
            self.left_son.display_inorder()
        if self.value:
            print(self.value, end=' ')
        if self.right_son:
            self.right_son.display_inorder()

    # Metoda wyświetlania drzewa postorder
    '''Jeśli węzeł ma lewego syna wykonujemy na nim metodę rekurencyjnie.  Wypisujemy wartość aktualnego węzła.
    Jeśli węzeł ma prawego syna wykonujemy na nim metodę rekurencyjnie.'''
    def display_postorder(self):
        if not self.parent:
            print("Postorder: ", end='')
        if self.left_son:
            self.left_son.display_postorder()
        if self.right_son:
            self.right_son.display_postorder()
        if self.value:
            print(self.value, end=' ')
