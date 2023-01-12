// Funkcja scala dwie tablice w jedną.
void merge(int array[], int idxLeft, int idxMid, int idxRight) {
    // Obliczamy długości naszych pomocniczych podtablic. leftArray = [idxLeft do idxMid], rightArray[idxMid + 1 do idxRight].
    int leftArraySize = idxMid - idxLeft + 1;
    int rightArraySize = idxRight - idxMid;

    // Tworzymy dwie tablice pomocnicze.
    int leftArray[leftArraySize];
    int rightArray[rightArraySize];

    // Do tablic pomocniczych przydzielamy elementy głównej tablicy.
    for (int i = 0; i < leftArraySize; i++)
        leftArray[i] = array[idxLeft + i];
    for (int j = 0; j < rightArraySize; j++)
        rightArray[j] = array[idxMid + 1 + j];

    int currLeftIdx = 0; // Aktualny indeks lewej tablicy.
    int currRightIdx = 0; // Aktualny index prawej tablicy.
    int currArrIdx = idxLeft; // Aktualny indeks głównej tablicy.

    // Dopóki indeksy podtablic są mniejsze od ich długości, wybieramy większe elementy z obu oraz ustawiamy na odpowiednim miejscu głównej tablicy.
    while (currLeftIdx < leftArraySize && currRightIdx < rightArraySize) {
        if (leftArray[currLeftIdx] <= rightArray[currRightIdx]) {
            array[currArrIdx] = leftArray[currLeftIdx];
            currLeftIdx++;
        } else {
            array[currArrIdx] = rightArray[currRightIdx];
            currRightIdx++;
        }
        currArrIdx++;
    }

    // Jeśli w którejś z podtablic zostały jakieś elementy ustawiamy je w głównej tablicy.
    while (currLeftIdx < leftArraySize) {
        array[currArrIdx] = leftArray[currLeftIdx];
        currLeftIdx++;
        currArrIdx++;
    }

    while (currRightIdx < rightArraySize) {
        array[currArrIdx] = rightArray[currRightIdx];
        currRightIdx++;
        currArrIdx++;
    }
}

// Funkcja dzieli tablice na dwie podtablice, sortuje a następnie scala.
void mergeSort(int array[], int idxLeft, int idxRight) {
    // Jeśli indeks początkowy jest mniejszy od końcowego, tablica nie jest jeszcze posortowana.
    if (idxLeft < idxRight) {
        // Obliczamy indeks środkowego elementu głównej tablicy.
        int idxMid = (idxLeft + idxRight) / 2;

        // Wykonujemy rekurencyjnie naszą funkcję, dopóki nie otrzymamy jednoelementowych tablic.
        mergeSort(array, idxLeft, idxMid);
        mergeSort(array, idxMid + 1, idxRight);

        // Scalamy ze sobą podtablice.
        merge(array, idxLeft, idxMid, idxRight);
    }
}
