#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Correct usage: ./recover IMAGE\n");
        return 1;
    }

    char* inputFile = argv[1];
    if(inputFile == NULL)
    {
        printf("Cannot open file: %s\n", inputFile);
        return 1;
    }

    unsigned char buffer[512];
    FILE* inputPtr = fopen(inputFile, "r");
    fread(buffer, sizeof(char), 512, inputPtr);

    

}
