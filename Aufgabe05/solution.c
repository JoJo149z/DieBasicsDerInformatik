#include <stdio.h>
#include <stdlib.h>

void print_array (int array [], int len) {
    // HIER Code einfügen
    printf("Array: ");
    for (int i = 0; i < len; i++) {
        printf("%d", array[i]);
        if (i < len - 1) {
            printf(", ");
        }
    }
    printf("\n");
}


void summe(int array[], int len, int *s) {
    int summe = array[0];
    for (int i = 1; i < len; i++){ 
        summe += array[i];

    }
    *s = summe;
}

int min(int array[], int len){
    int min = array[0];
    for (int i = 1; i < len; i++) {
        if (array[i]< min) {
            min = array[i];
        }
    }
    
    return min;
}

int max(int array[], int len){
    int max = array[0];
    for (int i = 1; i < len; i++) {
        if (array[i]> max) {
            max = array[i];
        }
    }
    
    return max;
}
// Schreibe die Funktion "sum", "min" und "max"

int main () {
    int array[] = {9, 4, 7, 8, 10, 5, 1, 6, 3, 2};
    int len = 10;
    int s;
    print_array (array , len);
    printf("Minimum: %d\n", min(array, len));
    printf("Maximum: %d\n", max(array, len));
    summe(array, len, &s);
    printf("Sum: %d\n", s);
    // Gebe hier nacheinander das Minimum , Maximum und die Summe
    // aus. Trenne die Werte durch einen einzelnen Zeilenumbruch .
}
