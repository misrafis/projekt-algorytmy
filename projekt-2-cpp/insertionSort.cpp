// Funkcja sortuje tablicę poprzez wstawianie elementów na odpowiednie indeksy.
void insertionSort(int array[], int size) {
    // Za iterator bierzemy step = 1, ponieważ zakładamy, że pierwszy element jest posortowany.
    for (int i = 1; i < size; i++) {
        int currElement = array[i]; // Do zmiennej currElement przypisujemy liczbę, którą chcemy wstawić w odpowiednie miejsce.
        int j = i - 1;

        // Dopóki po lewej stronie są większe liczby
        while (currElement > array[j] && j >= 0) {
            array[j + 1] = array[j]; // Przesuwamy je o jeden indeks w prawo
            --j;
        }

        array[j + 1] = currElement; // Wstawiamy liczbę na odpowiednie miejsce.
    }
}
