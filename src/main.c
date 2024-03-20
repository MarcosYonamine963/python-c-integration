#include <stdio.h>

int main(void)
{

    setbuf(stdout, NULL); // Desativar o buffering da saída padrão

    printf("C program started\n");

    char my_char;

    while (my_char != 'X') {


        my_char = getchar(); // Ler uma letra do stdin
        putchar(my_char);    // Imprimir a letra
        // fflush(stdout);      // Limpar o buffer de saída
    }

    return 0;
}
