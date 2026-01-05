#include <stdio.h>
#include <stdlib.h>

int main() {
    int breite = 6;
    int hoehe = 3; 

    int ih = hoehe;
    
    while(ih != 0){
        printf("A");

        for(int ib = breite; ib != 0; ib--){

            if( ih == hoehe|| ih == 1){
                printf("A");
            }else{
                printf("B");
            }
            
        }
        printf("A\n");
         

        ih = ih-1;        
    }

    

    // Hier Code einfügen

    return 0;
}
