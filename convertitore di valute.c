#include <stdio.h>
#include <string.h>

int main() {
	printf("CONVERTITORE DI STRINGHE");
	printf("\n\n");
	
	printf("MENU{");
	printf("\n\n");
	
	printf("dollaro_to_euro");
	printf("\n\n");
	
	printf("euro_to_dollaro");
	printf("\n\n");
	
	printf("}");
	printf("\n\n");
	printf("||||||ricordo gli elementi del menu devono essere scritti sul terminale come sono stati scritti qui sopra||||||");
	printf("\n\n");
	
	char risposta[40];
	printf("che conversione vuoi fare? ");
	scanf("%s",&risposta);
	
	float risultato  = 0;

	if(risposta[0] == 'd'){
		float ris;
		printf("quanti dollari vuoi convertire in euro? ");
	    scanf("%f",&ris);
		risultato = ris * 0.85;
		printf(" il risultato e %.2f€",risultato);
		
	}
	if(risposta[0] == 'e'){
		float ris;
		printf("quanti euro vuoi convertire in dollari? ");
	    scanf("%f",&ris);
		risultato = ris * 1.17;
		printf("il risultato e %.2f$",risultato);
		
	}
		
	
	
	
    return 0;
}
