#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>

bool isPrime(int nummer) {
    printf("Ist %d eine Primzahl ?\n", nummer);


    if (nummer < 0) {
        printf("nein\n");
    return false;
    }

    int rest;
    for(int a = 2; a<nummer; a++){
        rest = (nummer%a);
        
        if (rest == 0) {
            printf("nein\n");
            return false;
            
        }
        
    }

    
    // TODO HIER Code einfügen
    // Tipp: nutze eine for-loop
    printf("ja\n");
    return true;
}

int main() {
    isPrime(105);
    return 0;
}
