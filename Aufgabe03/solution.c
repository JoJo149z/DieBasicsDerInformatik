#include <stdio.h>
#include <stdlib.h>

int main() {
    int breite = -1;
    int hoehe = -1; 

    int ih = hoehe;
    if (breite >= 0 || hoehe >= 0){
    for(int ib = breite+2; ib != 0; ib--){
        printf("A");
    }
    printf("\n");
        
    while(ih != 0){
        printf("A");

        for(int ib = breite; ib != 0; ib--){
            printf("B");
        }
        printf("A\n");
         

        ih = ih-1;        
    }
    for(int ib = breite+2; ib != 0; ib--){
        printf("A");
    }
    printf("\n");

    }    

    // Hier Code einfügen

    return 0;
}
