#include <stdio.h>
#include <stdbool.h>
#include <ctype.h>

void ordena(int arr[], int n){

    for (int i = 0; i < n -1; i++){
        bool swapeed = false;
        for (int j = 0; j < n; j++){ 
            if (arr[j] > arr[j + 1]){
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                swapeed = true;
            }
        }
        printf("Passo %d: ", i + 1);
        for (int k = 0; k < n; k++){
            printf("%d ", arr[k]);
        }

        printf("\n");
        if (!swapeed) break;
    }
}

void limparBuffer(){
    while (getchar() != '\n');
}

int main(){
    int arr[100];
    int n = 0;
    char opcao;

    printf("=== SISTEMA INTERATIVO DE ORDENACAO ===\n");
    printf("=== Bubble Sort em C ===\n\n");

    do {
        printf("Quantos numeros deseja ordenar (Maximo 100 numeros):\n");
        while (scanf("%d", &n) != 1 || n < 1 || n > 100){
            printf("Digite um numero entre 1 e 100: ");
            limparBuffer();
        }

        printf("\nDigite os %d numeros separados por espaco:\n", n);
        for(int i = 0; i < n; i++){
            while (scanf("%d", &arr[i]) !=1){
                printf("Entrada invalida. Digite um numero inteiro: ");
                limparBuffer();
            }
        }

        printf("\nArray original: ");
        for (int i = 0; i < n; i++) {
            printf("%d ", arr[i]);
        }
        printf("\n\n");

        ordena(arr, n);

        printf("\nArray ordenado: ");
        for (int i = 0; i < n; i++) {
            printf("%d ", arr[i]);
        }
        printf("\n\n");

        printf("Deseja ordenar outro conjunto? (s/n): ");
        limparBuffer();
        opcao = tolower(getchar());
        printf("\n");

    } while (opcao == 's');
    
    printf("Programa encerrado.\n");
    return 0;
}