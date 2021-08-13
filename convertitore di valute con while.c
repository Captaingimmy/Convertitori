#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main() {
	printf("CONVERTITORE DI STRINGHE");
	printf("\n\n");
	
	printf("MENU{");
	printf("\n\n");
	
	printf("1.dollaro_to_euro");
	printf("\n\n");
	
	printf("2.euro_to_dollaro");
	printf("\n\n");

	printf("3.out");
	printf("\n\n");
	
	printf("}");
	printf("\n\n");
	printf("||||||ricordo gli elementi del menu devono essere scritti sul terminale come sono stati scritti qui sopra||||||");
	printf("\n\n");

	bool Trovato = true;

	while(Trovato){
		char risposta[40];
		printf("che conversione vuoi fare? ");
	    scanf("%s",&risposta);
	    Trovato = true;
	    float risultato  = 0;
		
		if(risposta[0] == 'd'){
			float ris;
			printf("quanti dollari vuoi convertire in euro? ");
			scanf("%f",&ris);
			risultato = ris * 0.85;
			printf(" il risultato e %.2f€\n\n",risultato);
	    }
		if(risposta[0] == 'e'){
			float ris;
			printf("quanti euro vuoi convertire in dollari? ");
			scanf("%f",&ris);
			risultato = ris * 1.17;
			printf("il risultato e %.2f$\n\n",risultato);
		}
		if(risposta[0] == 'o'){
			Trovato = false;
		}


	    	
	}
	
	return 0;
}
