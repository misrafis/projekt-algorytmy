#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++)
        std::cout << arr[i] << " ";
}

int getArraySize(string fileName) {
    int size = 0;
    ifstream File;
    File.open(fileName);
    if(File.is_open()) {
        File >> size;
    }
    File.close();
    return size;
}

void getArrayFromFile(int array[], string fileName) {
    int arraySize = 0;
    int counter = 1;
    ifstream File;
    File.open(fileName);
    File.clear();
    if(File.is_open()) {
        File >> arraySize;
        while(counter < arraySize + 1) {
            cout << counter << endl;
            File >> array[counter - 1];
            counter++;
        }
    }
    File.close();
}

void writeArrayToFile(int array[], int arraySize, auto duration, string sortType, string fileName) {
    if(sortType == "mergeSort") {
        sortType = "scalanie";
    }
    if(sortType == "insertionSort") {
        sortType = "wstawianie";
    }
    ofstream File;
    File.open(fileName);
    File.clear();
    if(File.is_open()) {
        File << "Sortowanie przez "<< sortType <<" dla tablicy o " << arraySize << " elementow - czas: " << duration << "ms" << endl;
        File << arraySize << endl;
        for(int i = 0; i < arraySize; i++) {
            File << array[i] << " ";
        }
    }
    File.close();
}

void printVector(const std::vector<string> &vector) {
    for (const auto &item : vector) {
        std::cout << item << " ";
    }
}
